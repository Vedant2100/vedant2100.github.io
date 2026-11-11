---
layout: editorial
title: "Who Gets to Remember? Governing Shared Memory in Coding-Agent Fleets"
description: "A working study of which past coding experiences should enter shared memory and when later agents should see them."
date: 2026-10-25
permalink: /blog/fleet-memory-governance/
tags: [agents, memory, research]
---

[Experiment](/fleet-mem/) · [Source](https://github.com/Vedant2100/sharedmemgov)

## The question

A coding agent can complete a task and leave behind a record of what worked. In a fleet, other agents might reuse that experience. But the decision to store an experience and the decision to show it to a later agent are different: keeping everything accumulates noise, while retrieving indiscriminately can distract or mislead the worker.

## Approach

I framed memory governance as two decisions: **SHARE / DO_NOT_SHARE** at the source task, then **EXPOSE / WITHHOLD** when another task arrives. The study separates memory extraction from admission and recipient-facing retrieval, and emphasizes controlling what information was available at source time. The [working research note](/fleet-mem/) documents the motivation, early failed setups, evaluation controls, and current exploratory results.

## Evidence and results

The [experiment note](/fleet-mem/) records the evaluation controls, observed failure modes, and pending comparisons. Results so far do not establish a task-resolution improvement from the memory-governance policies.

## Limitations

Cross-task usefulness depends on task relationships, worker model, repository state, memory quality, and randomness. A positive retrieval example is not evidence of a population-wide gain. Subsequent work needs repeated trials, held-out tasks, and careful leakage checks. For the broader literature, see my [annotated citation map](/fleet-mem/lineage/).

[← Back to all projects](/projects/)
