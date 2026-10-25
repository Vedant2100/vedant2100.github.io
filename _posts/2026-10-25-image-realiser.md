---
layout: editorial
title: "Image-realiser: synthetic image forensics"
description: "A CLIP discriminator, convolutional purifier, and explainability tools for synthetic-image artifacts."
date: 2026-10-25
permalink: /blog/image-realiser/
tags: [vision, deepfakes, explainability]
---

[**View source or reference**](https://github.com/Vedant2100/image-realiser)

## The question

A synthetic-image detector can identify artifacts without revealing which image regions drove its decision. Conversely, an image-cleaning model might remove some artifacts while introducing others. Joint detection and visualization can help inspect both.

## Approach

Image-realiser pairs a **frozen CLIP ViT-B/32 visual backbone** and trainable discriminator head with a convolutional autoencoder purifier. The training code uses adversarial feedback, while an evaluation command generates four-way views: original image, purified image, pixel residual, and Grad-CAM explanation. The [repository](https://github.com/Vedant2100/image-realiser) includes model definitions, training, evaluation, and reporting utilities.

## Evidence and results

This is a published implementation and analysis workflow. The README documents a runnable path, but it does not establish cross-generator detection accuracy or robustness. I therefore avoid advertising an unsupported benchmark score.

## Limitations

A Grad-CAM heatmap is an aid to inspection, not proof that a detector relies on causally meaningful visual evidence. Transfer to novel generators requires a separate held-out evaluation.

[← Back to all projects](/projects/)
