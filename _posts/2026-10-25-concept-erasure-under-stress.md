---
layout: editorial
title: "Concept erasure under stress"
description: "A research analysis of concept erasure via SPEED, including rank saturation, collateral damage, and paraphrase evasion."
date: 2026-10-25
permalink: /blog/concept-erasure-under-stress/
tags: [vision, safety, diffusion]
---

[Source](https://vedant2100.github.io/concept-erasure-analysis/)

## The question

A text-to-image model may appear to forget a prohibited concept under one prompt while retaining related associations under reworded prompts. Erasure methods also risk changing unrelated concepts, making robustness and collateral damage joint concerns.

## Approach

In an EE243 advanced-computer-vision investigation, I examined the ESD concept-erasure method through the lens of SPEED. The analysis probed rank saturation, collateral changes to neighboring concepts, and whether paraphrases could still elicit erased ideas. The [standalone analysis](https://vedant2100.github.io/concept-erasure-analysis/) is the primary artifact.

## Evidence and results

The [technical report](https://vedant2100.github.io/concept-erasure-analysis/) contains the experimental setup and visual examples.

## Limitations

Prompt-level observations do not establish complete removal of a concept from learned representations. Conclusions depend on prompts, seeds, model version, evaluator, and how semantic similarity is measured.

[← Back to all projects](/projects/)
