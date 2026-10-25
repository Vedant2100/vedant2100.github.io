---
layout: editorial
title: "Safety evaluation under an attack-family shift"
description: "A small public-benchmark test of prompt-injection classifiers with attack families excluded from training."
date: 2026-10-25
permalink: /blog/trajectory-safety-eval/
tags: [safety, evaluation, prompt-injection]
---

[**Open the experiment or artifact**](/trajectory-safety-eval/)

## The question

A strong in-distribution classifier score can hide missing attack coverage. I wanted a transparent comparison between a normal holdout and a test where entire attack categories were unseen during training.

## Approach

I trained word-level and character-level TF-IDF logistic-regression classifiers on a 303-example public prompt-injection dataset, with a deterministic split. In the shifted condition, encoding bypass and delimiter injection categories were withheld from training. The [interactive audit](/trajectory-safety-eval/) displays the measured counts, not generated scores.

## Evidence and results

On the ordinary holdout, the word-level classifier found **46/47** attack examples (**97.9% recall**). On the two held-out attack families, the audit reports **95.6% recall** for the word model and **97.8%** for the character model. The exact denominators, control reuse, and methodology are stated in the [audit page](/trajectory-safety-eval/).

## Limitations

The dataset is tiny and curated, benign controls are reused across comparisons, and no live agent attacks were executed. These scores should not be presented as production protection rates.

[← Back to all projects](/projects/)
