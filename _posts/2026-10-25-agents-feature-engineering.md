---
layout: editorial
title: "Agents for feature engineering and analytics"
description: "An agent pipeline for domain-aware feature suggestions, SQL/Python generation, and analytics workflows."
date: 2026-10-25
permalink: /blog/agents-feature-engineering/
tags: [agents, data-science, software-engineering]
---

## The question

Turning a natural-language analytics request into a useful ML feature is more demanding than generating code. A feature must make sense in the domain, be computable from available data, and show value under evaluation rather than merely appearing plausible.

## Approach

At Finarb AI I built an orchestrated workflow in which LLM agents interpreted a use case, looked for relevant domain factors, proposed features, generated candidate transformations, and tested their impact on model performance. Related work supported natural-language cross-database queries, SQL/Python generation, and KPI dashboards. Guardrails, execution checks, and failure handling were central parts of the pipeline.

## Evidence and results

My longer [engineering account](/best-work/) describes ownership and the validation challenge of non-deterministic LLM outputs. Client datasets, production metrics, and code are not public, so I avoid inventing standalone performance numbers for this system.

## Limitations

Generated features can introduce leakage or spurious correlations. Tool correctness and SQL validity are different from statistical usefulness; reliable deployments require held-out validation and human review of domain assumptions.

[← Back to all projects](/projects/)
