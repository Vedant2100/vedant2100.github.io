---
layout: single
permalink: /fleet-mem/
title: ""
author_profile: false
comments: false
share: false
related: false
sitemap: true
---

<style>
.fleet-blog { max-width: 780px; margin: 0 auto; line-height: 1.72; }
.fleet-blog * { box-sizing: border-box; }
.fleet-blog .kicker { margin: 0 0 .8rem; font-size: .78rem; font-weight: 700; letter-spacing: .11em; text-transform: uppercase; }
.fleet-blog h1 { margin: 0 0 1rem; font-size: clamp(2.4rem, 7vw, 4.9rem); line-height: .98; letter-spacing: -.045em; }
.fleet-blog .deck { max-width: 690px; margin: 0 0 1.2rem; font-size: 1.28rem; line-height: 1.48; }
.fleet-blog .byline { margin: 0 0 3.2rem; font-size: .92rem; opacity: .68; }
.fleet-blog h2 { margin-top: 4.2rem; padding-top: 1.7rem; border-top: 1px solid currentColor; font-size: 1.8rem; letter-spacing: -.02em; }
.fleet-blog h3 { margin-top: 2.2rem; font-size: 1.2rem; }
.fleet-blog p, .fleet-blog li { font-size: 1.02rem; }
.fleet-blog .lede { font-size: 1.18rem; line-height: 1.62; }
.fleet-blog .standfirst { margin: 2.4rem 0; padding-left: 1.15rem; border-left: 3px solid currentColor; font-size: 1.14rem; }
.fleet-blog .quick { margin: 2.5rem 0 3rem; padding: 1.4rem 0; border-top: 1px solid currentColor; border-bottom: 1px solid currentColor; }
.fleet-blog .quick p { margin: .45rem 0; }
.fleet-blog .metric-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin: 2rem 0; }
.fleet-blog .metric { padding-top: .8rem; border-top: 2px solid currentColor; }
.fleet-blog .metric strong { display: block; font-size: 2rem; line-height: 1.05; letter-spacing: -.04em; }
.fleet-blog .metric span { display: block; margin-top: .35rem; font-size: .84rem; line-height: 1.35; opacity: .72; }
.fleet-blog figure { margin: 2.6rem 0; }
.fleet-blog figure svg { display: block; width: 100%; height: auto; }
.fleet-blog figcaption { margin-top: .8rem; font-size: .86rem; line-height: 1.45; opacity: .7; }
.fleet-blog .note { margin: 2rem 0; padding: 1.2rem 0 1.2rem 1.2rem; border-left: 2px solid currentColor; }
.fleet-blog .status { font-weight: 700; }
.fleet-blog table { width: 100%; margin: 1.8rem 0; border-collapse: collapse; font-size: .91rem; }
.fleet-blog th, .fleet-blog td { padding: .7rem .55rem; border-bottom: 1px solid currentColor; vertical-align: top; text-align: left; }
.fleet-blog th { border-bottom-width: 2px; }
.fleet-blog .small { font-size: .88rem; opacity: .74; }
.fleet-blog .sources li { margin-bottom: .55rem; }
.fleet-blog .foot { margin-top: 4rem; padding-top: 1.4rem; border-top: 1px solid currentColor; font-size: .88rem; opacity: .72; }
@media (max-width: 650px) {
  .fleet-blog .metric-row { grid-template-columns: 1fr; }
  .fleet-blog h1 { font-size: 2.8rem; }
  .fleet-blog .deck { font-size: 1.12rem; }
  .fleet-blog table { font-size: .8rem; }
  .fleet-blog th, .fleet-blog td { padding: .55rem .35rem; }
}
</style>

<article class="fleet-blog">

<p class="kicker">Research note · October 2026 · Work in progress</p>
<h1>Who gets to remember?</h1>
<p class="deck">A controlled study of when one coding agent’s experience should become shared organizational memory for future coding agents—and when a later agent should be shown it.</p>
<p class="byline">Vedant Borkute · Shared memory governance for coding-agent fleets</p>

<p class="lede">Imagine a team of coding agents maintaining the same repository over months. One agent discovers a testing trick. Another learns that a “general” fix actually breaks a particular subsystem. A third encounters an environment quirk. The tempting move is to save everything and give all of it to future agents.</p>

<p class="standfirst"><strong>The research question is not whether agents can have memory.</strong> It is whether experience produced by one worker deserves to cross an organizational boundary into shared memory, and whether a later worker should be exposed to it.</p>

<div class="quick">
  <p><strong>In 60 seconds:</strong></p>
  <p>1. A coding agent finishes a real software task and produces candidate lessons.</p>
  <p>2. A <strong>write policy</strong> decides which lessons become shared fleet memory—before future tasks are known.</p>
  <p>3. A later agent receives a new task. A <strong>read policy</strong> decides which shared memories it sees.</p>
  <p>4. We score the consequence with executable repository tests, not an LLM preference score.</p>
</div>

<figure aria-labelledby="pipeline-caption">
<svg viewBox="0 0 940 300" role="img" aria-label="Fleet memory governance pipeline">
  <g fill="none" stroke="currentColor" stroke-width="2">
    <rect x="20" y="100" width="150" height="70" rx="6"/>
    <rect x="215" y="100" width="150" height="70" rx="6"/>
    <rect x="410" y="100" width="150" height="70" rx="6"/>
    <rect x="605" y="100" width="150" height="70" rx="6"/>
    <rect x="800" y="100" width="120" height="70" rx="6"/>
    <path d="M170 135H215 M365 135H410 M560 135H605 M755 135H800"/>
    <path d="M204 128l11 7-11 7 M399 128l11 7-11 7 M594 128l11 7-11 7 M789 128l11 7-11 7"/>
  </g>
  <g fill="currentColor" text-anchor="middle">
    <text x="95" y="128" font-size="17">Agent A</text>
    <text x="95" y="151" font-size="14">does a task</text>
    <text x="290" y="128" font-size="17">Write gate</text>
    <text x="290" y="151" font-size="14">share / don’t share</text>
    <text x="485" y="128" font-size="17">Fleet memory</text>
    <text x="485" y="151" font-size="14">many past lessons</text>
    <text x="680" y="128" font-size="17">Read gate</text>
    <text x="680" y="151" font-size="14">expose / withhold</text>
    <text x="860" y="128" font-size="17">Agent B</text>
    <text x="860" y="151" font-size="14">later task</text>
    <text x="470" y="235" font-size="17">↓ executable tests decide whether the intervention helped or hurt ↓</text>
  </g>
</svg>
<figcaption id="pipeline-caption">The benchmark separates two decisions that are usually entangled: what enters shared memory, and what a particular future worker is allowed to see.</figcaption>
</figure>

<h2>Why this needs a benchmark before it needs a clever governor</h2>

<p>A memory governor is only interesting if it has a real choice to make. If a target task is handed exactly one known-relevant earlier experience, there is almost no governance problem. The system has already been told what matters.</p>

<p>In a real organization, the history is messier. A future agent may face dozens of memories from earlier tasks: some useful, some irrelevant, some too broad, some redundant, some based on failed attempts, some stale, and some already encoded in the current codebase.</p>

<figure aria-labelledby="pool-caption">
<svg viewBox="0 0 940 360" role="img" aria-label="One memory versus a realistic candidate pool">
  <g fill="none" stroke="currentColor" stroke-width="2">
    <rect x="30" y="55" width="360" height="245" rx="8"/>
    <rect x="550" y="55" width="360" height="245" rx="8"/>
    <rect x="130" y="145" width="160" height="64" rx="6"/>
    <rect x="595" y="105" width="100" height="48" rx="5"/>
    <rect x="720" y="105" width="100" height="48" rx="5"/>
    <rect x="657" y="175" width="100" height="48" rx="5"/>
    <rect x="595" y="245" width="100" height="48" rx="5"/>
    <rect x="720" y="245" width="100" height="48" rx="5"/>
  </g>
  <g fill="currentColor" text-anchor="middle">
    <text x="210" y="88" font-size="18">Pairwise context reuse</text>
    <text x="210" y="170" font-size="16">one known source</text>
    <text x="210" y="191" font-size="14">already chosen for you</text>
    <text x="730" y="88" font-size="18">Fleet-memory governance</text>
    <text x="645" y="134" font-size="13">useful</text>
    <text x="770" y="134" font-size="13">similar</text>
    <text x="707" y="204" font-size="13">stale?</text>
    <text x="645" y="274" font-size="13">failed</text>
    <text x="770" y="274" font-size="13">redundant</text>
    <text x="470" y="334" font-size="16">The second setting creates an actual decision problem.</text>
  </g>
</svg>
<figcaption id="pool-caption">Multiple memories are not decoration. They are what make “governance” measurable rather than trivial selection of a single known source.</figcaption>
</figure>

<h3>A concrete example</h3>
<p>Suppose an earlier worker learns: <em>“Normalize paths before comparing them.”</em> A later path-related task might benefit. But the shared history may also contain:</p>
<ul>
  <li>“Do not normalize URLs in this subsystem.”</li>
  <li>“This bug was Windows-only.”</li>
  <li>“Normalization here broke symlink handling.”</li>
  <li>“Run test X before touching this module.”</li>
  <li>an unrelated but superficially similar serialization lesson.</li>
</ul>
<p>Now the question is no longer “can retrieval find a related document?” It is whether earlier experience should have been institutionalized at all, and whether this particular future task should see it.</p>

<h2>How we got here: one useful failure</h2>

<p>The project did not start with Fleet Mem. It started with the simpler idea that a fast controller could govern which lessons from coding agents become shared memory. Then the experiment drifted.</p>

<figure aria-labelledby="timeline-caption">
<svg viewBox="0 0 940 310" role="img" aria-label="Research trajectory from original idea to Fleet Mem">
  <g fill="none" stroke="currentColor" stroke-width="2">
    <path d="M85 150H855"/>
    <circle cx="120" cy="150" r="9" fill="currentColor"/>
    <circle cx="350" cy="150" r="9" fill="currentColor"/>
    <circle cx="585" cy="150" r="9" fill="currentColor"/>
    <circle cx="820" cy="150" r="9" fill="currentColor"/>
  </g>
  <g fill="currentColor" text-anchor="middle">
    <text x="120" y="72" font-size="17">Original idea</text>
    <text x="120" y="96" font-size="13">govern what gets shared</text>
    <text x="350" y="205" font-size="17">ChainSWE pivot</text>
    <text x="350" y="229" font-size="13">real sequence, weak memory choices</text>
    <text x="585" y="72" font-size="17">Diagnosis</text>
    <text x="585" y="96" font-size="13">benchmark did not create the decision</text>
    <text x="820" y="205" font-size="17">Fleet Mem</text>
    <text x="820" y="229" font-size="13">many prior experiences + hidden relation</text>
  </g>
</svg>
<figcaption id="timeline-caption">The correction was not “find a newer benchmark.” It was “make the benchmark expose the causal decision the paper actually cares about.”</figcaption>
</figure>

<h3>Why ChainSWE looked attractive</h3>
<p>ChainSWE gives genuine sequences of software-maintenance tasks. Repository state persists over time, so it looks like a realistic coding-agent fleet. That realism was attractive.</p>

<p>But the repository itself was already carrying much of the persistent information. Extra textual memory often had little unique work to do. In the clean 36-context study, the outcomes were roughly <strong>No Share 14/36, Share-All 12/36, Governed 12/36</strong>. The deeper problem was structural: only <strong>7 targets</strong> had multiple candidate memories, and the audit found few genuine conflict or supersession cases.</p>

<p class="note"><strong>That result did not show that governance fails.</strong> It showed that the experiment rarely gave the governor a meaningful decision.</p>

<h2>The redesign: Fleet Mem on top of SWE-ContextBench</h2>

<p>SWE-ContextBench is useful because it already contains real repository tasks, executable evaluation, prior experience tasks, later related tasks, and known source-to-target relationships. But we do not run it as published.</p>

<p>The key change is simple:</p>

<p class="standfirst"><strong>The benchmark’s known source→target relationship is hidden from the memory system.</strong> It becomes evaluation metadata, not the retrieval mechanism.</p>

<p>For a later task, we instead build a history from <strong>all eligible earlier tasks in the same repository</strong>. The target agent must operate in a realistic pool of prior experiences rather than being handed the answer about which experience matters.</p>

<h3>The benchmark protocol</h3>
<ol>
  <li><strong>Source workers act first.</strong> Each earlier coding task produces a trajectory and candidate lessons.</li>
  <li><strong>Extraction is fixed and high-recall.</strong> The extractor creates atomic candidate memories plus provenance; it must not quietly perform the governor’s filtering job.</li>
  <li><strong>Write decisions are source-global and target-blind.</strong> A memory is marked <strong>SHARE</strong> or <strong>DO NOT SHARE</strong> once, before any future target is known.</li>
  <li><strong>Later targets see a shared pool.</strong> A target-time read policy chooses which shared memories to <strong>EXPOSE</strong> or <strong>WITHHOLD</strong>.</li>
  <li><strong>The coding worker is fixed.</strong> Only the memory treatment changes.</li>
  <li><strong>Executable tests grade the result.</strong> We measure whether the memory intervention changed real software outcomes.</li>
</ol>

<p class="small">The primary write action is deliberately binary. With fresh workers, “keep local” and “reject” are experimentally indistinguishable because the original worker does not return. Likewise, the primary read action is expose/withhold rather than “advisory/rely,” which would change how the coding worker is prompted.</p>

<div class="metric-row" aria-label="Current benchmark construction status">
  <div class="metric"><strong>11</strong><span>clean development targets</span></div>
  <div class="metric"><strong>13–114</strong><span>earlier same-repository candidates per target</span></div>
  <div class="metric"><strong>0</strong><span>memory-treatment conclusions so far</span></div>
</div>

<p>The first structural gate therefore passed: the benchmark now contains nontrivial historical pools instead of singleton memories.</p>

<h2>Why we did not switch to a completely new benchmark</h2>

<p>We explored a second route in parallel: constructing a native organizational-memory benchmark from <strong>SWE-rebench V2</strong>. It has much richer repository histories and is probably the more natural long-term substrate.</p>

<p>But “many earlier tasks” is not the same as “known transferable experience.” The hard part is establishing which earlier work can genuinely help a later task without leaking the answer or cherry-picking pairs.</p>

<table>
<thead><tr><th>Substrate</th><th>What it gives us</th><th>Why it is / is not primary</th></tr></thead>
<tbody>
<tr><td><strong>ChainSWE</strong></td><td>Sequential maintenance with persistent repo state</td><td>Excellent realism, but too few meaningful memory-governance choices in our run.</td></tr>
<tr><td><strong>SWE-ContextBench + Fleet Mem</strong></td><td>Known useful relations, executable tasks, earlier same-repo history</td><td><strong>Primary now.</strong> Fastest path to a controlled causal experiment.</td></tr>
<tr><td><strong>SWE-rebench V2</strong></td><td>Large natural repository histories</td><td>Promising follow-up, but relation quality/chronology and end-to-end validation were not ready; only 1/48 pilot targets was fully validated.</td></tr>
<tr><td><strong>VibeMemBench</strong></td><td>Large historical trajectory pools with executable memory interventions</td><td>Strong read-memory benchmark; less direct for natural source-time organizational admission.</td></tr>
</tbody>
</table>

<p>So the current choice is intentionally conservative: use SWE-ContextBench as the executable substrate, but replace its pairwise “give the related source to the target” setup with a fleet-history overlay.</p>

<h2>What is actually new—and what is not</h2>

<p>We are <strong>not</strong> claiming that we invented memory, coding-agent memory, memory admission, or memory governance.</p>

<p>Recent work already occupies important pieces:</p>
<ul>
  <li><strong>SWE-ContextBench</strong> studies reuse of prior coding experience and shows that the right concise experience can help while mismatched experience can hurt.</li>
  <li><strong>VibeMemBench</strong> shows that useful historical experience can exist even when complete memory systems fail to turn that history into gains.</li>
  <li><strong>GateMem</strong> directly studies shared-memory governance in multi-principal settings, though not executable software maintenance.</li>
  <li><strong>MemGuard</strong> studies admission, stale/conflicting records, retrieval, and lifecycle governance for coding-agent memory. That rules out broad “first governance” claims.</li>
  <li><strong>Agent Memory Bench</strong> includes present/absent/superseded/contradictory coding-memory conditions, but evaluates retrieval over a pre-ingested corpus rather than source workers learning and promoting memories during the run.</li>
  <li><strong>Jev-Mem</strong> motivates a cheap System-One controller for bounded memory decisions, but its evaluation is not this cross-worker executable software setting.</li>
</ul>

<p>The narrower gap we are testing is the whole chain:</p>

<p class="standfirst">coding worker produces experience → target-blind source-time fleet admission → shared organizational pool evolves → later independent worker receives governed memory → target-time exposure → executable downstream outcome</p>

<p>That decomposition also lets us ask whether write governance and read governance solve different problems instead of bundling them into a single opaque “memory system.”</p>

<h2>The experiment we want to run</h2>

<table>
<thead><tr><th>Condition</th><th>What changes</th><th>What it tells us</th></tr></thead>
<tbody>
<tr><td><strong>No memory</strong></td><td>No past experience exposed</td><td>Baseline worker performance</td></tr>
<tr><td><strong>Share all</strong></td><td>All eligible memories shared; fixed read budget</td><td>Cost of indiscriminate organizational memory</td></tr>
<tr><td><strong>Size-matched random</strong></td><td>Randomly shares the same amount as the governor</td><td>Separates “better filtering” from merely “less context”</td></tr>
<tr><td><strong>Governed write</strong></td><td>Source-time share/do-not-share; fixed read</td><td>Isolates write governance</td></tr>
<tr><td><strong>Governed read</strong></td><td>Share all; target-time exposure gate</td><td>Isolates read governance</td></tr>
<tr><td><strong>Governed write + read</strong></td><td>Both gates active</td><td>Full lifecycle intervention</td></tr>
<tr><td><strong>Deliberative LLM governor</strong></td><td>Stronger reasoning controller with same decision schema</td><td>Quality/cost comparison</td></tr>
<tr><td><strong>Known-relevant memory</strong></td><td>Directly provides the benchmark’s known related experience</td><td>Checks whether useful memory can move the worker at all</td></tr>
</tbody>
</table>

<p>The lightweight controller of interest is a <strong>Jev/System-One-style governor</strong>: small bounded decisions rather than an expensive LLM repeatedly reasoning over the entire memory store. The scientific question is not “can Jev be used?” It is whether cheap decisions preserve enough of the benefit of a stronger governor to justify the systems tradeoff.</p>

<h2>Before the governor: prove that memory can matter</h2>

<p>This is the current stage. We deliberately have <strong>not</strong> launched the full memory comparison yet.</p>

<p>The original worker qualification rule required full resolution on 2 of 3 burned development tasks. GPT-6 Luna failed that gate, but the diagnosis was more informative than a binary score:</p>
<ul>
  <li>On a SymPy task, it fixed part of the required behavior but introduced or exposed a serious performance problem.</li>
  <li>On a Django task, it fixed the reported duplicate-column case and preserved the regression suite, but missed several required cases.</li>
</ul>

<p>That means the worker is not mechanically broken. It can understand tasks, edit code, submit patches, and get graded—it is simply incomplete. For a memory study, that may actually be useful: a near-perfect worker leaves little room for memory to help, while a totally broken worker cannot use memory at all.</p>

<figure aria-labelledby="gates-caption">
<svg viewBox="0 0 940 360" role="img" aria-label="Current experimental gates">
  <g fill="none" stroke="currentColor" stroke-width="2">
    <rect x="40" y="70" width="190" height="68" rx="6"/>
    <rect x="270" y="70" width="190" height="68" rx="6"/>
    <rect x="500" y="70" width="190" height="68" rx="6"/>
    <rect x="730" y="70" width="170" height="68" rx="6"/>
    <path d="M230 104H270 M460 104H500 M690 104H730"/>
    <path d="M259 97l11 7-11 7 M489 97l11 7-11 7 M719 97l11 7-11 7"/>
  </g>
  <g fill="currentColor" text-anchor="middle">
    <text x="135" y="98" font-size="16">Structure</text>
    <text x="135" y="120" font-size="14">PASS</text>
    <text x="365" y="98" font-size="16">Evaluator</text>
    <text x="365" y="120" font-size="14">PASS</text>
    <text x="595" y="98" font-size="16">Worker signal</text>
    <text x="595" y="120" font-size="14">CURRENT</text>
    <text x="815" y="98" font-size="16">Governor study</text>
    <text x="815" y="120" font-size="14">NOT RUN</text>
    <text x="470" y="214" font-size="18">No memory  ↔  known-relevant memory</text>
    <text x="470" y="244" font-size="14">Does giving the worker a useful past experience change executable outcomes?</text>
    <text x="470" y="303" font-size="16">If no → stop.   If yes → run the governance comparison.</text>
  </g>
</svg>
<figcaption id="gates-caption">The signal check is deliberately before the expensive governor study. If a known-relevant memory cannot move the worker, a sophisticated policy has nothing to recover.</figcaption>
</figure>

<h3>The immediate sequence</h3>
<ol>
  <li>Compare Luna and Sol on the same already-burned tasks to choose a worker without contaminating the main experiment.</li>
  <li>Freeze the worker.</li>
  <li>Run a paired <strong>no-memory vs known-relevant-memory</strong> signal check on burned targets.</li>
  <li>Only if memory changes outcomes on multiple targets, run the small governance pilot.</li>
  <li>Then freeze the clean experiment and scale the final comparison.</li>
</ol>

<p class="note"><strong>Important:</strong> no Jev-vs-Share-All result, no governed-vs-random result, and no main memory result exists yet. The project is still validating that the benchmark + worker combination exposes a real memory effect before spending compute on the headline comparison.</p>

<h2>What would count as an informative result?</h2>

<ul>
  <li><strong>Known-relevant memory does nothing:</strong> stop. The benchmark/worker pairing does not expose enough memory signal.</li>
  <li><strong>Share-All hurts but governance helps:</strong> evidence that organizational memory needs selectivity, not just storage.</li>
  <li><strong>Governed selection matches random selection:</strong> the gain may come from reducing context, not from intelligent governance.</li>
  <li><strong>Write governance helps but read governance does not:</strong> the important decision is institutionalization at source time.</li>
  <li><strong>Read governance helps but write governance does not:</strong> keeping broad history may be fine if target-time exposure is selective.</li>
  <li><strong>Jev approaches an LLM governor at much lower cost:</strong> evidence for a cheap System-One control layer.</li>
  <li><strong>Nothing beats no memory:</strong> still useful. It would show how hard it is for explicit textual organizational memory to add value beyond code, tests, and repository state.</li>
</ul>

<h2>The core lesson so far</h2>

<p>The biggest mistake in this project was treating benchmark realism as the same thing as benchmark fit. ChainSWE looked more like a real evolving repository, but that did not automatically create a meaningful memory-governance problem.</p>

<p>Fleet Mem is the correction: <strong>design the evaluation around the decision we want to identify.</strong> Give the system multiple plausible prior experiences. Keep future tasks hidden from source-time admission. Hold the coding worker fixed. Separate writing from reading. Compare against matched controls. Judge everything by executable outcomes.</p>

<p class="standfirst">The goal is not another memory database. It is to understand when local agent experience deserves to become organizational knowledge.</p>

<h2>References and adjacent work</h2>
<ul class="sources">
  <li><a href="https://arxiv.org/abs/2602.08316">SWE-ContextBench: A Benchmark for Context Learning in Coding</a></li>
  <li><a href="https://arxiv.org/abs/2609.23570">VibeMemBench: Evaluating Memory Systems for Coding Agents on Real Repository Coding Tasks</a></li>
  <li><a href="https://arxiv.org/abs/2606.18829">GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents</a></li>
  <li><a href="https://arxiv.org/abs/2608.21867">MemGuard</a></li>
  <li><a href="https://arxiv.org/pdf/2609.23986">Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents</a></li>
  <li><a href="https://github.com/GiulioDER/agent-memory-bench">Agent Memory Bench</a></li>
  <li><a href="https://proceedings.mlr.press/v306/badertdinov26a.html">SWE-rebench V2</a></li>
</ul>

<p class="foot">This is an active research note. The benchmark construction has passed its structural feasibility check; the main memory-governance treatments have not yet run. The page will be updated when the signal check and controlled comparisons are complete.</p>

</article>
