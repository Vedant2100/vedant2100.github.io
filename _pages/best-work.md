---
permalink: /best-work/
title: "My Best Work to Date"
author_profile: true
---

So far, my proudest achievement has been building and shipping an LLM-based agent system that automated feature engineering for real-world datasets, end to end.

I designed and implemented an orchestrated workflow where multiple AI agents could analyze natural-language machine learning use cases, research external sources for relevant domain factors and strategies specific to the usecase, propose and generate features, and then assess their impact on model performance. This system was built as a submodule of a larger AutoML project Finarb was developing.

I implemented the entire pipeline, from prompt design and guardrails to execution logic, error handling, and evaluation. Because the system relied on LLMs, it was inherently non-deterministic, which meant testing and validation were significantly more challenging than in a typical software engineering project. Making the system reliable enough to be used in practice required careful design choices around constraints, verification, and failure modes as well as extensive testing.
