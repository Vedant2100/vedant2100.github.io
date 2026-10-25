---
layout: editorial
permalink: /
title: ""
description: "Vedant Borkute, MS Computer Science at UC Riverside. Research and engineering in AI agents, machine learning, and computer vision."
redirect_from:
  - /about/
  - /about.html
---

<section class="home-intro">
  <div class="home-intro__grid">
    <div>
      <h1>Vedant Borkute<span class="accent-period">.</span></h1>
      <p>I'm completing an MS in Computer Science at UC Riverside (December 2026), after a B.Tech from IIT Bombay. Previously, I worked on agent governance at CompFly AI and forecasting and data science at Finarb AI.</p>
      <p class="home-intro__small">Open to full-time research engineering and ML roles beginning February 2027.</p>
      <nav class="home-intro__links" aria-label="Profiles and contact">
        <a href="https://github.com/Vedant2100" rel="me">GitHub</a>
        <a href="https://www.linkedin.com/in/vedant-borkute/" rel="me">LinkedIn</a>
        <a href="https://scholar.google.com/citations?user=PS_CX0AAAAAJ">Google Scholar</a>
        <a href="mailto:vbork001@ucr.edu">Email</a>
        <a href="{{ '/files/Vedant_Resume_09_26.pdf' | relative_url }}">Resume (PDF)</a>
      </nav>
    </div>
    <div class="home-intro__photo">
      <img src="{{ '/images/profile.jpg' | relative_url }}" alt="Vedant Borkute" width="208" height="220" decoding="async" fetchpriority="high">
    </div>
  </div>
</section>

<section class="editorial-section">
  <div class="section-heading"><h2>Selected projects</h2><a href="{{ '/projects/' | relative_url }}">All projects ↗</a></div>
  <div class="entry-list">
  {% assign featured_projects = site.data.projects | where: "featured", true %}
  {% for project in featured_projects limit: 6 %}
    <article class="entry">
      <h3><a href="{{ project.blog | relative_url }}">{{ project.title }}</a></h3>
      {% if project.code or project.demo %}
      <p class="entry__links">{% if project.code %}<a href="{{ project.code }}">Code</a>{% endif %}{% if project.code and project.demo %} · {% endif %}{% if project.demo %}<a href="{{ project.demo | relative_url }}">Demo</a>{% endif %}</p>
      {% endif %}
    </article>
  {% endfor %}
  </div>
</section>

<section class="editorial-section">
  <div class="section-heading"><h2>Recent writing</h2><a href="{{ '/blog/' | relative_url }}">Full archive ↗</a></div>
  <div class="entry-list">
  {% for post in site.posts limit: 5 %}
    <article class="entry">
      <p class="entry__date"><time datetime="{{ post.date | date: '%Y-%m-%d' }}">{{ post.date | date: '%b %-d, %Y' }}</time></p>
      <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    </article>
  {% endfor %}
  </div>
</section>
<p class="home-contact">For collaborations or opportunities: <a href="mailto:vbork001@ucr.edu">vbork001@ucr.edu</a>.</p>
