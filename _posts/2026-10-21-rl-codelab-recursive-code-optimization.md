---
layout: single
title: "Can Dueling DQN Stabilize Self-Improving Code? A Colab Experiment"
date: 2026-10-21
permalink: /posts/rl-codelab-rsi/
author_profile: true
tags:
  - reinforcement-learning
  - recursive-self-improvement
  - research-engineering
  - code-optimization
  - ablation
---

*I tested an idea from reinforcement learning against a small, real program-optimization loop: can a slowly updated critic help a system choose better improvements to its own code? The answer is less conclusive than the best-looking bar chart.*

[**Open the reproducible Colab notebook**](https://colab.research.google.com/github/Vedant2100/vedant2100.github.io/blob/master/projects/rl-recursive-code-optimizer/RSI_CodeLab_Colab.ipynb) · [**Source and methodology**](https://github.com/Vedant2100/vedant2100.github.io/tree/master/projects/rl-recursive-code-optimizer) · [**Raw held-out results**](https://github.com/Vedant2100/vedant2100.github.io/blob/master/projects/rl-recursive-code-optimizer/results/codelab_heldout_results.csv)

## The motivation: a moving evaluator

In DQN, a model learns from bootstrapped targets based on estimates from another model. If the estimating network and its target change rapidly together, training can oscillate. A target network, Double DQN, and the dueling value/advantage architecture address different aspects of that instability.

Recursive self-improvement (RSI) systems face a superficially similar issue: they propose modifications, use measurements to decide which to keep, and then propose further modifications from the changed system. I wanted to test the *mechanism*, not assume the analogy was already proven.

The question I put into code was:

> If a controller learns to pick successive program optimizations, do RL target-network techniques improve its ability to choose good modifications on workloads it has not trained on?

That is narrower than creating a self-improving language model. It is a useful engineering question, however, because it forces an evaluator, candidate modifications, real execution, regression checks, and a held-out test.

## The executable code gym

I implemented k-nearest-neighbor search with 24 configurations assembled from executable NumPy building blocks: naive broadcasting, matrix-multiplication distance computation, chunked matrix multiplication, full sorting versus partial selection, and precision/chunk-size choices. Not every configuration is a distinct source-level algorithm: chunk size does not affect the non-chunked variants.

At each step, the controller can propose one of six edits to the current program configuration. We execute *each candidate family* on benchmark workloads beforehand, check that its nearest-neighbor indices match a double-precision brute-force reference, and cache measured latencies. During RL training, action feedback comes from that table of real runs. A faster valid edit is accepted; a slower edit is rejected. Each episode allows five proposals.

The distinction matters: **the RL rollout uses cached measurements, not live recompilation, and no LLM writes the source code.** This isolates the edit-selection problem while keeping the reward attached to working code.

```text
current kNN implementation
        │
        ▼
RL controller picks a code edit
        │
        ▼
candidate configuration → verified measured latency
        │
        ├─ faster and correct → accept
        └─ slower or incorrect → reject
        │
        ▼
log speed improvement → replay buffer → Q-network update
        └───────────────────────────────────────────┐
                         next edit ◀────────────────┘
```

## What I ablated

Every policy gets a five-edit budget on the same initial code. I trained on four input shapes, froze network parameters, and measured outcomes on three different held-out shapes. Six seeded runs per method yielded 90 held-out method/workload/seed outcomes.

| Arm | Key mechanism |
| --- | --- |
| Random edits | No learned controller |
| Online-only DQN | Bootstrap from the live Q-network |
| Target DQN | Periodically copied target network |
| Double DQN | Online argmax, hard-target evaluation |
| Dueling Double DQN + EMA | Separate value and advantage streams, Double DQN, slowly updated target |

All learned methods use replay, the same network-width budget, 75 training episodes per seed, and the same action budget at test time. The combined arm is *not* a clean single-variable test of dueling or EMA, and should not be interpreted as one.

The connected Colab runtime was a **Tesla T4**. PyTorch used its GPU for network training; the benchmarked NumPy kernels ran on the runtime's CPU. The six notebook code cells all executed, with **96/96 calibration and 72/72 held-out correctness checks passing**.

## The results

![Held-out five-edit speedup chart](/images/rsi-codelab-heldout.svg)

| Method | Geometric mean speedup against original code |
| --- | ---: |
| Random | **10.22×** |
| Online-only DQN | **12.38×** |
| Hard-target DQN | **12.26×** |
| Double DQN | **12.21×** |
| Dueling Double DQN + EMA | **12.02×** |

On a fresh Colab T4 rerun, **online-only DQN ranked first**, with a geometric 12.38× speedup versus 10.22× for random. Its seed-paired mean log-speedup difference was **+0.191**. A two-sided Wilcoxon comparison yielded **p = 0.0625 before correction**; with Holm correction for the four comparisons, **all adjusted p-values were 0.25**. In this rerun the combined dueling/Double/EMA model ranked below each other learned controller. This variability itself is a reason not to overinterpret any single run.

**My conclusion is not that soft updates work for RSI.** The rerun found no statistically reliable improvement from target networks, and its ranking reversed the earlier run. It cannot disentangle which of the combined mechanisms matters, and six seeds are too few for confidence. The large absolute speedups are unsurprising because the original program intentionally uses a costly broadcast distance computation; optimizing that baseline does not establish an advance over an optimized nearest-neighbor library.

## The most important failure modes

**Cached metrics create a simpler world than an autonomous agent faces.** In real automated AI research, a proposed change might require training, cause nondeterministic failures, or exploit the evaluator. Here the entire finite family can be benchmarked in advance. That makes this a test of RL *selection*, not automated hypothesis discovery.

**Correctness is necessary but not sufficient.** The oracle checks exact neighbor indices on sampled inputs. Production-ready optimizations would need much broader correctness and numerical-stability tests, different hardware, resource limits, and careful measurement methodology.

**Held-out workload shapes are not held-out code families.** Every held-out evaluation still chooses among the same 24 implementation configurations. Transfer to new algorithm families remains unknown.

**The comparison combines mechanisms.** Dueling Double DQN + EMA outperformed the random baseline descriptively. That does not identify whether dueling, Double DQN, EMA, replay, or random variation drove the outcome. A factorial ablation with many more seeds would be needed.

## Connection to the larger research problem

[Darwin Gödel Machine](https://arxiv.org/abs/2505.22954) uses empirical feedback to evolve coding agents. [RRSI](https://arxiv.org/abs/2609.24972) studies regularized evolution of an agent's harness and shows why improvement on the evolution tasks can fail to transfer. [Eureka](https://arxiv.org/abs/2310.12931) uses LLM-authored code in an iterative reward-design loop. These are much richer systems than this notebook.

The next meaningful test would let an LLM propose **genuinely new code patches**, run sandboxed tests and performance measurements, and train a conservative controller to choose which hypotheses to spend the next compute budget on. At that point we could compare a frozen critic, EMA teacher, Double DQN, and acceptance gates while measuring both performance and harmful regressions. Such a study would need leakage-resistant held-out tasks and budget-matched search.

For now, the outcome is a working and auditable **RL-governed code-optimization prototype**. The most transferable lesson is methodological: verify that improvements actually run, separate calibration from held-out evaluation, publish negative results, and avoid inferring a new algorithm from one appealing chart.

**[Notebook](https://github.com/Vedant2100/vedant2100.github.io/blob/master/projects/rl-recursive-code-optimizer/RSI_CodeLab_Colab.ipynb)** · **[CSV data and exact statistical report](https://github.com/Vedant2100/vedant2100.github.io/tree/master/projects/rl-recursive-code-optimizer/results)** · **[Methodology and reproduction](https://github.com/Vedant2100/vedant2100.github.io/blob/master/projects/rl-recursive-code-optimizer/README.md)**
