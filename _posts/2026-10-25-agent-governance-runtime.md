---
layout: editorial
title: "Evaluating agent governance at runtime"
description: "Work on prompt-injection controls, high-stakes tool use, detector evaluation, and agent observability at CompFly AI."
date: 2026-10-25
permalink: /blog/agent-governance-runtime/
tags: [safety, agents, evaluation]
---

[**View source or reference**](https://compfly.ai/resources/blog/agentdojo)

## The question

A text classifier's detection score is not the same as an agent's safety outcome. For an agent that calls tools, security evaluation also depends on where instructions enter, what actions follow, and whether a control actually intervenes.

## Approach

During my CompFly AI research internship, I worked on reproducible benchmark harnesses for governance controls using AgentDojo-style prompt injection and ToolEmu-style high-stakes scenarios. I benchmarked lightweight transformer detectors using changes to windowing, chunking, heuristics, and parallel ensembles. I also extended OpenTelemetry tracing over agent turns, LLM inference, tool calls, handoffs, and token/cost accounting.

## Evidence and results

The [CompFly technical article](https://compfly.ai/resources/blog/agentdojo), **Evaluating Prompt-Injection Controls Beyond Detection**, is the externally hosted write-up linked here so it can be discovered from the portfolio archive. The page you are reading is my short project overview, not a republication of company material.

## Limitations

Detector performance alone cannot establish end-to-end prevention of unsafe actions. Generalization under novel prompts, tool behavior, and deployment conditions requires separate empirical validation.

[← Back to all projects](/projects/)
