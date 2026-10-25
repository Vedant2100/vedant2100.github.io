---
layout: editorial
title: "Hybrid movie recommendation system"
description: "A collaborative/content-based movie recommender with PyTorch autoencoders."
date: 2026-10-25
permalink: /blog/movie-recommendation-system/
tags: [recommenders, archive]
---

## The question

Collaborative filtering can learn from user–item interactions, while content features help represent items and preferences in a different way. Hybrid recommenders combine these signals but need careful offline evaluation.

## Approach

For an IIT Bombay project under Professor Abir De, I implemented a hybrid recommendation approach combining **collaborative and content-based filtering** with **PyTorch deep autoencoders**. I engineered user–movie features and tuned multilayer-network configurations using prediction error.

## Evidence and results

The historical CV describes RMSE-based optimization, but gives no verified held-out score or public dataset split. This archive note intentionally avoids creating a quantitative result that is not documented.

## Limitations

Lower RMSE alone does not demonstrate useful recommendation rankings, diversity, or cold-start quality. Reproducing the project would require source, data provenance, and consistent train/test partitioning.

[← Back to all projects](/projects/)
