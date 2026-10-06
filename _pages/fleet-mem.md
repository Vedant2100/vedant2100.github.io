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
#main { max-width: 1500px; }
#main .page { width:100%; max-width:none; float:none; padding-right:0; }
#main .page__inner-wrap, #main .page__content { width:100%; max-width:none; }

.fleet-page {
  --bg-primary:#ffffff;
  --bg-secondary:#f8fafc;
  --text-primary:#1f2937;
  --text-secondary:#4b5563;
  --accent:#2563eb;
  --border-color:#e5e7eb;
  color:var(--text-primary);
  font-family:Georgia,"Times New Roman",Times,serif;
  line-height:1.8;
  background:var(--bg-primary);
}
.fleet-page * { box-sizing:border-box; }
.fleet-page .layout-wrapper {
  display:flex;
  flex-direction:row;
  max-width:1400px;
  margin:0 auto;
  padding:2rem;
  gap:4rem;
  align-items:stretch;
  justify-content:center;
}
.fleet-page .toc-sidebar {
  flex:0 0 310px;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
}
.fleet-page .toc-sticky {
  position:sticky;
  top:2rem;
  background:var(--bg-secondary);
  padding:1.35rem;
  border-radius:8px;
  border:1px solid var(--border-color);
  max-height:calc(100vh - 4rem);
  overflow-y:auto;
}
.fleet-page .toc-sticky h3 {
  margin:0 0 .65rem;
  padding-bottom:.5rem;
  border-bottom:1px solid var(--border-color);
  font-size:1.05rem;
}
.fleet-page .toc-sticky ul { list-style:none; padding:0; margin:0; }
.fleet-page .toc-sticky li { margin:.38rem 0; font-size:.88rem; }
.fleet-page .toc-sticky a { color:var(--text-secondary); text-decoration:none; display:block; }
.fleet-page .toc-sticky a:hover { color:var(--accent); }

.fleet-page .main-content { flex:1; min-width:0; max-width:850px; }
.fleet-page header { text-align:center; margin-bottom:3rem; }
.fleet-page h1,.fleet-page h2,.fleet-page h3,.fleet-page h4 {
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  color:#111827;
  line-height:1.3;
}
.fleet-page h1 { font-size:1.72rem; font-weight:700; margin:0 0 .55rem; letter-spacing:-.015em; }
.fleet-page .subtitle {
  margin:0 auto;
  max-width:760px;
  font-size:1.08rem;
  line-height:1.5;
  color:var(--text-secondary);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
}
.fleet-page .meta {
  margin-top:1rem;
  color:#6b7280;
  font-size:.9rem;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
}
.fleet-page h2 {
  font-size:1.42rem;
  font-weight:700;
  margin:2.8rem 0 .8rem;
  padding-bottom:.5rem;
  border-bottom:1px solid var(--border-color);
}
.fleet-page h3 { font-size:1.15rem; margin:1.7rem 0 .5rem; }
.fleet-page p { margin:0 0 1rem; font-size:1rem; }
.fleet-page ul,.fleet-page ol { font-size:1rem; margin:0 0 1.5rem; padding-left:1.5rem; }
.fleet-page li { margin-bottom:.45rem; }
.fleet-page a { color:var(--accent); text-underline-offset:.14em; }

.fleet-page .tldr {
  font-size:1.02rem;
}
.fleet-page .mermaid-like {
  margin:2rem 0 .5rem;
  padding:1rem;
  border:1px solid var(--border-color);
  border-radius:4px;
  background:#fff;
  overflow-x:auto;
}
.fleet-page .mermaid-like svg { display:block; width:100%; min-width:760px; height:auto; }
.fleet-page .figure-caption {
  text-align:center;
  font-style:italic;
  margin:.55rem 0 2rem;
  color:var(--text-secondary);
  font-size:.92rem;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
}
.fleet-page .accent-node { fill:#eaf2ff; stroke:var(--accent); stroke-width:2.5; }
.fleet-page .node { fill:#fff; stroke:#6b7280; stroke-width:1.4; }
.fleet-page .soft-node { fill:#f8fafc; stroke:#9ca3af; stroke-width:1.2; }
.fleet-page .edge { fill:none; stroke:#6b7280; stroke-width:1.5; }
.fleet-page .dashed { stroke-dasharray:6 5; }
.fleet-page .figure-text { fill:#111827; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; }
.fleet-page .figure-muted { fill:#4b5563; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; }

.fleet-page table {
  width:100%;
  border-collapse:collapse;
  margin:2rem 0;
  background:#fff;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size:.92rem;
}
.fleet-page th,.fleet-page td {
  padding:.72rem .85rem;
  text-align:left;
  border-bottom:1px solid var(--border-color);
  vertical-align:top;
}
.fleet-page th {
  background:var(--bg-secondary);
  font-weight:600;
  color:#111827;
  border-top:1px solid var(--border-color);
  border-bottom:2px solid var(--border-color);
}
.fleet-page .table-responsive { width:100%; overflow-x:auto; -webkit-overflow-scrolling:touch; }

.fleet-page .finding {
  border-left:4px solid var(--accent);
  background:#f8fafc;
  padding:1rem 1.25rem;
  margin:1.8rem 0;
}
.fleet-page .finding p:last-child { margin-bottom:0; }

.fleet-page .status-grid {
  display:grid;
  grid-template-columns:repeat(3,1fr);
  gap:1rem;
  margin:2rem 0;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
}
.fleet-page .example-strip {
  display:grid;
  grid-template-columns:1fr 1fr 1fr;
  gap:1rem;
  margin:1.5rem 0 2rem;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
}
.fleet-page .example-strip > div {
  border:1px solid var(--border-color);
  border-radius:6px;
  padding:1rem;
  background:#fff;
}
.fleet-page .example-strip strong {
  display:block;
  font-size:.86rem;
  margin-bottom:.35rem;
}
.fleet-page .example-strip code {
  font-size:.82rem;
}
.fleet-page .status-grid > div {
  background:var(--bg-secondary);
  border:1px solid var(--border-color);
  border-radius:6px;
  padding:1rem;
}
.fleet-page .status-grid strong { display:block; font-size:1.5rem; line-height:1.1; margin-bottom:.3rem; }
.fleet-page .status-grid span { display:block; color:var(--text-secondary); font-size:.84rem; line-height:1.4; }

.fleet-page details {
  margin:1rem 0;
  padding:.8rem 0;
  border-top:1px solid var(--border-color);
}
.fleet-page details:last-of-type { border-bottom:1px solid var(--border-color); }
.fleet-page summary {
  cursor:pointer;
  font-weight:600;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
}
.fleet-page details div { margin-top:.85rem; }
.fleet-page .references li { margin-bottom:.65rem; }

@media (max-width:1000px) {
  .fleet-page .layout-wrapper { flex-direction:column; padding:1rem; gap:1rem; }
  .fleet-page .toc-sidebar { flex:none; width:100%; }
  .fleet-page .toc-sticky { position:static; max-height:none; }
  .fleet-page .main-content { max-width:100%; width:100%; }
}
@media (max-width:650px) {
  .fleet-page .status-grid, .fleet-page .example-strip { grid-template-columns:1fr; }
  .fleet-page table { display:block; overflow-x:auto; }
}
</style>

<div class="fleet-page">
  <div class="layout-wrapper">

    <nav class="toc-sidebar">
      <div class="toc-sticky">
        <h3>Contents</h3>
        <ul>
          <li><a href="#tldr">TL;DR</a></li>
          <li><a href="#lineage">1. Research Lineage & Positioning</a></li>
          <li><a href="#benchmark">2. Benchmark Design</a></li>
          <li><a href="#experiment">3. Experimental Design</a></li>
          <li><a href="#status">4. Current Status</a></li>
          <li><a href="#references">5. References</a></li>
        </ul>
      </div>
    </nav>

    <main class="main-content">

      <header>
        <h1>Who Gets to Remember?</h1>
        <p class="subtitle">Shared memory for coding-agent fleets: deciding which experiences become team knowledge, when later agents should see them, and whether those decisions improve real software outcomes.</p>
        <p class="meta">Vedant Borkute · Fleet Mem · Research note · October 2026</p>
      </header>

      <h2 id="tldr" style="margin-top:0;">TL;DR</h2>
      <div class="tldr">
        <p>A coding agent can finish a task with useful experience that is not fully captured by the resulting patch: repository conventions, debugging procedures, failure modes, architectural assumptions, or environment-specific facts. Shared memory offers a way to pass that experience to future agents, but indiscriminate sharing can also preserve stale, redundant, overscoped, or misleading advice.</p>

        <p><strong>Fleet Mem</strong> studies two decisions separately: whether an experience produced by one coding worker should become shared team knowledge before future tasks are known, and whether a later coding worker should be shown that memory for its current task. Both decisions are evaluated using executable repository tests.</p>

        <p>The current benchmark overlays SWE-ContextBench with realistic same-repository histories. Its clean development set contains <strong>11 later tasks with 13–114 earlier candidate experiences each</strong>. The full memory comparison has not yet run; the current stage is validating that known useful memory can measurably change the coding worker’s outcome.</p>
      </div>

      <div class="finding">
        <p><strong>A concrete example.</strong> Suppose an earlier coding agent fixes a filesystem bug and learns: “normalize filesystem paths before comparing cache keys.” That lesson may help a later path-related bug—but a real shared memory also contains competing advice, exceptions, and failed attempts.</p>
      </div>

      <div class="mermaid-like">
        <svg viewBox="0 0 900 525" role="img" aria-label="Illustrative path normalization memory example">
          <defs>
            <marker id="arrow3" markerWidth="8" markerHeight="8" refX="7" refY="3.5" orient="auto">
              <polygon points="0 0, 8 3.5, 0 7" fill="#6b7280"></polygon>
            </marker>
          </defs>

          <rect class="soft-node" x="300" y="25" width="300" height="72" rx="6"/>
          <text class="figure-text" x="450" y="51" text-anchor="middle" font-size="15" font-weight="600">Earlier agent fixes a cache-key bug</text>
          <text class="figure-muted" x="450" y="73" text-anchor="middle" font-size="12">Lesson: normalize filesystem paths before equality checks</text>

          <path class="edge" marker-end="url(#arrow3)" d="M450 97 L450 135"/>

          <text class="figure-text" x="450" y="158" text-anchor="middle" font-size="14" font-weight="600">Repository memory already contains other lessons</text>

          <rect class="accent-node" x="25" y="190" width="158" height="94" rx="6"/>
          <text class="figure-text" x="104" y="216" text-anchor="middle" font-size="12" font-weight="600">Useful</text>
          <text class="figure-muted" x="104" y="237" text-anchor="middle" font-size="10">Normalize filesystem paths</text>
          <text class="figure-muted" x="104" y="253" text-anchor="middle" font-size="10">before cache-key equality</text>

          <rect class="soft-node" x="200" y="190" width="158" height="94" rx="6"/>
          <text class="figure-text" x="279" y="216" text-anchor="middle" font-size="12" font-weight="600">Too broad</text>
          <text class="figure-muted" x="279" y="237" text-anchor="middle" font-size="10">“Normalize every string</text>
          <text class="figure-muted" x="279" y="253" text-anchor="middle" font-size="10">before comparing it”</text>

          <rect class="soft-node" x="375" y="190" width="158" height="94" rx="6"/>
          <text class="figure-text" x="454" y="216" text-anchor="middle" font-size="12" font-weight="600">Exception</text>
          <text class="figure-muted" x="454" y="237" text-anchor="middle" font-size="10">Do not normalize URL paths</text>
          <text class="figure-muted" x="454" y="253" text-anchor="middle" font-size="10">inside the router</text>

          <rect class="soft-node" x="550" y="190" width="158" height="94" rx="6"/>
          <text class="figure-text" x="629" y="216" text-anchor="middle" font-size="12" font-weight="600">Failed attempt</text>
          <text class="figure-muted" x="629" y="237" text-anchor="middle" font-size="10">Lowercase every path</text>
          <text class="figure-muted" x="629" y="253" text-anchor="middle" font-size="10">broke case-sensitive systems</text>

          <rect class="soft-node" x="725" y="190" width="150" height="94" rx="6"/>
          <text class="figure-text" x="800" y="216" text-anchor="middle" font-size="12" font-weight="600">Irrelevant</text>
          <text class="figure-muted" x="800" y="237" text-anchor="middle" font-size="10">Serialization tests require</text>
          <text class="figure-muted" x="800" y="253" text-anchor="middle" font-size="10">sorted dictionary keys</text>

          <path class="edge" marker-end="url(#arrow3)" d="M104 284 C160 325,295 330,365 355"/>
          <path class="edge dashed" marker-end="url(#arrow3)" d="M279 284 C315 315,350 330,395 355"/>
          <path class="edge dashed" marker-end="url(#arrow3)" d="M454 284 L450 355"/>
          <path class="edge dashed" marker-end="url(#arrow3)" d="M629 284 C590 315,550 335,505 355"/>
          <path class="edge dashed" marker-end="url(#arrow3)" d="M800 284 C710 330,610 345,535 365"/>

          <rect class="node" x="300" y="355" width="300" height="72" rx="6"/>
          <text class="figure-text" x="450" y="382" text-anchor="middle" font-size="15" font-weight="600">Later agent: cache invalidation bug</text>
          <text class="figure-muted" x="450" y="404" text-anchor="middle" font-size="11">Which memories should enter its context?</text>

          <path class="edge" marker-end="url(#arrow3)" d="M450 427 L450 463"/>
          <rect class="soft-node" x="322" y="463" width="256" height="42" rx="6"/>
          <text class="figure-text" x="450" y="488" text-anchor="middle" font-size="12" font-weight="600">Repository tests decide whether the choice helped</text>
        </svg>
      </div>
      <div class="figure-caption"><strong>Figure 1:</strong> Illustrative running example. The difficulty is not retrieving one obviously related lesson; it is deciding which memories deserve shared status and which subset a later agent should see. This example is explanatory, not an experimental result.</div>

      <div class="example-strip">
        <div>
          <strong>No memory</strong>
          The later agent solves the bug using only the repository and task description.
        </div>
        <div>
          <strong>Share everything</strong>
          The agent sees the useful path lesson <em>plus</em> the overgeneralization, exception, failed attempt, and irrelevant advice.
        </div>
        <div>
          <strong>Governed memory</strong>
          The system may keep the scoped filesystem lesson while withholding memories that are irrelevant or unsafe for this task.
        </div>
      </div>

      <p>The example also explains why multiple memories matter. With only one known-relevant earlier experience, the benchmark has already solved most of the selection problem. A useful memory governor becomes measurable only when the history contains plausible alternatives that differ in scope, reliability, freshness, and relevance.</p>

      <h2 id="lineage">1. Research Lineage & Positioning</h2>

      <p>The motivating idea predates the current benchmark: instead of treating each coding agent as an isolated worker, a fleet could accumulate <strong>organizational knowledge</strong> across fresh agents. Early formulations used a shared knowledge graph or common memory containing procedures, conventions, fixes, architecture, workflow rules, and other forms of tacit repository knowledge. The scientific question gradually narrowed from “can agents share memory?” to “which experiences deserve to become shared knowledge in the first place?”</p>

      <p>That narrowing was necessary because several neighboring research directions already cover substantial parts of the problem. Shared-memory governance is addressed by work such as GateMem and related governed-memory systems. Coding-agent memory systems such as MemGuard, CODESKILL, and STAIR already study admission, skill-bank maintenance, stale/conflicting memories, and reusable repair knowledge. SWE-ContextBench and VibeMemBench establish that earlier coding experience can help later tasks, while mismatched memory can hurt. Jev-Mem contributes a lightweight System-One controller for bounded memory-management and retrieval decisions.</p>

      <div class="mermaid-like">
        <svg viewBox="0 0 900 690" role="img" aria-label="Fleet Mem research lineage and positioning">
          <defs>
            <marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="3.5" orient="auto">
              <polygon points="0 0, 8 3.5, 0 7" fill="#6b7280"></polygon>
            </marker>
          </defs>

          <g>
            <rect class="soft-node" x="310" y="25" width="280" height="62" rx="6"/>
            <text class="figure-text" x="450" y="51" text-anchor="middle" font-size="16" font-weight="600">Agents reuse past experience</text>
            <text class="figure-muted" x="450" y="72" text-anchor="middle" font-size="12">memory, skills, history, organizational knowledge</text>

            <rect class="node" x="35" y="145" width="185" height="86" rx="6"/>
            <text class="figure-text" x="128" y="170" text-anchor="middle" font-size="14" font-weight="600">Shared-memory governance</text>
            <text class="figure-muted" x="128" y="192" text-anchor="middle" font-size="11">GateMem · governed memory</text>
            <text class="figure-muted" x="128" y="209" text-anchor="middle" font-size="11">who may write / read shared state?</text>

            <rect class="node" x="250" y="145" width="190" height="86" rx="6"/>
            <text class="figure-text" x="345" y="170" text-anchor="middle" font-size="14" font-weight="600">Coding-memory reuse</text>
            <text class="figure-muted" x="345" y="192" text-anchor="middle" font-size="11">SWE-ContextBench · VibeMemBench</text>
            <text class="figure-muted" x="345" y="209" text-anchor="middle" font-size="11">does earlier coding experience help?</text>

            <rect class="node" x="470" y="145" width="190" height="86" rx="6"/>
            <text class="figure-text" x="565" y="170" text-anchor="middle" font-size="14" font-weight="600">Coding-memory control</text>
            <text class="figure-muted" x="565" y="192" text-anchor="middle" font-size="11">MemGuard · CODESKILL · STAIR</text>
            <text class="figure-muted" x="565" y="209" text-anchor="middle" font-size="11">admission, maintenance, stale memory</text>

            <rect class="node" x="690" y="145" width="175" height="86" rx="6"/>
            <text class="figure-text" x="778" y="170" text-anchor="middle" font-size="14" font-weight="600">Fast memory control</text>
            <text class="figure-muted" x="778" y="192" text-anchor="middle" font-size="11">Jev-Mem</text>
            <text class="figure-muted" x="778" y="209" text-anchor="middle" font-size="11">cheap bounded decisions</text>

            <path class="edge" marker-end="url(#arrow)" d="M450 87 C310 112,195 112,128 145"/>
            <path class="edge" marker-end="url(#arrow)" d="M450 87 C400 112,365 120,345 145"/>
            <path class="edge" marker-end="url(#arrow)" d="M450 87 C500 112,535 120,565 145"/>
            <path class="edge" marker-end="url(#arrow)" d="M450 87 C600 112,710 116,778 145"/>

            <rect class="soft-node" x="70" y="310" width="220" height="92" rx="6"/>
            <text class="figure-text" x="180" y="337" text-anchor="middle" font-size="14" font-weight="600">Original project framing</text>
            <text class="figure-muted" x="180" y="359" text-anchor="middle" font-size="11">shared knowledge graph →</text>
            <text class="figure-muted" x="180" y="376" text-anchor="middle" font-size="11">organizational knowledge across fresh agents</text>

            <rect class="soft-node" x="340" y="310" width="220" height="92" rx="6"/>
            <text class="figure-text" x="450" y="337" text-anchor="middle" font-size="14" font-weight="600">Governance question</text>
            <text class="figure-muted" x="450" y="359" text-anchor="middle" font-size="11">which worker experiences should</text>
            <text class="figure-muted" x="450" y="376" text-anchor="middle" font-size="11">become trusted team knowledge?</text>

            <rect class="soft-node" x="610" y="310" width="220" height="92" rx="6"/>
            <text class="figure-text" x="720" y="337" text-anchor="middle" font-size="14" font-weight="600">ChainSWE experiment</text>
            <text class="figure-muted" x="720" y="359" text-anchor="middle" font-size="11">sequential maintenance looked realistic</text>
            <text class="figure-muted" x="720" y="376" text-anchor="middle" font-size="11">but repo state already carried memory</text>

            <path class="edge" marker-end="url(#arrow)" d="M180 402 C220 430,350 430,405 460"/>
            <path class="edge" marker-end="url(#arrow)" d="M450 402 L450 460"/>
            <path class="edge dashed" marker-end="url(#arrow)" d="M720 402 C670 430,555 438,505 460"/>

            <rect class="accent-node" x="280" y="460" width="340" height="112" rx="7"/>
            <text class="figure-text" x="450" y="489" text-anchor="middle" font-size="17" font-weight="700">Fleet Mem</text>
            <text class="figure-text" x="450" y="514" text-anchor="middle" font-size="13" font-weight="600">repository-scoped shared memory for coding-agent fleets</text>
            <text class="figure-muted" x="450" y="538" text-anchor="middle" font-size="11">future-blind share decision → shared pool → later show/withhold decision</text>
            <text class="figure-muted" x="450" y="556" text-anchor="middle" font-size="11">paired executable outcomes on later software tasks</text>

            <path class="edge" marker-end="url(#arrow)" d="M128 231 C170 280,285 420,350 460"/>
            <path class="edge" marker-end="url(#arrow)" d="M345 231 C365 300,405 405,425 460"/>
            <path class="edge" marker-end="url(#arrow)" d="M565 231 C545 315,510 410,490 460"/>
            <path class="edge" marker-end="url(#arrow)" d="M778 231 C735 315,620 420,545 460"/>

            <rect class="soft-node" x="260" y="615" width="380" height="52" rx="6"/>
            <text class="figure-text" x="450" y="638" text-anchor="middle" font-size="13" font-weight="600">Where the contribution lies</text>
            <text class="figure-muted" x="450" y="656" text-anchor="middle" font-size="11">not “memory governance” broadly, but controlled cross-worker sharing + later exposure + executable evaluation</text>
            <path class="edge" marker-end="url(#arrow)" d="M450 572 L450 615"/>
          </g>
        </svg>
      </div>
      <div class="figure-caption"><strong>Figure 2:</strong> Research lineage and the position of Fleet Mem. The project sits at the intersection of shared-memory governance, coding-experience reuse, coding-memory lifecycle work, and lightweight memory control.</div>

      <p>The project’s own trajectory follows the same convergence. It began with a broad shared-knowledge-graph idea for fresh agent generations, then focused on coding fleets because repository work exposes concrete procedural knowledge and executable outcomes. Questions of stale knowledge, revocation, scope, conflict, and promotion became central as the related-work landscape filled in. The remaining useful question was no longer whether agents can have shared memory, but <strong>what should cross the boundary from one worker’s experience into organizational memory, and how should later workers be exposed to it?</strong></p>

      <p>Jev fits naturally as a controller for this question, but not as the novelty claim. Its bounded decision interface is attractive because organizational-memory control is largely a sequence of small decisions rather than a free-form generation problem. The scientific contribution should therefore survive a controller swap: Jev can be compared with deterministic rules and a stronger deliberative LLM under the same interface.</p>

      <h3>Why ChainSWE was not sufficient</h3>

      <p>ChainSWE initially appeared ideal because tasks occur sequentially and later agents inherit an evolving repository. In practice, that persistence made explicit textual memory difficult to isolate: much of the useful information had already been institutionalized in code, tests, and repository state.</p>

      <div class="status-grid">
        <div><strong>14 / 36</strong><span>No shared memory</span></div>
        <div><strong>12 / 36</strong><span>Share all memories</span></div>
        <div><strong>12 / 36</strong><span>Governed condition</span></div>
      </div>

      <p>More importantly, only seven of the 36 targets contained multiple candidate memories. Most extracted memories were close to restatements of code, and clear conflict or supersession cases were rare. The comparison therefore offered little room for a memory governor to express a meaningful policy.</p>

      <div class="finding">
        <p><strong>Benchmark lesson.</strong> A realistic sequence of tasks is not enough. The benchmark must expose a later worker to a non-trivial history of plausible earlier experiences while keeping the useful relationship hidden from the memory controller.</p>
      </div>

      <h2 id="benchmark">2. Benchmark Design</h2>

      <p>The current benchmark returns to SWE-ContextBench, but changes how its experience relationships are used. The original benchmark contains earlier coding experiences and later related tasks with executable evaluation. In Fleet Mem, the known source-to-target relationship is retained only as hidden metadata. It no longer selects the memory that a later worker receives.</p>

      <p>For each later task, all eligible earlier experiences from the same repository are collected into a historical pool. The current clean development set contains <strong>11 later tasks with 13–114 earlier candidates each</strong>. The memory system must therefore operate over a realistic set of alternatives rather than one preselected helpful source.</p>

      <div class="mermaid-like">
        <svg viewBox="0 0 840 330" role="img" aria-label="Pairwise versus repository-history benchmark">
          <defs>
            <marker id="arrow2" markerWidth="8" markerHeight="8" refX="7" refY="3.5" orient="auto">
              <polygon points="0 0, 8 3.5, 0 7" fill="#6b7280"></polygon>
            </marker>
          </defs>
          <g>
            <rect class="soft-node" x="35" y="45" width="310" height="220" rx="6"/>
            <text class="figure-text" x="190" y="76" text-anchor="middle" font-size="15" font-weight="600">Pairwise transfer</text>
            <circle class="node" cx="120" cy="145" r="34"/>
            <circle class="node" cx="260" cy="195" r="34"/>
            <text class="figure-muted" x="120" y="150" text-anchor="middle" font-size="11">known source</text>
            <text class="figure-muted" x="260" y="200" text-anchor="middle" font-size="11">later task</text>
            <path class="edge" marker-end="url(#arrow2)" d="M153 157 L228 184"/>

            <rect class="soft-node" x="495" y="45" width="310" height="220" rx="6"/>
            <text class="figure-text" x="650" y="76" text-anchor="middle" font-size="15" font-weight="600">Fleet Mem history</text>
            <circle class="node" cx="555" cy="125" r="18"/>
            <circle class="node" cx="615" cy="165" r="18"/>
            <circle class="node" cx="565" cy="215" r="18"/>
            <circle class="node" cx="680" cy="118" r="18"/>
            <circle class="node" cx="700" cy="190" r="18"/>
            <circle class="node" cx="630" cy="235" r="18"/>
            <circle class="accent-node" cx="755" cy="228" r="28"/>
            <path class="edge dashed" marker-end="url(#arrow2)" d="M700 190 C725 200,735 210,748 217"/>
            <text class="figure-muted" x="650" y="291" text-anchor="middle" font-size="11">13–114 earlier same-repository experiences</text>
          </g>
        </svg>
      </div>
      <div class="figure-caption"><strong>Figure 3:</strong> SWE-ContextBench’s known relation becomes hidden evaluation metadata; the live system sees the full eligible repository history instead.</div>

      <p>The benchmark also enforces a strict temporal boundary. When an earlier experience is converted into a candidate memory, neither the extractor nor the share decision may see the future task, hidden tests, reference patch, later commits, or the eventual effect of the memory. The share decision is made once when the experience is produced and applies to all future tasks.</p>

      <p>A parallel construction using SWE-rebench V2 tested whether a more natural benchmark could be built directly from repository histories. That pilot produced 48 later tasks across 12 repositories, 226 earlier episodes, and 600 history links, with pools ranging from 2 to 75 predecessors. History richness was strong, but relation quality and evaluator readiness were not: chronology relied on issue or PR creation time, natural useful links were difficult to establish, and only one of 48 later tasks passed both no-fix and reference-fix evaluator controls. SWE-rebench therefore remains a follow-up path rather than the current primary benchmark.</p>

      <div class="table-responsive">
        <table>
          <thead>
            <tr><th>Benchmark</th><th>Strength</th><th>Limitation for Fleet Mem</th><th>Role</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>ChainSWE</strong></td><td>Sequential repository maintenance</td><td>Repository state already carries much of the history; few targets have competing memories</td><td>Secondary evidence</td></tr>
            <tr><td><strong>SWE-ContextBench + history overlay</strong></td><td>Executable tasks, known useful links, non-trivial same-repo histories</td><td>Constructed history rather than a complete naturally observed organization</td><td><strong>Primary benchmark</strong></td></tr>
            <tr><td><strong>SWE-rebench V2</strong></td><td>Richer natural histories</td><td>Weak relation evidence, imperfect chronology, 1/48 fully evaluator-validated</td><td>Follow-up</td></tr>
            <tr><td><strong>VibeMemBench</strong></td><td>Large historical pools with verified useful experiences</td><td>Better suited to memory-use evaluation than future-blind sharing decisions</td><td>Related work / later validation</td></tr>
          </tbody>
        </table>
      </div>

      <h2 id="experiment">3. Experimental Design</h2>

      <p>The main experiment separates the decision made when a memory is created from the decision made when a later task arrives. This distinction is important because an experience may be reasonable to preserve globally but irrelevant to a particular future task.</p>

      <p>The primary write action is simply <strong>share / do not share</strong>. Earlier formulations used reject / keep local / share, but local and rejected memories are experimentally equivalent when workers do not persist across tasks. The target-time action is <strong>show / withhold</strong>. More directive states such as “advisory” or “rely” are avoided because they would change how the coding worker is instructed, confounding memory selection with memory authority.</p>

      <div class="table-responsive">
        <table>
          <thead><tr><th>Condition</th><th>What reaches the coding worker</th><th>Purpose</th></tr></thead>
          <tbody>
            <tr><td><strong>No memory</strong></td><td>No earlier lessons</td><td>Baseline</td></tr>
            <tr><td><strong>Share everything</strong></td><td>Eligible earlier lessons under a fixed context budget</td><td>Tests indiscriminate sharing</td></tr>
            <tr><td><strong>Random, matched amount</strong></td><td>A random subset matched to the governor by count or token budget</td><td>Separates better selection from simply using less context</td></tr>
            <tr><td><strong>Selective sharing</strong></td><td>Only memories approved before future tasks are known</td><td>Measures the early share decision</td></tr>
            <tr><td><strong>Selective showing</strong></td><td>Broad memory is retained, but only selected items are shown later</td><td>Measures filtering at use time</td></tr>
            <tr><td><strong>Selective sharing + showing</strong></td><td>Both stages are controlled</td><td>Full two-stage system</td></tr>
            <tr><td><strong>Strong reasoning controller</strong></td><td>The same bounded decisions made by a stronger LLM</td><td>Quality, cost, and latency comparison</td></tr>
            <tr><td><strong>Known-relevant experience</strong></td><td>The benchmark’s linked earlier experience is supplied directly</td><td>Checks whether useful memory can move this worker at all</td></tr>
          </tbody>
        </table>
      </div>

      <p>The known-relevant condition is run before the full controller comparison. If deliberately supplying the benchmark’s known useful experience does not change executable outcomes, then the worker–benchmark pair contains too little observable memory signal for a more elaborate governor to recover.</p>

      <p>The candidate-memory extractor is kept separate from the governor. It should capture plausible lessons broadly rather than filtering for only “good” or reusable memories, otherwise extraction would silently perform part of the sharing decision being evaluated.</p>

      <p>The primary outcomes remain software outcomes: task resolution, failing tests fixed, previously passing tests preserved, and positive or negative changes relative to the no-memory condition. The experiment also tracks exposed memory tokens, coding-agent steps and tool calls, latency, and controller cost.</p>

      <h2 id="status">4. Current Status</h2>

      <div class="status-grid">
        <div><strong>11</strong><span>clean later tasks with non-trivial repository histories</span></div>
        <div><strong>13–114</strong><span>earlier same-repository candidates per task</span></div>
        <div><strong>0</strong><span>completed memory-policy conclusions so far</span></div>
      </div>

      <p>The benchmark-construction stage has passed its first structural check. A deterministic smoke test also confirmed that the routing code can produce different memory exposures across all 11 tasks. That smoke run is infrastructure evidence only: the real Jev policy, the stronger reasoning policy, and the full coding-worker comparison have not yet been evaluated.</p>

      <p>The remaining pre-treatment question is worker suitability. The original qualification rule required the coding worker to fully solve at least two of three development tasks. GPT-6 Luna failed that rule, and the failure remains part of the record. Its actual patches, however, showed partial competence rather than a broken harness. On a SymPy task, Luna fixed one of two failing tests but introduced a severe performance regression. On a Django task, it fixed the reported duplicate-column behavior, fixed one of six failing tests, and preserved all 166 previously passing tests.</p>

      <p>This motivated a narrower validation question: not whether the worker is nearly perfect in isolation, but whether it is capable enough for memory to measurably help or hurt. The current sequence is therefore to compare Luna and Sol on the same already-used development tasks, freeze one worker, and then compare no memory against the known-relevant earlier experience. The full governance experiment proceeds only if that simpler comparison establishes a real memory effect.</p>

      <div class="finding">
        <p><strong>Current claim boundary.</strong> Fleet Mem does not yet establish that shared memory improves coding-agent performance. The present evidence establishes a non-trivial benchmark structure, functioning executable evaluation, and a controlled experimental design for measuring the effect once treatment runs begin.</p>
      </div>

      <details>
        <summary>Methodological controls</summary>
        <div>
          <p>The worker and memory policy are not tuned simultaneously. Future-task reference information is never used to write a memory. The share decision is made once before later tasks are known. The later task set remains fixed once treatment outcomes are observed. Empty-patch or broken-harness runs are not interpreted as memory results. The full governance comparison is gated by the known-relevant-experience check.</p>
        </div>
      </details>

      <details>
        <summary>Natural history and stress cases</summary>
        <div>
          <p>The primary benchmark uses naturally occurring repository history. A secondary stress set may emphasize duplicate advice, over-broad memories, failed-source lessons, possible stale or superseded guidance, conflicts, and superficially similar but wrong guidance. Synthetic stress cases are supplementary rather than the main evidence.</p>
        </div>
      </details>

      <details>
        <summary>Already-institutionalized knowledge</summary>
        <div>
          <p>An earlier lesson may already be encoded in implementation, regression tests, documentation, comments, configuration, or CI rules. Such cases are explicitly tracked because declining to create redundant textual memory can be the correct organizational decision.</p>
        </div>
      </details>

      <h2 id="references">5. References</h2>
      <ol class="references">
        <li><a href="https://arxiv.org/abs/2602.08316">SWE-ContextBench</a></li>
        <li><a href="https://arxiv.org/abs/2607.02606">ChainSWE</a></li>
        <li><a href="https://arxiv.org/abs/2609.23570">VibeMemBench</a></li>
        <li><a href="https://arxiv.org/abs/2608.21867">MemGuard</a></li>
        <li><a href="https://arxiv.org/abs/2606.18829">GateMem</a></li>
        <li><a href="https://arxiv.org/pdf/2609.23986">Jev-Mem</a></li>
        <li><a href="https://arxiv.org/abs/2605.25430">CODESKILL</a></li>
        <li><a href="https://arxiv.org/abs/2603.15401">SWE-Skills-Bench</a></li>
        <li><a href="https://huggingface.co/datasets/ZiLaotou/MemCalib">MemCalib</a></li>
        <li><a href="https://github.com/GiulioDER/agent-memory-bench">Agent Memory Bench</a></li>
        <li><a href="https://proceedings.mlr.press/v306/badertdinov26a.html">SWE-rebench V2</a></li>
      </ol>

    </main>
  </div>
</div>
