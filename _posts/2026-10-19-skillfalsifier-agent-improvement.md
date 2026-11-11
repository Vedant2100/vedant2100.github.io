---
layout: editorial
title: "SkillFalsifier: When an agent learns the wrong lesson"
description: "A reproducible gate that rejects self-generated agent skills unless they transfer beyond the training errors that inspired them."
date: 2026-10-19
permalink: /posts/skillfalsifier/
author_profile: false
tags:
  - agents
  - evaluations
  - safety
  - self-improvement
---

[**Try the deployed promotion-policy demo**](/skillfalsifier/) · [**Get the runnable Python code**](https://github.com/Vedant2100/skillfalsifier)

## The problem

An agent makes mistakes, studies its training failures, and proposes a new rule for future tasks. It gets more of those training examples right. Does that mean the rule deserves to become part of the agent's permanent playbook?

Not necessarily. A rule can explain visible failures while overfitting them. It might also break some tasks the original agent had already solved. I built **SkillFalsifier** to ask what evidence is needed before a self-generated skill is promoted.

## The testbed

The [GitHub project](https://github.com/Vedant2100/skillfalsifier) is a runnable Python CLI harness. An agent classifies hackathon-rules scenarios as *allowed*, *banned*, or *needs review*. Its predictions are scored by exact-match rules—not a free-form LLM judge.

It works with three data splits:

| Dataset | Purpose | Cases |
|---|---|---:|
| Training | Examples used to identify mistakes and generate candidate skills | 15 |
| Held-out | Unseen tests of whether the new rule transfers | 8 |
| Adversarial | Edge cases that punish rules that are too broad | 7 |

A real LLM proposes candidate skills from training failures. Each candidate is evaluated on the full set. Scores and promotion decisions are recorded in the CLI reports.

## Naive improvement versus falsification

The baseline **naive promotion** policy accepts a skill whenever it improves training accuracy.

The stricter **SkillFalsifier gate** requires three conditions: training accuracy must not decrease, accuracy on *held-out* examples must improve, and no previously correct *adversarial* case may become wrong.

That distinction is the project's central failure mode: a skill can increase the score on the examples that inspired it while reducing accuracy elsewhere. Training gains alone are not evidence of reliable improvement.

The [interactive demo](/skillfalsifier/) illustrates the exact deterministic promotion logic in the [source](https://github.com/Vedant2100/skillfalsifier/blob/main/skillfalsifier/promotion.py). The demo accepts hypothetical inputs; empirical scores can be reproduced with the repository datasets and model backends.

## Limits and why I care

This project is a small controlled testbed, not a universal theorem about agent self-improvement. The particularly conservative no-adversarial-regressions criterion may discard genuinely useful candidate skills. Larger datasets, multiple models, and repeated trials would be needed to evaluate production reliability.

What transfers is the *evaluation question*: if an agent learns a reusable skill, memory, or procedure from its own experience, how do we check that the update actually helps on work it hasn't seen?

A related research project on which coding-agent experiences deserve to persist is described in my [agent memory research note](/fleet-mem/).

**[Code](https://github.com/Vedant2100/skillfalsifier)** · **[Deployed decision demo](/skillfalsifier/)**
