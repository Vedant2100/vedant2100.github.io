---
layout: editorial
title: "Terminal DreamGym"
description: "A terminal-agent self-improvement harness that converts failures into practice tasks and tests skill transfer."
date: 2026-10-25
permalink: /blog/terminal-dreamgym/
tags: [agents, evaluation, self-improvement]
---

[Source](https://github.com/Vedant2100/terminal_dreamgym)

## The question

A terminal agent may fail because it skipped a traceback, changed the wrong file, or missed a regression. An instruction learned from that one failure can look useful while failing on the next task. Terminal DreamGym asks how to create targeted practice without confusing rehearsal with generalization.

## Approach

The harness captures a terminal-task failure, diagnoses the missing capability, creates a small practice repository, and proposes a reusable **SKILL.md**. A live model can propose full-file patches within a sandbox; real pytest results decide success. Candidates are subsequently checked on held-out and adversarial cases before promotion. The repository supports a local Ollama/Qwen backend and a Gemini path, and exposes commands for each stage of the loop.

## Evidence and results

The [repository](https://github.com/Vedant2100/terminal_dreamgym) includes a recorded live-model run, reproduction instructions, and unit tests. A transfer improvement over a comparable baseline has not yet been established.

## Limitations

Practice worlds are deliberately narrower than real software-maintenance tasks. A locally passing test is not equivalent to reliable behavior across unseen repositories. More diverse testbeds and independent repetitions are needed to evaluate transfer.

[← Back to all projects](/projects/)
