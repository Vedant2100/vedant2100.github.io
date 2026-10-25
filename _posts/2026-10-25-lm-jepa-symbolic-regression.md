---
layout: editorial
title: "LM-JEPA for symbolic regression"
description: "A screening prototype for structured mathematical expression generation using a reduced-size LM-JEPA."
date: 2026-10-25
permalink: /blog/lm-jepa-symbolic-regression/
tags: [scientific-ml, representation-learning, symbolic-regression]
---

[**View source or reference**](https://github.com/Vedant2100/symreg)

## The question

Generating symbolic expressions requires more than predicting plausible tokens: operators have fixed arity, formulas must parse, and the representation needs to avoid a vocabulary that explodes with constants and variables.

## Approach

For an ML4SCI GSoC screening task, I converted Feynman equations into **strict binary prefix notation** using SymPy's syntax tree. Associative expressions were broken into binary nodes; a compact vocabulary of roughly **40 tokens** made arity explicit. I explored a reduced-size LM-JEPA representation and causal fine-tuning on **100 benchmark equations**.

## Evidence and results

The [repository README](https://github.com/Vedant2100/symreg) reports pretraining latent loss around **0.015**, while causal fine-tuning loss plateaued near **3.2**. These are training objectives, not a measured symbolic-recovery success rate.

## Limitations

A grammar-respecting decoder may still generate mathematically wrong expressions. The small benchmark and loss plateau make this a screening prototype rather than a validated scientific-discovery model.

[← Back to all projects](/projects/)
