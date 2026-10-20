---
layout: research
title: "What survives when a model learns something new?"
subtitle: "ReplayGate: a small, reproducible experiment in continual learning, replay, and forgetting"
project_label: "Independent research note · October 2026"
description: "Experiments with online model updates, reservoir replay and memory-based classification using real UCI handwritten digits."
permalink: /posts/continual-agent-learning/
github_url: https://github.com/Vedant2100/role-work-forge-artifacts/tree/main/projects/prime-intellect-continual-memory
demo_url: /replaygate/
research_toc:
  - label: "TL;DR"
    id: tldr
  - label: "1. The question"
    id: question
  - label: "2. Experimental setup"
    id: setup
  - label: "3. Findings"
    id: findings
  - label: "4. Interpretation"
    id: interpretation
  - label: "5. Limitations & next steps"
    id: limitations
---

<h2 id="tldr">TL;DR</h2>

A model can learn a new task and, in the process, lose something it previously knew. We tested this under a simple, controlled sequence of five classification tasks built from **1,797 real handwritten digit images**. An online classifier trained only on the newest task retained just **19.0%** accuracy across all previously seen digit classes at the end. Keeping a small memory of earlier examples changed the outcome: rehearsal achieved **91.3%**, and a retrieval-only memory achieved **93.0%**. These are measured averages across three seeded runs, not illustrative values.

The result is useful as a concrete illustration of *catastrophic forgetting*. It is **not** evidence that the same approaches improve LLMs or coding agents. The purpose here was to examine the retention–adaptation tradeoff before attempting an agent-scale evaluation.

<h2 id="question">1. The question</h2>

Suppose a system works well today, encounters a new task tomorrow, and changes how it behaves. That change might live in its model weights, in a replay buffer used during training, or in an external memory consulted at inference time. All three can help it adapt, but they preserve old abilities in different ways.

The difficulty is that performance on the *latest* task is not a reliable measure of continual learning. A system might score highly on its new task while failing at an old one. To see that failure rather than hide it, we need to evaluate earlier tasks again after each new training stage.

For this first experiment, we deliberately use a small real-world classification setting instead of an expensive agent benchmark. This isolates the question of retention; it does not pretend that classifying digits captures every complication of learning from agent trajectories.

<h2 id="setup">2. Experimental setup</h2>

<h3>2.1 Dataset and task sequence</h3>

The data are the <a href="https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits">UCI Optical Recognition of Handwritten Digits</a> images, loaded through <code>sklearn.datasets.load_digits()</code>. There are 1,797 authentic handwritten examples, each represented by 64 pixel intensities. No synthetic or handwritten-for-this-demo evaluation cases were added.

Each seed has a stratified **75% training / 25% held-out testing** split. The learner sees five tasks in this fixed order:

<div class="table-responsive">
<table>
<thead><tr><th>Stage</th><th>New digit classes</th><th>Classes evaluated afterwards</th></tr></thead>
<tbody>
<tr><td>1</td><td>0, 1</td><td>0–1</td></tr>
<tr><td>2</td><td>2, 3</td><td>0–3</td></tr>
<tr><td>3</td><td>4, 5</td><td>0–5</td></tr>
<tr><td>4</td><td>6, 7</td><td>0–7</td></tr>
<tr><td>5</td><td>8, 9</td><td>0–9</td></tr>
</tbody>
</table>
</div>

<h3>2.2 Three ways to handle past experience</h3>

**Weights only.** A multiclass logistic classifier receives 120 stochastic-gradient minibatch updates per stage, using only examples of the two most recent classes. It has no way to revisit earlier examples. This is our forgetting-prone baseline.

**Reservoir replay.** The classifier gets the same 120 parameter-update steps per stage, but can fill half a minibatch from an online reservoir of at most **160 previously encountered training examples**. The reservoir samples uniformly from experience seen so far. Learning still happens in model weights, while memory supplies rehearsal data.

**Exemplar memory.** A distance-weighted, 3-nearest-neighbor classifier predicts labels using a reservoir of **160 real training examples**. It does not use the same parameter-update process. This makes it a useful *retrieval-only* reference, but not an equal-compute comparison to the other models.

We used seeds **7, 13, and 29** and evaluated every method on that seed's untouched test split. The full <a href="https://github.com/Vedant2100/role-work-forge-artifacts/blob/main/projects/prime-intellect-continual-memory/run.py">Python implementation</a> specifies the data, sampling, training loop, and evaluation procedure.

<h2 id="findings">3. Findings</h2>

<h3>3.1 Learning the new task is not retaining the old ones</h3>

<div class="research-figure">
<svg id="accuracy-chart" viewBox="0 0 800 350" role="img" aria-label="Measured test accuracy across learned tasks after each of five stages. Three lines: weights-only falls from 100% to 19%; replay ends at 91%; retrieval ends at 93%."></svg>
<div class="figure-caption"><strong>Figure 1.</strong> Mean accuracy on held-out examples from all classes seen so far (3 seeds). The plotted points are drawn from the <a href="https://github.com/Vedant2100/role-work-forge-artifacts/blob/main/projects/prime-intellect-continual-memory/results_summary.json">recorded measurements</a>, not invented demonstration values.</div>
</div>

At the final stage, the weight-only model is still good at classifying the new digits, but its accuracy on the first task has dropped to **0%**. This is the central failure the experiment was meant to expose: a high latest-task score can coexist with almost complete loss of earlier ability.

<h3>3.2 Memory changes the retention–adaptation balance</h3>

<div class="table-responsive">
<table>
<thead><tr><th>Final checkpoint, mean of 3 seeds</th><th>All 10 classes</th><th>First task (0–1)</th><th>Latest task (8–9)</th></tr></thead>
<tbody>
<tr><td>Weights only</td><td><strong>18.96%</strong></td><td>0.00%</td><td>96.97%</td></tr>
<tr><td>Reservoir replay</td><td><strong>91.33%</strong></td><td>81.32%</td><td>94.70%</td></tr>
<tr><td>Exemplar retrieval</td><td><strong>92.96%</strong></td><td>99.27%</td><td>79.92%</td></tr>
</tbody>
</table>
</div>

The replay model preserves much more of the first task while learning the final task reasonably well. The retrieval-only system keeps the earliest task almost intact, but scores lower on the newest one. These numbers should not be used to declare a universal winner: the methods have different computational costs and inductive biases.

<h2 id="interpretation">4. Interpretation</h2>

A growing system has at least two separate obligations: **acquire new behavior** and **avoid unnecessary regressions**. The baseline optimizes the first with almost no protection for the second. Replay reintroduces earlier data during adaptation; exemplar retrieval avoids overwriting a learned classifier altogether.

This is a useful reminder for work on continual learning and agent memory, where it is tempting to measure only performance on the latest benchmark. A more complete evaluation should ask what happens to *older* tasks, whether retained information transfers to unseen situations, and what it costs in compute, storage, and inference time.

My separate <a href="/fleet-mem/">coding-agent memory study</a> examines another piece of this problem: whether earlier experiences should be promoted and exposed to later agents. That work produced a negative full-task result under the memory conditions tested. The two studies address related questions, but neither experimentally proves the other.

<h2 id="limitations">5. Limitations and next steps</h2>

There are important boundaries on what this experiment can support:

- The benchmark is handwritten digit recognition, **not an LLM or coding-agent environment**. We do not claim gains for agent autonomy, reasoning or software engineering.
- Three seeds and one set of hyperparameters are not enough to establish an optimal continual-learning policy.
- Class-incremental learning can be particularly unforgiving to an online linear classifier; task design matters.
- Nearest-neighbor memory and SGD training are not compute-matched at inference time. High retrieval accuracy does not settle the systems tradeoff.

The next credible test would use authentic sequential agent tasks or recorded interaction trajectories, with old-task retention, unseen transfer, regression rates and cost tracked under a fixed harness. Until that experiment has been executed, it remains a **research direction**, not a finding.

<p class="evidence-note"><strong>Reproducibility.</strong> See the <a href="https://github.com/Vedant2100/role-work-forge-artifacts/tree/main/projects/prime-intellect-continual-memory">project folder</a> for <code>run.py</code>, the run protocol and environment information, and <a href="https://github.com/Vedant2100/role-work-forge-artifacts/blob/main/projects/prime-intellect-continual-memory/results_summary.json">results_summary.json</a> for the reported measurements. The <a href="/replaygate/">ReplayGate dashboard</a> lets you compare all five stages interactively. It uses the same recorded values.</p>

<section id="references">
<h2>References</h2>
<ol>
<li><a href="https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits">UCI Machine Learning Repository</a>. Optical Recognition of Handwritten Digits.</li>
<li><a href="https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html">scikit-learn documentation</a>. <code>load_digits</code> dataset loader.</li>
<li><a href="https://github.com/Vedant2100/role-work-forge-artifacts/tree/main/projects/prime-intellect-continual-memory">ReplayGate source and run protocol</a>. Independent experiment, October 2026.</li>
<li><a href="https://github.com/Vedant2100/role-work-forge-artifacts/blob/main/projects/prime-intellect-continual-memory/results_summary.json">ReplayGate result record</a>. Three seeded sequential runs and measured stage accuracies.</li>
</ol>
</section>

<script>
(function(){
const svg=document.getElementById('accuracy-chart');if(!svg)return;
const ns='http://www.w3.org/2000/svg';
const curves=[
 {label:'Weights only',v:[1,.58195,.33211,.25691,.18963],c:'#dc2626'},
 {label:'Reservoir replay',v:[1,.98895,.97181,.96777,.91333],c:'#059669'},
 {label:'Exemplar memory',v:[1,.99080,.97794,.97330,.92963],c:'#2563eb'}
];
function elem(t,attrs,text){let el=document.createElementNS(ns,t);for(const k in attrs)el.setAttribute(k,attrs[k]);if(text!==undefined)el.textContent=text;return el;}
const l=65,r=760,top=15,bottom=280,w=r-l,h=bottom-top;
for(let i=0;i<=5;i++){const y=bottom-i*h/5;svg.append(elem('line',{x1:l,y1:y,x2:r,y2:y,stroke:'#e5e7eb','stroke-width':1}));svg.append(elem('text',{x:52,y:y+5,fill:'#4b5563','font-size':13,'text-anchor':'end'},(i*20)+'%'));}
for(let i=0;i<5;i++){let x=l+w*i/4;svg.append(elem('text',{x,y:bottom+28,fill:'#4b5563','font-size':13,'text-anchor':'middle'},'Task '+(i+1)));}
for(const d of curves){svg.append(elem('polyline',{points:d.v.map((a,i)=>(l+w*i/4)+','+(bottom-a*h)).join(' '),stroke:d.c,fill:'none','stroke-width':3,'stroke-linecap':'round'}));d.v.forEach((a,i)=>svg.append(elem('circle',{cx:l+w*i/4,cy:bottom-a*h,r:3.3,fill:d.c})));}
let xx=l;for(const d of curves){svg.append(elem('line',{x1:xx,y1:328,x2:xx+18,y2:328,stroke:d.c,'stroke-width':4}));svg.append(elem('text',{x:xx+25,y:333,fill:'#4b5563','font-size':13},d.label));xx+=d.label==='Exemplar memory'?160:215;}
})();
</script>