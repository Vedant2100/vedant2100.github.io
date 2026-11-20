---
layout: single
permalink: /
title: ""
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

<header class="intro">
  <img class="intro__photo" src="/images/profile.jpg" alt="Vedant Borkute" width="132" height="132" fetchpriority="high">
  <div class="intro__text">
    <h1 class="intro__name">Vedant Borkute</h1>
    <p class="intro__role">MS Computer Science, University of California, Riverside</p>
    <p class="intro__links">
      <a href="mailto:vbork001@ucr.edu">Email</a>
      <a href="/files/Vedant_Borkute_Resume.pdf">CV</a>
      <a href="https://github.com/Vedant2100">GitHub</a>
      <a href="https://scholar.google.com/citations?user=PS_CX0AAAAAJ">Scholar</a>
      <a href="https://www.linkedin.com/in/vedant-borkute/">LinkedIn</a>
      <a href="https://x.com/vedant275">X</a>
    </p>
  </div>
</header>

<div class="bio">
  <p>I'm a master's student in Computer Science at the University of California, Riverside, finishing in December 2026. Before that I spent two years as a data scientist at <a href="https://finarb.ai/">Finarb AI</a>, building demand-forecasting systems for pharmaceutical supply chains, and studied Computer Science at Indian Institute of Technology Bombay.</p>
  <p>Most of my recent work is on evaluating LLM agents: what they do when a tool fails ambiguously or a trusted-looking source is wrong, whether notes from past runs actually help them, and how they hold up against prompt injection, which I worked on as a research intern at CompFly AI this summer.</p>
  <p>I'm looking for research engineer and ML engineer roles starting <strong>February 2027</strong>. The quickest way to reach me is email.</p>
</div>

<section class="home-section" id="work" aria-labelledby="work-heading">
  <h2 id="work-heading">Research</h2>
  <ol class="entries">
    <li class="entry">
      <p class="entry__when">Nov 2026, ongoing</p>
      <div class="entry__body">
        <h3>StaleStream</h3>
        <p>Can a small model trained with RL keep a bounded external memory correct across sessions, when facts go stale, arrive out of order, conflict between sources or use aliases? A controlled environment plus GRPO-trained memory writers on Qwen3 models, for CS 258. Results are being re-run with LoRA and three seeds on a fresh test split.</p>
      </div>
    </li>
    <li class="entry">
      <p class="entry__when">Nov 2026</p>
      <div class="entry__body">
        <h3><a href="https://github.com/Vedant2100/trustval">TrustVal</a></h3>
        <p>What does an agent do when a tool call fails ambiguously, such as a payment that commits but returns a timeout? Four containerized tasks each inject one fault and grade the final database state. Across 82+ runs, Claude Haiku 4.5, Sonnet 4.6 and GPT-5.3-Codex sometimes retried without checking and created duplicates; Sonnet 4.6 reported success in four of its five failed runs.</p>
        <p class="entry__links"><a href="https://github.com/Vedant2100/trustval">Code</a><a href="https://github.com/Vedant2100/trustval/blob/main/RESULTS.md">Results</a></p>
      </div>
    </li>
    <li class="entry">
      <p class="entry__when">Nov 2026</p>
      <div class="entry__body">
        <h3><a href="https://github.com/Vedant2100/provenance-bias">Provenance Bias</a></h3>
        <p>Do tool-using agents treat a verified signature as proof that a claim is true? In 96 recorded episodes with Qwen2.5-7B, verified origin metadata cut false trust from 83% to 33%, but also cut legitimate task completion from 50% to 20%. Exploratory: one model, one seed.</p>
        <p class="entry__links"><a href="https://github.com/Vedant2100/provenance-bias">Code</a><a href="https://huggingface.co/spaces/Artemis2100/proof-is-not-truth">Demo</a></p>
      </div>
    </li>
    <li class="entry">
      <p class="entry__when">Oct–Nov 2026</p>
      <div class="entry__body">
        <h3><a href="https://github.com/Vedant2100/frontiermemory-learning">Does memory help coding agents?</a></h3>
        <p>An audit of the FrontierMemory benchmark using its own pipeline with a local open model. Memory distilled from about 750 past runs gave no measurable gain over no memory (+0.01 tasks solved per task, p = 0.50, preregistered), with one exception: the Word2Vec task, which a placebo of the same shape did not help.</p>
        <p class="entry__links"><a href="https://github.com/Vedant2100/frontiermemory-learning">Code</a><a href="https://github.com/Vedant2100/frontiermemory-learning/blob/main/FINAL-RESULTS.md">Results</a></p>
      </div>
    </li>
    <li class="entry">
      <p class="entry__when">Spring 2026</p>
      <div class="entry__body">
        <h3><a href="https://github.com/Vedant2100/w26/tree/main/CS_228">LLM reasoning strategies for navigation</a></h3>
        <p>A controlled comparison of Reactive, ReAct, Chain-of-Thought, Tree-of-Thought and Buffer-of-Thought agents in MiniGrid with Qwen2.5-7B-Instruct, tracking success, exploration and token cost. Best results: 55% success on LavaGapS6 and 20% on LavaCrossingS9N2. Advised by Prof. Yinglun Zhu.</p>
        <p class="entry__links"><a href="https://github.com/Vedant2100/w26/tree/main/CS_228">Code</a></p>
      </div>
    </li>
    <li class="entry">
      <p class="entry__when">Spring 2026</p>
      <div class="entry__body">
        <h3><a href="/concept-erasure-analysis/">Concept erasure under stress</a></h3>
        <p>Concept-erasure methods from ESD to SPEED, tested for rank saturation, collateral damage to nearby concepts, and evasion by paraphrased prompts in text-to-image diffusion models. Course project for EE 243.</p>
        <p class="entry__links"><a href="/concept-erasure-analysis/">Write-up</a></p>
      </div>
    </li>
  </ol>
</section>

<section class="home-section" id="experience" aria-labelledby="experience-heading">
  <h2 id="experience-heading">Experience</h2>
  <ol class="entries">
    <li class="entry">
      <p class="entry__when">Jun–Sep 2026</p>
      <div class="entry__body">
        <h3>Research intern, CompFly AI</h3>
        <p>Built a benchmark harness for agent governance controls covering AgentDojo prompt-injection attacks and ToolEmu high-stakes tool use; benchmarked small transformer classifiers for prompt-injection detection; extended OpenTelemetry tracing across agent turns, tool calls and handoffs.</p>
        <p class="entry__links"><a href="https://compfly.ai/resources/blog/agentdojo">Blog post</a></p>
      </div>
    </li>
    <li class="entry">
      <p class="entry__when">2023–2025</p>
      <div class="entry__body">
        <h3>Data scientist, Finarb AI</h3>
        <p>Demand forecasting for pharmaceutical supply chains, from SARIMA and Prophet to LSTMs and TCNs, cutting MAPE by 90% against the moving-average baselines in use. Also built LLM agents for feature research and natural-language queries across databases.</p>
        <p class="entry__links"><a href="https://www.businesswire.com/news/home/20240205191469/en/Golden-State-Medical-Supply-GSMS-selects-Finarb-Analytics-Consulting-as-its-trusted-Partner-for-AI-enabled-Demand-Forecasting-for-their-generics-business">Business impact</a></p>
      </div>
    </li>
  </ol>
  <p class="section-more"><a href="/timeline/">Full timeline</a></p>
</section>

<section class="home-section" id="projects" aria-labelledby="projects-heading">
  <h2 id="projects-heading">Other projects</h2>
  <ul class="index">
    <li><a href="https://github.com/Vedant2100/straightshot">Study Loop</a> <span>A tutor in a single chat that builds an interactive workspace for whatever you want to learn and rewrites its teaching playbook from your results.</span></li>
    <li><a href="https://github.com/Vedant2100/terminal_dreamgym">Terminal DreamGym</a> <span>Turns a terminal agent's failures into practice tasks, then checks recovery on held-out ones.</span></li>
    <li><a href="https://github.com/Vedant2100/CS226-Final-Project">Vegetation anomaly pipeline</a> <span>Satellite imagery, PySpark and PostGIS for early signs of pine-beetle damage (CS 226, <a href="https://github.com/Vedant2100/CS226---Project-Report">report</a>).</span></li>
    <li><a href="https://github.com/Vedant2100/image-realiser">Image-realiser</a> <span>CLIP-based detector and purifier for synthetic-image artifacts, with Grad-CAM explanations.</span></li>
    <li><a href="https://github.com/Vedant2100/symreg">LM-JEPA for symbolic regression</a> <span>A reduced-size LM-JEPA that writes expressions in binary prefix notation (ML4SCI screening task).</span></li>
    <li><a href="https://github.com/Vedant2100/EE269-Presentation">LLM safety and interpretability</a> <span>Paper presentation on four recent papers for EE 269 with Prof. Yinglun Zhu.</span></li>
  </ul>
</section>

<section class="home-section" id="blog" aria-labelledby="blog-heading">
  <h2 id="blog-heading">Blog</h2>
  <ul class="index index--dated">
    {% for post in site.posts %}{% assign year = post.date | date: "%Y" | plus: 0 %}{% if year >= 2026 and post.date <= site.time and post.sitemap != false %}
    <li><time datetime="{{ post.date | date: '%Y-%m-%d' }}">{{ post.date | date: "%b %Y" }}</time> <a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}{% endfor %}
  </ul>
</section>

<section class="home-section" id="misc" aria-labelledby="misc-heading">
  <h2 id="misc-heading">Miscellaneous</h2>
  <ul class="index">
    <li>Reader for CS 228 (Deep Learning) with <a href="https://shizhouxing.github.io/">Prof. Zhouxing Shi</a>, University of California, Riverside, Winter 2026.</li>
    <li>Treasurer, Computer Science Graduate Student Association, University of California, Riverside.</li>
    <li>Volunteer, <a href="https://convention.marssociety.org/">International Mars Society Convention 2026</a>, University of Southern California, October 2026.</li>
  </ul>
</section>
