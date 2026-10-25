---
layout: editorial
title: "LLM reasoning strategies in MiniGrid navigation"
description: "Comparison of Reactive, ReAct, Chain-of-Thought, Tree-of-Thought, and Buffer-of-Thought planning."
date: 2026-10-25
permalink: /blog/minigrid-llm-reasoning/
tags: [agents, reasoning, evaluation]
---

[**View source or reference**](https://github.com/Vedant2100/w26/tree/main/CS_228)

## The question

An LLM acting in a grid world must translate observations into safe actions. Longer reasoning traces might improve planning, but also cost tokens and can fail in ways that shorter policies do not.

## Approach

In a collaborative CS228 project, we evaluated five prompting and planning strategies—Reactive, ReAct, Chain-of-Thought, Tree-of-Thought, and Buffer-of-Thought—using **Qwen2.5-7B-Instruct**. We built a deterministic Python evaluation pipeline across MiniGrid navigation tasks, recording success, exploration steps, and token use over **20 episodes per environment**. The Buffer-of-Thought variant used reusable navigation templates, structured outputs, and checks for unsafe forward actions.

## Evidence and results

The study reported up to **55% success** on LavaGapS6 and **20%** on LavaCrossingS9N2 in the evaluated settings. The [project folder](https://github.com/Vedant2100/w26/tree/main/CS_228) holds the implementation and results; these are task-specific observations, not a general ranking of reasoning methods.

## Limitations

Conclusions are bounded by the model, environments, prompting protocol, and small evaluation budgets. Better success in one grid does not imply better real-world planning.

[← Back to all projects](/projects/)
