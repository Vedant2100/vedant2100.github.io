---
layout: editorial
permalink: /
title: ""
description: "Vedant Borkute — AI research engineer working on agents, memory, evaluation, and dependable machine learning."
redirect_from:
  - /about/
  - /about.html
---

<section class="home-intro">
  <p class="editorial-kicker">AI RESEARCH ENGINEERING · UC RIVERSIDE</p>
  <h1>Vedant Borkute<span class="accent-period">.</span></h1>
  <p class="home-intro__lead">I work on making intelligent systems more reliable: agent memory and evaluation, AI safety, computer vision, and applied machine learning.</p>
  <p>I'm completing an MS in Computer Science at UC Riverside (December 2026), after a B.Tech from IIT Bombay. Previously, I worked on agent governance at CompFly AI and forecasting and data science at Finarb AI.</p>
  <p class="home-intro__small">Open to full-time research engineering and ML roles beginning February 2027.</p>
  <p class="home-intro__links"><a href="{{ '/projects/' | relative_url }}">Explore projects ↗</a><a href="{{ '/blog/' | relative_url }}">Read the blog ↗</a><a href="{{ '/files/Vedant_Resume_09_26.pdf' | relative_url }}">Resume (PDF) ↗</a></p>
</section>

<section class="editorial-section">
  <div class="section-heading"><h2>Selected projects</h2><a href="{{ '/projects/' | relative_url }}">All projects ↗</a></div>
  <div class="entry-list">
  {% assign featured_projects = site.data.projects | where: "featured", true %}
  {% for project in featured_projects limit: 6 %}
    <article class="entry">
      <p class="entry__meta">{{ project.area }}</p>
      <h3><a href="{{ project.blog | relative_url }}">{{ project.title }}</a></h3>
      <p>{{ project.summary }}</p>
      <p class="entry__links"><a href="{{ project.blog | relative_url }}">Technical write-up ↗</a>{% if project.code %} · <a href="{{ project.code }}">Code / artifact ↗</a>{% endif %}</p>
    </article>
  {% endfor %}
  </div>
</section>

<section class="editorial-section">
  <div class="section-heading"><h2>Recent writing</h2><a href="{{ '/blog/' | relative_url }}">Full archive ↗</a></div>
  <div class="entry-list">
  {% for post in site.posts limit: 5 %}
    <article class="entry">
      <p class="entry__meta">{{ post.date | date: '%b %-d, %Y' }}{% if post.tags.size > 0 %} · {{ post.tags | first }}{% endif %}</p>
      <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      {% if post.description %}<p>{{ post.description }}</p>{% endif %}
    </article>
  {% endfor %}
  </div>
</section>
<p class="home-contact">For collaborations or opportunities: <a href="mailto:vbork001@ucr.edu">vbork001@ucr.edu</a>.</p>
