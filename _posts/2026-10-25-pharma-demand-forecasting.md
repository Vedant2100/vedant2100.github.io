---
layout: editorial
title: "Pharmaceutical demand forecasting"
description: "Forecasting and deployment pipelines for pharmaceutical supply-chain demand at Finarb AI."
date: 2026-10-25
permalink: /blog/pharma-demand-forecasting/
tags: [forecasting, data-science, production-ml]
---

## The question

Supply-chain forecasts must translate noisy operational history into useful planning quantities. Trend changes, seasonality, intermittent demand, and the relative costs of over- and under-forecasting complicate evaluation.

## Approach

At Finarb AI, I compared classical time-series approaches (SARIMA, VAR, and Prophet) with LSTM and Temporal Convolutional Network models. My pipeline incorporated preprocessing, feature engineering, selection under custom metrics, diagnostics, and Docker-based deployment across supply-chain nodes.

## Evidence and results

The work reported a **90% reduction in mean absolute percentage error** relative to existing moving-average and exponential-smoothing baselines in its evaluated setting. The [partner announcement](https://www.businesswire.com/news/home/20240205191469/en/Golden-State-Medical-Supply-GSMS-selects-Finarb-Analytics-Consulting-as-its-trusted-Partner-for-AI-enabled-Demand-Forecasting-for-their-generics-business) provides public project context; the original company dataset and evaluation artifacts are not publicly reproduced here.

## Limitations

This is a retrospective engineering account, not an independently rerunnable benchmark. The relative error reduction should not be generalized to other supply chains without knowing the data splits, horizons, aggregation, and baseline definitions.

[← Back to all projects](/projects/)
