---
layout: editorial
title: "Tracing the Research Lineage of Shared Memory in Coding Agents"
description: "A curated map of memory construction, sharing, retrieval, abstention, and evaluation research, with an explicit edge audit."
date: 2026-10-25
permalink: /blog/coding-agent-memory-lineage/
tags: [agents, memory, literature]
---

My [interactive citation lineage](/fleet-mem/lineage/) collects research relevant to shared experience in agent systems. I built it because a long list of papers is not enough to determine where an experiment sits: we need to distinguish shared-memory policies, learned retrieval, memory representation, and executable evaluation.

## Reading the map

The nodes are papers and the arrows represent **audited citations**, not a claim that one algorithm directly derives from another. An accompanying [audit report](/fleet-mem/lineage/AUDIT_REPORT.md) records revisions and the boundaries of the graph. For selected topics, it also identifies what a cited result does *not* establish.

## How it connects to my work

My [coding-agent memory project](/blog/fleet-memory-governance/) distinguishes the decision to retain a past experience from the decision to expose it to a later worker. The literature map organizes nearby ideas: admission gates, retrieval abstention, outcome-conditioned memories, provenance, and risk of negative transfer.

## Limits

The lineage is curated rather than systematic. Publication venues and citation edges can change with new versions; a visually prominent node is not a measure of empirical strength. For the full graph and references, use the [lineage explorer](/fleet-mem/lineage/) and its attached source artifacts.
