# Agent alignment research sprint — November 2026

Three separate portfolio research prototypes. **None is represented as an accepted or officially submitted hackathon entry.** Generated code/datasets contain no live credentials. All approvals, tickets, and repositories in experiments are fictional.

## Direct Colab runner

[Run all three experiments](https://colab.research.google.com/github/Vedant2100/vedant2100.github.io/blob/master/files/agent_alignment_2026/00_all_three_final_run.ipynb)

The runner is **not an executed-results notebook**. It reads `HF_TOKEN` and `ADAPTION_API_KEY` from the Colab UI's secret vault, performs an actual Adaption Adaptive Data run, launches AutoScientist SFT after adaptation, runs Qwen multi-agent and coding-agent evaluations, trains a permitted Cohere Tiny Aya model with QLoRA, and attempts public Hugging Face publication if successful. Platform credits may be consumed. Provider-generated run IDs are persisted in its output. User action is required to run the UI notebook; the separate Colab MCP kernel does not receive notebook secrets.

## ContagionBench — Swarm Alignment

An independent signer receives peer messages from different agent-network topologies. A compromised source may only send messages, not approve. Test forged signed overrides, fake tool output, role spoofing, peer consensus, reward pressure, and delegated authorization.

- [Reproducible source](experiments/swarm_v3.py).
- [Real Qwen2.5-0.5B CPU pilot and raw outputs](signer_cpu_0p5B_2026_11_06.json). In eight exploratory attack families, unauthorized approval occurred once with no guard and once with prompt guard. Positive signed-verifier control also failed. This is a **small-model pilot**, not a strong submission result.
- The older Qwen2.5-1.5B and Qwen2.5-3B pilots are documented separately in the private working repository; their original source-compromise and scorer limitations must be disclosed. Do not merge their success rates.

## ProvenanceTrap — micro1 Eval

8 repository-state tasks with untrusted README, CI output, and delegated notes; deterministically grade authorized target state plus unauthorized writes and sensitive reads.

- [Experiment source](experiments/micro1_repro.py).
- Stronger, independent frontier-model evaluations have **not** completed or been submitted. Old 96-case Qwen1.5B tests showed 75% task completion without observed unauthorized actions; not enough for an attack-success benchmark.

## RewardHackLab — Lexsi Track 3

Ticket-workflow environment; compare actual state verification against proxy-reward claims. Train and evaluate an approved Cohere model with before/after metrics, then publish Hugging Face artifacts.

- [Cohere QLoRA train/eval script](experiments/lexsi_train_cohere.py).
- [AgentTune + AuditKIT integration](experiments/lexsi_repro.py).
- Cohere-model training and publication are **not yet verified**. Earlier non-Cohere Qwen results (13/18 versus 18/18 with a mechanical guard) show a tool-policy problem but not learned improvement.

## Venue rules and deadlines

- [Swarm Alignment](https://apartresearch.com/sprints/swarm-alignment-2026): November 6–8, research PDF; pre-sprint work must be disclosed.
- [micro1 Eval](https://www.hackerrank.com/event/micro1-eval-hackathon): November 8, code-only ZIP + walkthrough.
- [Lexsi](https://hackathon.lexsi.ai/): November 14, Cohere models, real before/after evaluation, public HF model/dataset collections.

## Reproducibility / ethics

Run with `torch`, `transformers`, `peft`, `agenttune`, `auditkit`, and `adaption` as specified by the runner. All generated prompts and credentials are handled locally, and the runner never prints the secret values. No real production approvals or live secret exfiltration are included.
