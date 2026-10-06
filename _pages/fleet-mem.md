---
layout: single
permalink: /fleet-mem/
title: ""
author_profile: false
comments: false
share: false
related: false
sitemap: true
classes: wide
---

<style>
#main { max-width: 1320px; }
#main .page { width: 100%; max-width: none; float: none; padding-right: 0; }
#main .page__inner-wrap, #main .page__content { width: 100%; max-width: none; }
.fleet-blog {
  --ink: currentColor;
  width: min(1180px, calc(100vw - 52px));
  max-width: none;
  margin: 0 auto;
  line-height: 1.66;
}
.fleet-blog * { box-sizing: border-box; }
.fleet-blog a { text-underline-offset: .16em; }
.fleet-blog .hero {
  display: grid;
  grid-template-columns: minmax(0, 1.55fr) minmax(300px, .7fr);
  gap: 4rem;
  align-items: end;
  margin: 1rem 0 4.5rem;
  padding-bottom: 2.2rem;
  border-bottom: 1px solid var(--ink);
}
.fleet-blog .kicker,
.fleet-blog .eyebrow {
  margin: 0 0 .8rem;
  font-size: .76rem;
  font-weight: 700;
  letter-spacing: .11em;
  text-transform: uppercase;
}
.fleet-blog h1 {
  margin: 0;
  max-width: 820px;
  font-size: clamp(3rem, 6.2vw, 6rem);
  line-height: .93;
  letter-spacing: -.055em;
}
.fleet-blog .deck {
  margin: 1.35rem 0 0;
  max-width: 790px;
  font-size: 1.28rem;
  line-height: 1.5;
}
.fleet-blog .hero-meta {
  padding-top: 1rem;
  border-top: 2px solid var(--ink);
}
.fleet-blog .hero-meta p {
  margin: .55rem 0;
  font-size: .9rem;
  line-height: 1.45;
}
.fleet-blog .reading {
  max-width: 760px;
  margin-left: auto;
  margin-right: auto;
}
.fleet-blog .lede { font-size: 1.17rem; line-height: 1.68; }
.fleet-blog .standfirst {
  margin: 2.5rem auto;
  max-width: 860px;
  padding: 1.35rem 0 1.35rem 1.35rem;
  border-left: 3px solid var(--ink);
  font-size: 1.16rem;
  line-height: 1.6;
}
.fleet-blog h2 {
  margin: 5rem 0 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--ink);
  font-size: clamp(1.65rem, 2.4vw, 2.25rem);
  line-height: 1.14;
  letter-spacing: -.025em;
}
.fleet-blog h3 {
  margin-top: 2.2rem;
  font-size: 1.18rem;
  line-height: 1.3;
}
.fleet-blog p, .fleet-blog li { font-size: 1rem; }
.fleet-blog .section-grid,
.fleet-blog .two-up,
.fleet-blog .three-up,
.fleet-blog .four-up {
  display: grid;
  gap: 1.3rem;
}
.fleet-blog .section-grid {
  grid-template-columns: minmax(0, 1.15fr) minmax(340px, .85fr);
  gap: 3.2rem;
  align-items: start;
}
.fleet-blog .two-up { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.fleet-blog .three-up { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.fleet-blog .four-up { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.fleet-blog .panel {
  padding: 1.1rem 0;
  border-top: 2px solid var(--ink);
}
.fleet-blog .panel h3 { margin: 0 0 .65rem; }
.fleet-blog .panel p { margin: .45rem 0; }
.fleet-blog .panel .big {
  display: block;
  margin-bottom: .35rem;
  font-size: 2rem;
  font-weight: 700;
  line-height: 1;
  letter-spacing: -.04em;
}
.fleet-blog .panel .small,
.fleet-blog .small { font-size: .84rem; line-height: 1.45; opacity: .72; }
.fleet-blog .quick {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 1rem;
  margin: 2.5rem 0 4rem;
}
.fleet-blog .quick > div {
  padding-top: .85rem;
  border-top: 2px solid var(--ink);
}
.fleet-blog .quick strong {
  display: block;
  margin-bottom: .35rem;
  font-size: .8rem;
  text-transform: uppercase;
  letter-spacing: .07em;
}
.fleet-blog figure { margin: 2.8rem 0; }
.fleet-blog figure.wide { margin: 3.4rem 0; }
.fleet-blog figure svg { display: block; width: 100%; height: auto; }
.fleet-blog figcaption {
  margin-top: .75rem;
  max-width: 850px;
  font-size: .84rem;
  line-height: 1.45;
  opacity: .7;
}
.fleet-blog .note {
  margin: 2rem 0;
  padding: 1.15rem 0 1.15rem 1.2rem;
  border-left: 2px solid var(--ink);
}
.fleet-blog .status-strip {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  margin: 2.2rem 0 3rem;
  border-top: 1px solid var(--ink);
  border-bottom: 1px solid var(--ink);
}
.fleet-blog .status-strip > div { padding: 1.15rem 1rem 1.15rem 0; }
.fleet-blog .status-strip strong { display:block; font-size:1.35rem; line-height:1.05; }
.fleet-blog .status-strip span { display:block; margin-top:.35rem; font-size:.82rem; opacity:.72; }
.fleet-blog .table-wrap {
  width: 100%;
  overflow-x: auto;
  margin: 2rem 0;
  border-top: 2px solid var(--ink);
}
.fleet-blog table {
  width: 100%;
  min-width: 760px;
  border-collapse: collapse;
  font-size: .88rem;
  line-height: 1.45;
}
.fleet-blog th, .fleet-blog td {
  padding: .8rem .65rem;
  border-bottom: 1px solid var(--ink);
  vertical-align: top;
  text-align: left;
}
.fleet-blog th { font-size: .78rem; text-transform: uppercase; letter-spacing: .05em; }
.fleet-blog .mono-flow {
  margin: 2rem 0;
  padding: 1.25rem;
  border: 1px solid var(--ink);
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: .87rem;
  line-height: 1.6;
  white-space: pre-wrap;
}
.fleet-blog .timeline {
  display: grid;
  grid-template-columns: repeat(6, minmax(0, 1fr));
  gap: 0;
  margin: 2.7rem 0 3.5rem;
  border-top: 2px solid var(--ink);
}
.fleet-blog .timeline > div { padding: 1rem .9rem 0 0; }
.fleet-blog .timeline .n { display:block; font-size:.78rem; font-weight:700; margin-bottom:.35rem; }
.fleet-blog .timeline strong { display:block; line-height:1.25; }
.fleet-blog .timeline p { margin:.45rem 0 0; font-size:.82rem; line-height:1.4; opacity:.75; }
.fleet-blog details {
  margin: 1rem 0;
  padding: .95rem 0;
  border-top: 1px solid var(--ink);
}
.fleet-blog details:last-child { border-bottom: 1px solid var(--ink); }
.fleet-blog summary {
  cursor: pointer;
  font-weight: 700;
  list-style-position: outside;
}
.fleet-blog details > div { margin-top: 1rem; }
.fleet-blog .sources li { margin-bottom: .6rem; }
.fleet-blog .foot {
  margin-top: 4.5rem;
  padding: 1.4rem 0 2rem;
  border-top: 1px solid var(--ink);
  font-size: .86rem;
  opacity: .72;
}
@media (max-width: 1000px) {
  .fleet-blog .hero,
  .fleet-blog .section-grid { grid-template-columns: 1fr; gap: 1.8rem; }
  .fleet-blog .quick { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .fleet-blog .four-up { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .fleet-blog .timeline { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}
@media (max-width: 700px) {
  .fleet-blog { width: min(100% - 28px, 1180px); }
  .fleet-blog .hero { margin-bottom: 3rem; }
  .fleet-blog h1 { font-size: 3.2rem; }
  .fleet-blog .deck { font-size: 1.08rem; }
  .fleet-blog .two-up,
  .fleet-blog .three-up,
  .fleet-blog .four-up,
  .fleet-blog .quick,
  .fleet-blog .status-strip,
  .fleet-blog .timeline { grid-template-columns: 1fr; }
  .fleet-blog h2 { margin-top: 3.5rem; }
}
</style>

<article class="fleet-blog">

<header class="hero">
  <div>
    <p class="kicker">Research note · October 2026 · Work in progress</p>
    <h1>Who gets to remember?</h1>
    <p class="deck">When one coding agent learns something, should every future coding agent inherit it? This project is about deciding what deserves to become shared team knowledge—and proving that the decision actually changes software outcomes.</p>
  </div>
  <aside class="hero-meta">
    <p><strong>Project:</strong> Fleet Mem</p>
    <p><strong>Question:</strong> what should a fleet of coding agents remember together?</p>
    <p><strong>Current state:</strong> the benchmark setup works; we are still checking whether useful memory changes the coding agent’s behavior before running the full comparison</p>
    <p><strong>Important:</strong> there is no final “memory works” result yet</p>
  </aside>
</header>

<div class="reading">
  <p class="lede">Imagine a team of coding agents working on the same repository over time. One agent learns a testing trick. Another finds that a “general” fix breaks one subsystem. A third discovers an environment quirk. Saving all of those lessons sounds useful—until future agents are flooded with irrelevant, stale, or overgeneralized advice.</p>
</div>

<p class="standfirst"><strong>The project is not about building another memory database.</strong> It is about a narrower question: when does a lesson from one coding agent deserve to become shared knowledge for the whole fleet, and when should a later agent actually be shown it?</p>

<div class="quick">
  <div><strong>1 · Earlier work</strong>A coding agent performs a real repository task and leaves behind a short lesson.</div>
  <div><strong>2 · Share?</strong>Before future tasks are known, a small controller decides whether that lesson becomes shared team memory.</div>
  <div><strong>3 · Show?</strong>When a later task arrives, the system decides which shared lessons the new agent should actually see.</div>
  <div><strong>4 · Grade it</strong>We run the repository’s real tests and measure whether the memory helped, hurt, or changed nothing.</div>
</div>

<figure class="wide" aria-labelledby="pipeline-caption">
<svg viewBox="0 0 1100 290" role="img" aria-label="How Fleet Mem works">
  <g fill="none" stroke="currentColor" stroke-width="2">
    <rect x="30" y="90" width="170" height="72" rx="5"/>
    <rect x="250" y="90" width="170" height="72" rx="5"/>
    <rect x="470" y="90" width="170" height="72" rx="5"/>
    <rect x="690" y="90" width="170" height="72" rx="5"/>
    <rect x="910" y="90" width="160" height="72" rx="5"/>
    <path d="M200 126H250 M420 126H470 M640 126H690 M860 126H910"/>
    <path d="M239 119l11 7-11 7 M459 119l11 7-11 7 M679 119l11 7-11 7 M899 119l11 7-11 7"/>
  </g>
  <g fill="currentColor" text-anchor="middle">
    <text x="115" y="119" font-size="17">Earlier agent</text>
    <text x="115" y="143" font-size="14">learns a lesson</text>
    <text x="335" y="119" font-size="17">Share it?</text>
    <text x="335" y="143" font-size="14">yes / no</text>
    <text x="555" y="119" font-size="17">Team memory</text>
    <text x="555" y="143" font-size="14">many past lessons</text>
    <text x="775" y="119" font-size="17">Show it?</text>
    <text x="775" y="143" font-size="14">for this later task</text>
    <text x="990" y="119" font-size="17">Later agent</text>
    <text x="990" y="143" font-size="14">writes a patch</text>
    <text x="550" y="232" font-size="17">Repository tests tell us whether the memory actually helped or hurt.</text>
  </g>
</svg>
<figcaption id="pipeline-caption">Two separate decisions: what becomes shared knowledge, and what a later worker gets to see. Most memory systems blur those together.</figcaption>
</figure>

<h2>Why we collected many memories instead of one</h2>

<div class="section-grid">
  <div>
    <p>If a later coding task is handed exactly one known-helpful earlier lesson, the hard part has already been solved for us. There is almost nothing to govern.</p>
    <p>A realistic repository history is different. It contains several earlier experiences: useful ones, irrelevant ones, almost-right ones, old ones, duplicates, failed attempts, and lessons that are already written into the code or tests.</p>
    <p>That is why the current setup gives each later task a <strong>pool of earlier same-repository experiences</strong>. The system has to decide what should have become team knowledge instead of being told the answer in advance.</p>
  </div>
  <aside class="panel">
    <span class="big">13–114</span>
    <p>earlier same-repository experiences for each of the 11 clean development tasks in the current benchmark.</p>
    <p class="small">This was the first key check: does the benchmark contain enough competing history to make the memory decision non-trivial?</p>
  </aside>
</div>

<div class="two-up">
  <div class="panel">
    <h3>The easy version</h3>
    <p>“Here is the one earlier task we already know is related. Use it.”</p>
    <p class="small">Good for checking whether prior experience can help at all. Bad for studying what should enter shared memory.</p>
  </div>
  <div class="panel">
    <h3>The version we actually need</h3>
    <p>“Here are many earlier experiences from the same repository. Some may matter later. Decide what belongs in shared memory.”</p>
    <p class="small">Now the system has a real choice.</p>
  </div>
</div>

<h2>How the project drifted—and why we changed course</h2>

<div class="timeline">
  <div><span class="n">01</span><strong>Original idea</strong><p>Share nothing, share everything, or use a fast governor to decide.</p></div>
  <div><span class="n">02</span><strong>Jev-Mem arrives</strong><p>We worried the memory-governance idea was already taken.</p></div>
  <div><span class="n">03</span><strong>Wrong detour</strong><p>We shifted toward “text lesson vs regression test” as the novelty.</p></div>
  <div><span class="n">04</span><strong>ChainSWE</strong><p>We chose a realistic sequence of maintenance tasks.</p></div>
  <div><span class="n">05</span><strong>Diagnosis</strong><p>The repository itself carried most of the useful state; the memory governor rarely had a real decision.</p></div>
  <div><span class="n">06</span><strong>Fleet Mem</strong><p>Return to the original question, but redesign the benchmark so it actually tests it.</p></div>
</div>

<div class="reading">
  <h3>The Jev-Mem misunderstanding</h3>
  <p>Jev-Mem absolutely covers a lot of memory control: it organizes memories, scores candidates, decides how much to retrieve, checks evidence, and controls when to stop. That meant we could no longer say “we invented memory governance.”</p>
  <p>But we initially overreacted. In the configuration evaluated in the paper, Jev-Mem <strong>does not learn a keep-or-discard decision when an observation first arrives</strong>. Its active configuration keeps valid observations and places most selectivity later, during organization and retrieval. It can reason about redundancy, contradiction, and obsolescence later, but it does not establish the exact question we care about: should this coding experience cross from one worker into shared team memory in the first place?</p>

  <h3>The regression-test detour</h3>
  <p>After worrying that Jev-Mem had “taken” the idea, we tried moving the novelty elsewhere: first decide whether a lesson is worth keeping, then compare the same lesson stored as text versus stored as a repository-native regression test. That can be an interesting project, but it was no longer the paper we originally wanted. Jev became an optional baseline instead of the central controller.</p>

  <h3>Why ChainSWE looked right—but was wrong for the main question</h3>
  <p>ChainSWE looked attractive because it gives real sequences of maintenance tasks. The repository evolves and later agents inherit the updated codebase. That feels like a real coding-agent fleet.</p>
  <p>The problem is that the repository itself is already a powerful memory. New code, tests, and fixes persist. In our run, extra textual memory often had little unique work to do.</p>
</div>

<div class="status-strip">
  <div><strong>36</strong><span>frozen ChainSWE contexts in the clean run</span></div>
  <div><strong>14 / 36</strong><span>No Share resolved</span></div>
  <div><strong>12 / 36</strong><span>Share-All resolved</span></div>
  <div><strong>12 / 36</strong><span>Governed resolved</span></div>
</div>

<div class="reading">
  <p>The result that mattered most was not 14 vs 12 vs 12. It was that only <strong>7 targets</strong> had multiple candidate memories, most extracted lessons were simple restatements of code, and there were almost no real stale/conflicting cases for the governor to distinguish.</p>
  <p class="note"><strong>So the experiment did not show that governance fails.</strong> It showed that we had built an experiment where the governor rarely had anything meaningful to govern.</p>
</div>

<h2>The redesign: use SWE-ContextBench, but not in its original form</h2>

<div class="section-grid">
  <div>
    <p>SWE-ContextBench remains useful because it already gives us real repositories, earlier coding experiences, later related tasks, timestamps, executable grading, and a hidden clue about which earlier task is known to be useful.</p>
    <p>But the standard setup is too easy for our question because it can directly connect one known-related earlier task to one later task.</p>
    <p>We keep the benchmark’s known relation <strong>hidden</strong>. It is used to check whether a useful signal exists—not to choose what the later agent sees.</p>
  </div>
  <aside class="panel">
    <h3>The central change</h3>
    <p><strong>Before:</strong> known related past task → later task.</p>
    <p><strong>Now:</strong> all valid earlier same-repository tasks → pool of possible memories → share decisions → later task.</p>
  </aside>
</div>

<div class="mono-flow">Earlier repository history
A   C   D   E   F   G   ...
 \  |  / \  |  / 
  short lessons from earlier agents
            ↓
      decide what becomes shared
            ↓
        team memory bank
            ↓
      decide what this later agent sees
            ↓
        later coding task
            ↓
       executable tests</div>

<div class="reading">
  <p>The earlier source→later task link still matters, but only as a hidden reference. It gives us a useful “best-case” comparison: if we deliberately hand the worker the known relevant past experience, does that change the outcome at all?</p>
  <p>That check is important because there is no point evaluating a sophisticated memory governor if even the known useful memory cannot move the coding worker.</p>
</div>

<h2>How we tried to avoid another wasted experiment</h2>

<div class="reading">
  <p>We deliberately split the work into two independent repositories before either implementation could influence the other.</p>
</div>

<div class="two-up">
  <div class="panel">
    <h3>Agent 1</h3>
    <p>Test the cheapest hypothesis: can SWE-ContextBench be turned into a real team-memory benchmark simply by replacing its one-pair setup with full earlier repository histories?</p>
  </div>
  <div class="panel">
    <h3>Agent 2</h3>
    <p>Test the harder hypothesis independently: can SWE-rebench V2 give us a substantially better natural benchmark built around repository history from the start?</p>
  </div>
</div>

<div class="reading">
  <p>The implementations were told not to share code or intermediate findings during their first audits. The only intentional overlap was the basic “no future information” rule and a small common record format for repository, earlier/later task IDs, timestamps, provenance, history IDs, environment status, and leakage class.</p>
  <p>We also ran a separate adversarial literature/methodology review whose job was to <strong>kill the paper if the gap was already occupied</strong>. That review changed the claim materially: MemGuard and CODESKILL are too close for us to say “nobody has decided which coding-agent experiences should enter memory.” MemGauge also shows that separating write, management, and read stages is not itself a new methodological idea.</p>
  <p>The outcome of that audit was <strong>modify, not stop</strong>: keep the project, but make the contribution repository-scoped team memory with a controlled separation between the share decision and the later show decision, both judged by executable software outcomes.</p>
</div>

<h2>We also tried building a new benchmark from scratch</h2>

<div class="reading">
  <p>We did not simply assume SWE-ContextBench was the answer. Two independent implementations were started in parallel:</p>
</div>

<div class="two-up">
  <div class="panel">
    <h3>Track 1 · ContextBench overlay</h3>
    <p>Keep the existing executable software tasks, but rebuild the history around them so later agents face many earlier experiences rather than one chosen pair.</p>
    <p><strong>Result:</strong> the structural check passed.</p>
  </div>
  <div class="panel">
    <h3>Track 2 · Native benchmark from SWE-rebench V2</h3>
    <p>Build repository histories directly from a much larger pool of real software tasks, without inheriting ContextBench’s pair structure.</p>
    <p><strong>Result:</strong> richer histories, but the useful relationships and executable validation were not reliable enough for the current paper.</p>
  </div>
</div>

<h3>What the SWE-rebench experiment taught us</h3>

<div class="four-up">
  <div class="panel"><span class="big">48</span><p>frozen later tasks across 12 repositories</p></div>
  <div class="panel"><span class="big">226</span><p>eligible earlier work episodes</p></div>
  <div class="panel"><span class="big">600</span><p>earlier→later history links</p></div>
  <div class="panel"><span class="big">2–75</span><p>earlier tasks per later task; median 6, mean 12.5</p></div>
</div>

<div class="reading">
  <p>History richness was excellent. Relation quality was not. The audit found no explicit backreferences, no same-PR or identical-patch links, only 11 high text-similarity links, 282 shared-path links, and just 13 shared changed-symbol links. Path overlap by itself was too noisy to tell us which earlier work was genuinely useful.</p>
  <p>We also found 17 possible “older lesson may have been replaced” cases and 3 possible conflict cases, but none were human-confirmed. The timeline was based on issue/PR creation time, not known completion or merge time, so “earlier” was not as clean as we wanted.</p>
  <p>The biggest blocker was executable validation: although the task images were mostly available, only <strong>1 of 48</strong> later tasks passed both the no-fix and reference-fix checks end-to-end. That is not enough for a paper built around causal software outcomes.</p>
  <p>So the decision was: <strong>use the ContextBench overlay now; keep the native SWE-rebench benchmark as follow-up work.</strong></p>
</div>

<h2>What makes Fleet Mem different from just “memory for coding agents”</h2>

<div class="reading">
  <p>There is already a lot of nearby work. The contribution has to be narrow and honest.</p>
</div>

<div class="table-wrap">
<table>
<thead>
<tr><th>Existing work</th><th>What it already covers</th><th>What remains different here</th></tr>
</thead>
<tbody>
<tr><td><strong>SWE-ContextBench</strong></td><td>Past coding experience can help later tasks; mismatched experience can hurt.</td><td>It does not directly test which earlier experiences should become shared team memory before future tasks are known.</td></tr>
<tr><td><strong>VibeMemBench</strong></td><td>Large histories and strong tests of whether memory systems can recover useful experience.</td><td>Excellent for “can the system use known-useful history?”; less clean for natural keep/share decisions when the experience is first created.</td></tr>
<tr><td><strong>MemGuard</strong></td><td>Checks whether coding memories should be admitted, handles stale/conflicting/duplicate memories, and manages later retrieval.</td><td>This rules out broad “first memory admission” claims. Our narrower focus is a controlled cross-worker team setting with separate share and show decisions.</td></tr>
<tr><td><strong>GateMem</strong></td><td>Shared-memory governance across multiple principals.</td><td>Not executable software repair with patch-level grading.</td></tr>
<tr><td><strong>CODESKILL / STAIR</strong></td><td>Extract, maintain, abstract, and reuse coding skills or repair plans.</td><td>They already occupy much of the “learn reusable coding knowledge” space.</td></tr>
<tr><td><strong>Agent Memory Bench</strong></td><td>Tests present, absent, replaced, contradictory, and adjacent coding memories.</td><td>Its public setup is primarily a read test over a memory collection built before the run, not workers generating and promoting memories as they work.</td></tr>
<tr><td><strong>MemGauge</strong></td><td>Separates memory writing, management, and later exposure under matched conditions.</td><td>Shows that stage-by-stage causal separation is not itself novel; its focus is not repository-scoped coding work with executable patch grading.</td></tr>
<tr><td><strong>Jev-Mem</strong></td><td>Fast, bounded memory-control decisions and structured retrieval control.</td><td>Useful as our lightweight controller, but not itself the novelty claim.</td></tr>
<tr><td><strong>Shared organizational-memory deployment work</strong></td><td>Shows that shared memory for enterprise coding agents is already a real systems idea.</td><td>Shared organizational memory itself is not new; the controlled causal evaluation is the point.</td></tr>
</tbody>
</table>
</div>

<div class="reading">
  <p>A safer paper claim is therefore:</p>
</div>

<p class="standfirst"><strong>Build a controlled executable test for team memory in coding-agent fleets, separate “should this lesson become shared?” from “should this later agent see it?”, and compare a cheap fast controller with a stronger reasoning model.</strong></p>

<h2>The four questions we are actually asking</h2>

<div class="two-up">
  <div class="panel">
    <h3>1 · Is sharing everything harmful?</h3>
    <p>If every lesson becomes team memory, do later coding agents sometimes get worse because of irrelevant or misleading history?</p>
  </div>
  <div class="panel">
    <h3>2 · Can we decide early what deserves team status?</h3>
    <p>At the moment a lesson is created—and before future tasks are known—can we make a useful share / do-not-share decision?</p>
  </div>
  <div class="panel">
    <h3>3 · Is “worth sharing” different from “worth showing now”?</h3>
    <p>A lesson can have been reasonable to keep in January and still be wrong for one particular task in July.</p>
  </div>
  <div class="panel">
    <h3>4 · Can a cheap controller do this well?</h3>
    <p>How much of a strong reasoning model’s benefit can a fast System-One/Jev-style controller recover at much lower cost and latency?</p>
  </div>
</div>

<h2>The experiment, in plain language</h2>

<div class="table-wrap">
<table>
<thead><tr><th>Version</th><th>What the later coding agent gets</th><th>Why we need it</th></tr></thead>
<tbody>
<tr><td><strong>No memory</strong></td><td>Nothing from earlier agents.</td><td>Baseline.</td></tr>
<tr><td><strong>Share everything</strong></td><td>All eligible earlier lessons, under a fixed context budget.</td><td>Tests whether indiscriminate sharing creates noise.</td></tr>
<tr><td><strong>Randomly share the same amount</strong></td><td>A random subset with the same size as the governor’s subset.</td><td>If the governor wins, we need to know whether it picked better memories or simply showed fewer tokens.</td></tr>
<tr><td><strong>Govern what gets shared</strong></td><td>Only lessons approved before the future task is known.</td><td>Measures the value of the share decision itself.</td></tr>
<tr><td><strong>Govern what gets shown</strong></td><td>Everything may be stored, but only selected memories are exposed to the later agent.</td><td>Measures whether filtering at use time is enough.</td></tr>
<tr><td><strong>Govern both</strong></td><td>Selective sharing plus selective exposure.</td><td>Tests the full design.</td></tr>
<tr><td><strong>Strong reasoning model</strong></td><td>Same decisions, but made by a more expensive LLM.</td><td>Quality/cost comparison.</td></tr>
<tr><td><strong>Known helpful memory</strong></td><td>The benchmark’s known relevant earlier experience is given directly.</td><td>Best-case signal check: can useful memory move this worker at all?</td></tr>
</tbody>
</table>
</div>

<div class="reading">
  <h3>Five rules we froze before the real comparison</h3>
  <ol>
    <li><strong>The share decision happens once per lesson.</strong> An earlier lesson cannot be “shared for task B but not shared for task C.” That would secretly use knowledge of future tasks.</li>
    <li><strong>The main write decision is just share / do not share.</strong> We originally used “reject / keep local / share,” but if workers disappear after each task, “keep local” and “reject” are experimentally identical.</li>
    <li><strong>The main read decision is show / withhold.</strong> We originally considered “ignore / advisory / rely,” but that changes how the coding worker is instructed and adds a confound.</li>
    <li><strong>The lesson extractor must try to capture candidate lessons broadly.</strong> It must not quietly pre-filter for only “good reusable lessons,” because then the extractor would already be doing the governor’s job.</li>
    <li><strong>When testing the sharing decision, later selection stays fixed.</strong> We change one thing at a time.</li>
  </ol>
</div>

<h2>What counts as a valid earlier memory?</h2>

<div class="section-grid">
  <div>
    <p>We enforce a strict “no information from the future” rule. When a lesson is created, the extractor and share decision may see only the earlier task, the agent’s own trajectory, commands, tests, patch, and what was available in the repository at that time.</p>
    <p>They may not see the later task, its hidden tests, its gold patch, later commits, or whether the memory eventually helped.</p>
    <p>The known earlier→later relation may exist in the benchmark, but it is hidden from the memory system.</p>
  </div>
  <aside class="panel">
    <h3>Why this matters</h3>
    <p>If future-task information leaks into the share decision, the experiment stops measuring whether the organization made a good decision at the time.</p>
  </aside>
</div>

<div class="three-up">
  <div class="panel"><h3>Clean history</h3><p>Clearly earlier task, separate work episode, no obvious answer leak.</p></div>
  <div class="panel"><h3>Questionable history</h3><p>Later task explicitly references the older issue, nearly gives away the old fix, or chronology is uncertain.</p></div>
  <div class="panel"><h3>Exclude from main analysis</h3><p>Same PR/co-resolution, same commit, invalid environment, or ambiguous ordering.</p></div>
</div>

<div class="reading">
  <p>We still keep questionable cases for sensitivity analysis and case studies. We do not silently delete them.</p>

  <h3>A lesson may already be “stored” in the repository</h3>
  <p>An earlier lesson can become redundant because it is already encoded in the current implementation, a regression test, documentation, comments, configuration, or CI rules. We added an explicit diagnostic for that case. A good controller may decide that no extra textual memory is needed because the repository already remembers it.</p>

  <h3>Natural history first, stress cases second</h3>
  <p>The main benchmark uses naturally occurring earlier experiences. A secondary stress set can emphasize difficult cases—duplicate advice, overly broad advice, old guidance that may have been replaced, conflicting lessons, lessons from failed attempts, or superficially similar but wrong advice. We do not want the whole paper to depend on synthetic traps invented to make our method look good.</p>
</div>

<h2>What a memory item actually contains</h2>

<div class="reading">
  <p>The memory object is deliberately simple. It is not a graph database or a new memory architecture. Each item is a short, atomic claim with enough provenance to audit where it came from.</p>
</div>

<div class="three-up">
  <div class="panel"><h3>What it says</h3><p>Claim, type, scope, preconditions, how general it seems.</p></div>
  <div class="panel"><h3>Why we believe it</h3><p>Source task, source outcome, evidence, files/symbols touched, commands/tests that support it.</p></div>
  <div class="panel"><h3>Why it may be risky</h3><p>Confidence, failure-derived flag, possible staleness, possible conflict, and a provenance hash.</p></div>
</div>

<div class="reading">
  <p>Examples include repository conventions, procedures, architecture facts, debugging heuristics, failure-avoidance lessons, testing/workflow facts, and environment/setup facts.</p>
</div>

<h2>The benchmark construction itself passed its first check</h2>

<div class="status-strip">
  <div><strong>11</strong><span>clean later tasks</span></div>
  <div><strong>13–114</strong><span>earlier same-repo candidates per task</span></div>
  <div><strong>603</strong><span>candidate prompt/exposure items in the smoke setup</span></div>
  <div><strong>11 / 11</strong><span>Share-All and the placeholder governed path produced different exposures, proving the plumbing can vary memory</span></div>
</div>

<div class="reading">
  <p>That last number is <strong>not a research result</strong>. In that early smoke check, all 603 candidate memories were kept local by the placeholder policy, source outcomes were not yet known, the real Jev controller had not run, the strong LLM controller had not run, and the coding worker had not been evaluated under those memory conditions.</p>
  <p>It only proved that the benchmark builder and memory-routing code could create different conditions reproducibly.</p>
</div>

<h2>The current blocker is the coding worker, not the benchmark</h2>

<div class="reading">
  <p>Before comparing memory policies, we need a coding agent that is neither broken nor so strong that memory can never matter.</p>
  <p>The original development rule was simple: the worker should fully solve at least 2 of 3 test tasks. GPT-6 Luna failed that rule. We keep that failure in the record exactly as-is.</p>
</div>

<div class="two-up">
  <div class="panel">
    <h3>SymPy task</h3>
    <p>Luna produced a real patch that applied and fixed 1 of 2 failing tests, but the patched run became dramatically slower and timed out around 46% after 1,800 seconds.</p>
    <p class="small">No-patch runs were about 178–182 seconds; the gold/reference patch completed in 323 seconds. This strongly suggests a Luna-patch regression, though it was not profiler-confirmed.</p>
  </div>
  <div class="panel">
    <h3>Django task</h3>
    <p>Luna produced a real patch, fixed the reported duplicate-column case, fixed 1 of 6 failing tests, and preserved all 166 previously passing tests.</p>
    <p class="small">That is incomplete, but it shows the worker can understand the repository, edit code, submit a patch, and survive the evaluator.</p>
  </div>
</div>

<div class="reading">
  <p>That changed the development question. Instead of asking only “does Luna solve enough tasks from scratch?”, we now ask “is Luna capable enough that a useful memory could measurably help or hurt it?” A partially capable worker may actually be better for this study than a nearly perfect one because there is room for memory to make a difference.</p>
</div>

<h2>The stop/continue check before we spend on the governor</h2>

<figure class="wide" aria-labelledby="gate-caption">
<svg viewBox="0 0 1100 300" role="img" aria-label="Experiment progression">
  <g fill="none" stroke="currentColor" stroke-width="2">
    <rect x="30" y="80" width="200" height="70" rx="5"/>
    <rect x="290" y="80" width="200" height="70" rx="5"/>
    <rect x="550" y="80" width="200" height="70" rx="5"/>
    <rect x="810" y="80" width="240" height="70" rx="5"/>
    <path d="M230 115H290 M490 115H550 M750 115H810"/>
    <path d="M279 108l11 7-11 7 M539 108l11 7-11 7 M799 108l11 7-11 7"/>
  </g>
  <g fill="currentColor" text-anchor="middle">
    <text x="130" y="108" font-size="17">History pools</text>
    <text x="130" y="132" font-size="14">PASS</text>
    <text x="390" y="108" font-size="17">Evaluator + patches</text>
    <text x="390" y="132" font-size="14">PASS</text>
    <text x="650" y="108" font-size="17">Useful-memory check</text>
    <text x="650" y="132" font-size="14">CURRENT</text>
    <text x="930" y="108" font-size="17">Full memory comparison</text>
    <text x="930" y="132" font-size="14">NOT RUN</text>
    <text x="550" y="225" font-size="18">No memory  ↔  known helpful past experience</text>
    <text x="550" y="253" font-size="14">If this does not change real outcomes, stop before running a sophisticated governor.</text>
  </g>
</svg>
<figcaption id="gate-caption">The best-case memory check comes first. If a known useful lesson cannot move the worker, the more complicated comparison has no signal to recover.</figcaption>
</figure>

<div class="reading">
  <p>Before that check, we are comparing Luna and Sol on the same already-used development tasks. The goal is not to keep switching models until something works. The rule change was written down before any new model result, and the task set, histories, cards, evaluator, and research question remain frozen.</p>
  <p>The development amendment was committed before running the new comparison. At the last recorded state in the conversation, the Sol route had been configured at the same effort level, all 40 tests passed, but Sol itself had <strong>not yet run</strong> because the protected OpenAI environment file was unavailable in that launch environment.</p>
</div>

<h3>Frozen development state</h3>
<div class="three-up">
  <div class="panel"><h3>Original qualification</h3><p><strong>FAILED.</strong> Preserve it; do not reinterpret it as a pass.</p></div>
  <div class="panel"><h3>Memory experiments</h3><p><strong>None run yet.</strong> No Jev, Share-All, random, or full comparison outcome exists.</p></div>
  <div class="panel"><h3>Repository state</h3><p>40 tests passed; frozen plan hash <code>b6535c56e8db63dd72f4e7901960d995db533214df22e139034f99cd29f6a7f5</code>.</p></div>
</div>

<h2>What we will measure</h2>

<div class="reading">
  <p>The headline outcome is simple: did the later coding agent solve the task without breaking things that already worked?</p>
</div>

<div class="three-up">
  <div class="panel"><h3>Software outcome</h3><p>Task resolved, originally failing tests fixed, previously passing tests preserved, memory helped, memory hurt, or no change.</p></div>
  <div class="panel"><h3>Agent effort</h3><p>Tokens, tool calls, steps, latency, and worker cost.</p></div>
  <div class="panel"><h3>Memory overhead</h3><p>How many memories were shared, how many were shown, memory tokens, controller cost, and controller latency.</p></div>
</div>

<div class="reading">
  <p>We also want performance broken down by how old the memory is, what kind of relationship it has to the later task, whether it may be stale or conflicting, and how deep into the repository history the task occurs.</p>
  <p>A benchmark relation is only a clue. The final evidence is always the real downstream software effect.</p>
</div>

<h2>What would make the result interesting?</h2>

<div class="two-up">
  <div class="panel">
    <h3>If sharing everything hurts</h3>
    <p>Then team memory needs selectivity; simply storing more experience is not enough.</p>
  </div>
  <div class="panel">
    <h3>If random sharing matches the governor</h3>
    <p>Then the “win” may just come from showing less context, not making smarter decisions.</p>
  </div>
  <div class="panel">
    <h3>If early filtering matters more</h3>
    <p>The important decision is what becomes institutional knowledge in the first place.</p>
  </div>
  <div class="panel">
    <h3>If later filtering matters more</h3>
    <p>It may be fine to keep broad history as long as each worker sees only what it needs.</p>
  </div>
  <div class="panel">
    <h3>If the cheap controller nearly matches the LLM</h3>
    <p>That supports a lightweight control layer instead of repeated expensive reasoning over memory.</p>
  </div>
  <div class="panel">
    <h3>If nothing beats no memory</h3>
    <p>That is still a useful result: code, tests, and repository state may already carry most of what a worker needs.</p>
  </div>
</div>

<h2>What we deliberately did not do</h2>

<div class="reading">
  <ul>
    <li>We did not claim that the 14/36 vs 12/36 ChainSWE result proves governance is useless.</li>
    <li>We did not quietly add arbitrary junk memories when the first benchmark had too few choices.</li>
    <li>We did not use later-task gold patches to create the memories shown to workers.</li>
    <li>We did not tune the coding worker and memory policy at the same time.</li>
    <li>We did not change the task set after seeing memory outcomes.</li>
    <li>We did not treat the 603-item smoke check as evidence that the governor works.</li>
    <li>We did not run Jev before proving that useful memory can affect the worker.</li>
    <li>We did not switch the paper to SWE-rebench just because it had larger histories.</li>
    <li>We did not keep the text-card-vs-regression-test detour as the central contribution.</li>
    <li>We did not make “first memory governance,” “first shared memory,” “first provenance,” or “first forgetting” claims.</li>
  </ul>
</div>

<h2>What the paper is now</h2>

<p class="standfirst">A controlled executable study of when coding experience should become shared team memory, when it should be shown to later coding agents, and whether a cheap fast controller can make those decisions almost as well as a more expensive reasoning model.</p>

<div class="reading">
  <p>That framing survives even if the controller changes. Jev is an important method under test, not the scientific contribution by itself.</p>
  <p>The benchmark contribution also matters independently: it turns a known related pair into a real repository history with many plausible memories, keeps future information out of the share decision, and gives us paired software outcomes under different memory rules.</p>
</div>

<h2>Immediate next steps</h2>

<div class="four-up">
  <div class="panel"><span class="big">1</span><p>Finish the small Luna-vs-Sol check on the same already-used tasks.</p></div>
  <div class="panel"><span class="big">2</span><p>Choose one coding worker and freeze it.</p></div>
  <div class="panel"><span class="big">3</span><p>Compare no memory against the known helpful earlier experience on the burned development set.</p></div>
  <div class="panel"><span class="big">4</span><p>Only if useful memory changes multiple real outcomes, run the full memory-policy comparison.</p></div>
</div>

<div class="reading">
  <p>For the submission plan discussed in the research log: finish the worker choice first, run the useful-memory check next, launch the small governance comparison only if that passes, then freeze the clean experiment and spend the remaining time on results and writing. The native SWE-rebench version remains follow-up work unless the current overlay unexpectedly fails.</p>
</div>

<h2>Technical appendix: details kept out of the main story</h2>

<details>
<summary>Exact benchmark-audit rules</summary>
<div>
<p>The audit records, where available: earlier-task ID, later-task ID, repository, timestamps, whether the earlier task truly precedes the later one, same PR, same commit, whether the earlier change exists in the later task’s ancestry, whether the later issue mentions the earlier issue or PR, whether the later issue describes the earlier failure or contains a solution hint, file overlap, symbol overlap, patch overlap, relationship type, number of earlier candidates, environment validity, and a leakage-risk class.</p>
<p>Primary classes include clean earlier work, explicit backreference, regression/revert, same-PR/co-resolution, high target hint, ambiguous order, already institutionalized, possible replacement, possible conflict, and invalid environment.</p>
</div>
</details>

<details>
<summary>Exact memory record fields</summary>
<div>
<p>Each candidate memory can store: memory ID, earlier task, repository, earlier-task time, earlier worker outcome, claim, memory type, scope, preconditions, evidence, evidence references, file/symbol provenance, confidence, whether the memory comes from a failed attempt, possible staleness, possible conflict, and a provenance hash.</p>
<p>Two source modes are kept separate: benchmark-provided experience for construction smoke tests, and fresh coding-agent trajectories for the intended scientific run. The two are not treated as equivalent.</p>
</div>
</details>

<details>
<summary>Original benchmark-scale numbers and earlier audits</summary>
<div>
<p>SWE-ContextBench Lite originally provided 300 experience tasks and 99 related later tasks. Our earlier strict audit removed same-PR/co-resolution and missing-trace cases, leaving 73 usable later tasks across 10 repositories with at least one mapped earlier trajectory. That prior leakage work was reused rather than discarded.</p>
<p>VibeMemBench was attractive for the read side because it reports 111 later tasks, 90 repositories, and 3,634 historical trajectories, with each retained task known to have at least one experience that produced executable uplift in a reference setting. That is excellent motivation for selective memory use, but its construction is less clean for natural online share decisions.</p>
</div>
</details>

<details>
<summary>Why the second benchmark is still worth building later</summary>
<div>
<p>SWE-rebench V2 offers far richer repository histories. In the pilot we froze 48 later tasks across 12 repositories, 226 earlier episodes, and 600 history links. Every later task had at least two predecessors; 36 had at least five. That is much closer to how a real organization accumulates history.</p>
<p>But useful relationships were not established strongly enough, chronology was only approximated by created-at timestamps, and only 1/48 tasks survived full executable control validation. A serious future version should invest in relation discovery, human auditing, stronger chronology, and agent-generated earlier trajectories before claiming it as a benchmark.</p>
</div>
</details>

<details>
<summary>Worker-selection chronology, including the failed harness attempts</summary>
<div>
<p>Before the graded Luna patches, one corrected qualification job using the local/Ollama worker returned model responses but produced <strong>0/3 nonempty patches</strong>. Two runs hit a 12-step cap and the third submitted an empty patch. Because there was no usable patch, canonical FAIL_TO_PASS / PASS_TO_PASS grading was unavailable; those values were unmeasured, not zero.</p>
<p>We traced part of that to the worker contract. The upstream Mini-SWE SWE-bench setup expects a real <code>patch.txt</code> and an exact final submission command, and its standard budget is far larger than 12 steps. Those runs were therefore treated as infrastructure failures rather than evidence that the scientific idea or benchmark had failed.</p>
<p>The recommendation then moved to a stronger worker. Luna was chosen first for cost, because no valid memory result existed yet and switching workers before treatment did not contaminate the experiment. After the first graded Luna failures, the immediate recommendation briefly moved to Sol. A deeper inspection of the actual patches then showed partial competence, so the plan was amended again—before any memory treatment—to compare Sol and Luna on the same already-burned tasks rather than declaring Luna unusable from a tiny binary sample.</p>
<p>The key methodological record remains: the original 2/3 full-resolution qualification gate failed; we do not erase that result. The amendment changes what we consider sufficient evidence that a worker is suitable for a memory-intervention study.</p>
</div>
</details>

<details>
<summary>Old development rules we refuse to repeat</summary>
<div>
<ul>
<li>Do not tune the coding solver and memory policy at the same time.</li>
<li>Establish the official evaluator independently before interpreting memory outcomes.</li>
<li>Bad tool/model integration can swamp the entire memory effect.</li>
<li>Keep a strict “no future information” firewall.</li>
<li>Use gold/no-patch runs only as infrastructure checks, not model-dependent science.</li>
<li>Do not silently change the task set after outcomes appear.</li>
<li>Keep experiment-owned artifacts separate from the benchmark’s official grading state.</li>
<li>Do not assume that sequential tasks automatically create useful memory-transfer cases.</li>
<li>Do not scale an expensive run until the small experiment proves that the intended decision is actually present.</li>
</ul>
</div>
</details>

<details>
<summary>Frozen development artifacts from the latest recorded state</summary>
<div>
<p>Development report: <code>fleet-mem-contextbench/docs/PILOT_DEVELOPMENT_REPORT.md</code></p>
<p>Frozen amendment: <code>fleet-mem-contextbench/docs/PILOT_DEVELOPMENT_AMENDMENT_02.md</code></p>
<p>SymPy timing evidence: <code>fleet-mem-contextbench/artifacts/development/sympy_timing_diagnosis.json</code></p>
<p>Recorded commits: <code>cd16b80</code>, <code>d1d9e8f</code>, <code>6974290</code>.</p>
<p>Native SWE-rebench benchmark repo checkpoints: <code>f4dadcd</code>, <code>46ddbdb</code>, <code>a79f354</code>.</p>
</div>
</details>

<h2>References</h2>

<ul class="sources">
  <li><a href="https://arxiv.org/abs/2602.08316">SWE-ContextBench</a></li>
  <li><a href="https://arxiv.org/abs/2607.02606">ChainSWE</a></li>
  <li><a href="https://arxiv.org/abs/2609.23570">VibeMemBench</a></li>
  <li><a href="https://arxiv.org/abs/2606.18829">GateMem</a></li>
  <li><a href="https://arxiv.org/abs/2608.21867">MemGuard</a></li>
  <li><a href="https://arxiv.org/pdf/2609.23986">Jev-Mem</a></li>
  <li><a href="https://arxiv.org/abs/2605.25430">CODESKILL</a></li>
  <li><a href="https://arxiv.org/abs/2603.15401">SWE-Skills-Bench</a></li>
  <li><a href="https://huggingface.co/datasets/ZiLaotou/MemCalib">MemCalib</a></li>
  <li><a href="https://github.com/GiulioDER/agent-memory-bench">Agent Memory Bench</a></li>
  <li><a href="https://proceedings.mlr.press/v306/badertdinov26a.html">SWE-rebench V2</a></li>
</ul>

<p class="foot">Active research note. The benchmark construction has passed its structural check. The main memory comparison has not run yet. The page is deliberately written as a research log rather than a claim of finished results.</p>

</article>
