---
layout: single
title: "ReplayGate: where should an adapting system keep its experience?"
date: 2026-10-19
permalink: /posts/continual-agent-learning/
author_profile: true
tags:
  - continual-learning
  - replay
  - agents
  - evaluations
---

*One real, executed experiment on the tradeoff between adapting model weights and retaining examples in memory.*

[**Explore the new interactive results dashboard**](/replaygate/) · [**Runnable Python experiment and raw protocols**](https://github.com/Vedant2100/role-work-forge-artifacts/tree/main/projects/prime-intellect-continual-memory) · [**Actual measured result JSON**](https://github.com/Vedant2100/role-work-forge-artifacts/blob/main/projects/prime-intellect-continual-memory/results_summary.json)

## The continual-learning question

When a system learns something new, should that change the model's weights, persist in a memory store, or be replayed during later training? How much of its *earlier* ability survives?

This question matters to continual-learning systems and self-improving agents, but there is a prerequisite before making claims about coding agents: run a controlled benchmark where retention and adaptation can actually be measured. I built **ReplayGate**, a separate experimental project, to do that.

**This is not the earlier SkillFalsifier demo.** ReplayGate trains a real online learner, performs sequential evaluation, and draws its interactive chart from actual run output.

## Real public data, not made-up tasks

The data comes directly from the [UCI Optical Recognition of Handwritten Digits dataset](https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits), provided by \`sklearn.datasets.load_digits()\`. It has **1,797 real handwritten digit images**, each represented by 64 pixel intensities.

I split the dataset into training and untouched test examples using a stratified 75/25 split separately for three fixed random seeds (7, 13, 29). Each model encounters five tasks in sequence: digits 0–1, 2–3, 4–5, 6–7 and finally 8–9.

The experiment uses **no handcrafted examples, mock benchmark records, or invented results**.

## Three ways to retain experience

**Weights only.** A 10-class logistic SGD classifier updates only on the current stage's two digit classes. There is no access to old examples when learning new classes.

**Reservoir replay.** The same classifier receives the same **120 parameter-update minibatches per stage**; half of each batch can be drawn from a uniformly sampled memory of at most **160 previous real training examples**. It still updates weights, but it revisits earlier experience.

**Exemplar memory.** Instead of updating model weights, a simple distance-weighted 3-nearest-neighbor classifier answers using at most **160 real examples** retained by the same online reservoir process. This measures the very different choice of making memory, rather than parameter updating, the primary mechanism.

All three methods are tested on the same held-out split for each seed. The 3-NN approach is **not inference-compute matched** to SGD.

## Results from the executed experiment

I ran the complete five-task sequence for **three seeds**, then measured accuracy on test examples from all tasks encountered so far, on the very first task, and on the newest task.

| Method | Final accuracy across all 10 digits | First task retained (0–1) | Newest task learned (8–9) |
| --- | ---: | ---: | ---: |
| Weights only | **18.96%** | 0.00% | 96.97% |
| Reservoir replay | **91.33%** | 81.32% | 94.70% |
| Exemplar memory | **92.96%** | 99.27% | 79.92% |

These are the **arithmetic means from the recorded three seeded runs**; see [the result file](https://github.com/Vedant2100/role-work-forge-artifacts/blob/main/projects/prime-intellect-continual-memory/results_summary.json) for per-seed metrics and learning curves, or [run the Python benchmark](https://github.com/Vedant2100/role-work-forge-artifacts/blob/main/projects/prime-intellect-continual-memory/run.py) to regenerate full results.

The [interactive ReplayGate dashboard](/replaygate/) lets you inspect **three different measured metrics** across all five checkpoints. It does **not** generate artificial accuracy values or let a slider invent results.

## What the numbers do and don't mean

In this configuration, adapting weights only to new classes produces severe forgetting of old classes. Rehearsal trades some of the newest-task performance for retained ability. Retrieval-only example memory also retains older classes quite well, but does worse than trained classifiers on the final new classes. Choosing where experience lives changes the tradeoff.

This **does not establish** that memory beats weight updates in an LLM, that our strategy improves coding-agent resolution, or that a three-seed linear-classifier result should be deployed in production. This is a **small genuine benchmark** on real handwritten digits, with only one learning-rate and memory configuration.

A next step toward agent continual learning would evaluate real agent trajectories and regression gates, using fixed versions of the harness and tasks, measuring old-task retention, unseen transfer and any regressions before promoting an update. That next experiment is **not yet executed**, so I don't report fictional numbers for it.

A separate line of my research studies exactly which historical experiences to expose to coding agents: [coding-agent memory governance](/fleet-mem/).

## Reproduce

From [the project folder on GitHub](https://github.com/Vedant2100/role-work-forge-artifacts/tree/main/projects/prime-intellect-continual-memory), install NumPy and scikit-learn, then run:

\`\`\`bash
OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1 python run.py --output results.json
\`\`\`

The script loads the public data, trains each method for each seed, evaluates all five stages, and saves full run output. No API keys or model-hosted inference are required.

**[New deployed demo](/replaygate/)** · **[Source and reproducibility](https://github.com/Vedant2100/role-work-forge-artifacts/tree/main/projects/prime-intellect-continual-memory)** · **[Measured results](https://github.com/Vedant2100/role-work-forge-artifacts/blob/main/projects/prime-intellect-continual-memory/results_summary.json)**

*Independent learning experiment. Not affiliated with Prime Intellect or a claim about LLM-agent performance.*