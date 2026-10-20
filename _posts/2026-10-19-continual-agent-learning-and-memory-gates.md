---
layout: single
title: "When should an agent keep what it learned?"
date: 2026-10-19
permalink: /posts/continual-agent-learning/
author_profile: true
tags:
  - continual-learning
  - agent-memory
  - evaluation
  - self-improvement
---

*Two independent experiments on a practical question: how do we tell a useful persistent update from something that only looks useful?*

**[Interactive evaluation demo](/skillfalsifier/)** · **[Runnable SkillFalsifier code](https://github.com/Vedant2100/skillfalsifier)** · **[Coding-agent memory research](/fleet-mem/)**

## The question

An agent finishes a task and learns something: a debugging trick, a rule about a tool, or a shortcut through a workflow. We could store it in memory, add it to a shared playbook, use it as new training data, or discard it. Which choice makes the *next* agent better, without breaking something that already worked?

I have been exploring that question from two directions: sharing historical experience between coding agents, and evaluating new skills generated from an agent's past errors.

## 1. Does sharing more memory help a coding agent?

My [coding-agent memory research](/fleet-mem/) investigates two different decisions:

- **Promotion:** which past experiences deserve to become shared memory?
- **Exposure:** which saved memories should be shown to a later agent facing a new task?

On a clean 11-target development set from SWE-ContextBench, earlier same-repository experiences served as candidate memories. The memory conditions we evaluated **did not improve full-task resolution over the no-memory baseline**.

This is a negative result, not a proof that memory cannot work. An earlier experience can look relevant and still be ignored, misapplied, or distracting. A memory relevance metric is not a substitute for running the downstream agent.

The [public summary](https://github.com/Vedant2100/coding-agent-mem) describes the study; the full task harness and benchmark artifacts are not currently available in that repository, so I do not claim the public summary is an independently reproducible experiment.

## 2. When should an agent promote a self-generated skill?

In [SkillFalsifier](https://github.com/Vedant2100/skillfalsifier), an agent learns from failures in a small rules-adjudication task. A model proposes candidate skills and the harness checks each candidate on training examples, held-out cases, and adversarial edge cases.

The project compares:

- **Naive promotion:** accept any skill that improves training accuracy.
- **Falsification gate:** require no training regression, a positive held-out improvement, and no newly incorrect adversarial examples.

The underlying Python source implements those decisions exactly. You can [try the deployed policy explorer](/skillfalsifier/) to change the three metrics and see the difference. **The sliders are hypothetical inputs, not measured benchmark outcomes.** To reproduce measurements, run the [CLI project](https://github.com/Vedant2100/skillfalsifier).

## What this suggests for continual learning

For agents that learn from a continuing stream of work, I would separate three questions rather than call all of them “memory quality”:

1. **Source quality:** did we extract a valid experience or learning signal?
2. **Retention and exposure:** did we store the right information, and present it only when it was likely to help?
3. **Behavioral effect:** when tested on new tasks *and old ones*, did the update improve completion without unacceptable regressions?

Those questions matter whether an update lives in model weights, retrieval memory, harness instructions, or a reusable skill. The system should also preserve the ability to inspect failures and roll back a bad update.

This is an **evaluation design direction**, not a result that one update mechanism is better than another. A serious next experiment would compare memory/harness updates against model-based post-training over a changing task stream, with retention, transfer, forgetting, and cost measured separately.

## Artifacts

- [Run the SkillFalsifier code](https://github.com/Vedant2100/skillfalsifier) — small reproducible CLI with a model-backed skill generator
- [Try the live promotion-policy demo](/skillfalsifier/) — interactive, deterministic visualization of the project's policy logic
- [Read the SWE-ContextBench memory study](/fleet-mem/) — exploratory negative-results research note
- [Coding-agent memory summary](https://github.com/Vedant2100/coding-agent-mem) — public research overview with full harness not yet released

*Independent research, not affiliated with any employer.*
