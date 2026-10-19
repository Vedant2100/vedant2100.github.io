# Adversarial audit of the coding-agent memory lineage

**As of October 18, 2026 (US Pacific).** This is a curated citation network, **not** a systematic claim about all papers in the field and not a diagram of algorithmic inheritance. A directed edge means the newer paper explicitly cites the older paper in its references. The original edge ledger is retained and now includes added prior works; `citation_edges_audited.csv` provides an audit trail per edge.

## Verdict

**Original version was materially incomplete.** The most consequential omission was **Agent KB (2025)**, which uses shared experience and a disagreement gate, evaluates SWE-bench and is **explicitly cited and experimentally compared against in Memory Transfer Learning**. That makes it a direct empirical predecessor. The original also missed two memory-representation predecessors that Memory Transfer Learning explicitly cites: **Agent Workflow Memory (ICML 2025)** and **Synapse (ICLR 2024)**. The revised graph adds these three nodes and four citation-verified edges.

**Metadata fixes:** The original truncated the formal titles of **Jev-Mem** and **Memory-R1**. The revised node titles use the published/arXiv exact titles. Conference status verified against publisher pages for Memory-R1 (ACL 2026), Learning to Share (ICML 2026), AWM (ICML 2025), Synapse (ICLR 2024), CTIM-Rover (REALM 2025), Mem0 (ECAI 2025), ExpeL (AAAI 2024), with author acceptance for Memory Transfer Learning (EMNLP 2026 Main) and Agent Memory Distillation (EMNLP 2026 Findings). Other 2026 nodes remain labeled preprint unless publication is independently demonstrated.

## Correct use: which works substantiate which FleetMem claim?

| Component of our question | Highest-value works | What they establish | Cannot claim |
|---|---|---|---|
| Cross-task coding reuse | CTIM-Rover (REALM'25); SWE-Exp; ReasoningBank (ICLR'26); Memory Transfer Learning (EMNLP'26) | Past coding experiences can be stored/retrieved, but noise and negative transfer matter | Simply retrieving similar text predicts task benefit |
| Shared cross-agent memory / protection | **Agent KB**; Learning to Share (ICML'26); SEDM | Shared memory, gates and selective admission are known concepts | Same mechanism already validated for paired, pre-execution coding-task effects |
| Outcome-grounded memory training | **MemOp**; **CODESKILL** | Agent execution results can train memory construction or skill maintenance | These train an identical per-candidate recipient EXPOSE/WITHHOLD classifier |
| Learned retrieval abstention | **Learning When to Remember**; SEDM; Jev-Mem as different control strategy | Gating can be learned or performed by a lightweight controller | Proxy/offline and conversational metrics demonstrate SWE repair improvement |
| Credible coding evaluation | **SWE-ContextBench**, **VibeMemBench**, SWE-bench | Executable outcomes and historical memories can be evaluated together | SWE-ContextBench automatically controls evolving-repo confounds; VibeMemBench positive-conditioned set estimates general prevalence of useful memories |

## Experiment-specific threats not resolved by this graph

1. **Selection bias**: VibeMemBench includes targets with known benefit in a reference solver. Keep a representative/random target cohort alongside positive controls; otherwise report effect conditional on benchmark construction.
2. **Environment confounding**: Ensure source experiences use only source-time information. Keep target repository commit, tools, test visibility and budget identical across memory-on/off. No evolved repository state masquerading as memory effects.
3. **Counterfactual uncertainty**: One paired execution is a *noisy contrast*, not proof of an intrinsic memory effect. Use repeated stochastic seeds where feasible and report effect distributions and uncertainty.
4. **Information leakage**: Do not train or prompt a governor with target gold patches, target test results, or outcomes from the same held-out evaluation task. Keep train/test split by repository (and source/target groups), not only by pairs.
5. **Treatment definition**: Memory representation, extraction, retrieval shortlist, injection location, and worker model should be held fixed when comparing governor policies; otherwise end-to-end memory pipeline gains cannot be assigned to the exposure decision.
6. **Construct validity**: Relevance, correctness, reliability, likely utility and eventual outcome improvement are different labels. Test them separately.
7. **Statistics**: FleetMem's current ~11 clean targets are suitable for preflight/sanity checks but not reliable evidence of generalization by a learned controller. Avoid presenting a learned gate without substantial training/evaluation data.
8. **Bibliography vs inheritance**: A citation edge doesn't show the cited algorithm was implemented or extended. For the five primary methodological ancestors read the methods/ablations, not just citation graph.

## Scope and audit limits

The graph was re-audited using current arXiv full-text and publisher/author venue evidence, plus the original bibliography-ledger references. The original 64 edges were retained after positive bibliography-title matching checks, and four verified citations were added. For paper versions with revised bibliographies, use the cited HTML version linked in the ledger and recheck publication-camera-ready variants before claiming exhaustive coverage. **This is not a formally exhaustive systematic literature review.** Papers released very recently are poorly indexed; absence of an arrow is not an absence-of-citation claim. The diagram no longer claims a unique methodological parent.

## Primary verification pages

- Agent KB: https://arxiv.org/html/2507.06229
- Memory Transfer Learning (explicit Agent KB comparison and memory-format citations): https://arxiv.org/html/2604.14004
- CTIM-Rover published workshop: https://aclanthology.org/2025.realm-1.30/
- Synapse ICLR 2024: https://proceedings.iclr.cc/paper_files/paper/2024/hash/52f050499cf82fa8efb588e263f6f3a7-Abstract-Conference.html
- Agent Workflow Memory ICML 2025: https://proceedings.mlr.press/v267/wang25bx.html
- Memory-R1 ACL 2026: https://aclanthology.org/2026.acl-long.583/
- Learning to Share ICML 2026: https://proceedings.mlr.press/v306/fioresi26a.html
- Memory Transfer Learning and Agent Memory Distillation acceptance: https://kangsankim07.github.io/
- VibeMemBench and its positive-conditioned selection: https://arxiv.org/abs/2609.23570
- Jev-Mem (LoCoMo evaluation): https://arxiv.org/abs/2609.23986

## Proposed reading sequence for FleetMem

1. **Agent KB** — direct overlooked predecessor on shared coding-related memory and disagreement gating.
2. **Memory Transfer Learning** — accepted coding-memory empirical comparator and citations to Agent KB.
3. **SEDM** — the closest two-governor admission/exposure conceptual implementation (in QA).
4. **MemOp + CODESKILL** — learn memory construction/skill maintenance from measured coding outcomes, not the same as exposure classification.
5. **Learning When to Remember + MemGuard** — recipient abstention controller and reliability-oriented SE memory, with different evaluation controls.
6. **SWE-ContextBench + VibeMemBench** — pick and audit the executable substrate before assessing governance.

The final research question should remain the one already agreed on; these sources are antecedents, not evidence for or against a result not yet experimentally tested.