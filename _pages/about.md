---
layout: single
permalink: /
title: ""
author_profile: true
description: "Vedant Borkute, MS Computer Science at UC Riverside. Research and engineering in AI agents, machine learning, and computer vision."
redirect_from:
  - /about/
  - /about.html
---

<div class="home-hero">
  <h1>Vedant Borkute</h1>
  <p>I'm completing an MS in Computer Science at UC Riverside (December 2026), after a B.Tech from IIT Bombay. Previously, I worked on agent governance at CompFly AI and forecasting and data science at Finarb AI.</p>
  <p class="home-hero__availability">Open to full-time research engineering and ML roles beginning February 2027.</p>
  <div class="home-hero__actions">
    <a class="btn btn--primary" href="{{ '/projects/' | relative_url }}">Projects</a>
    <a class="btn" href="{{ '/blog/' | relative_url }}">Blog</a>
    <a class="btn" href="{{ '/files/Vedant_Resume_09_26.pdf' | relative_url }}">Resume (PDF)</a>
  </div>
</div>

## Selected projects

<div class="home-grid home-grid--two">
{% assign featured_projects = site.data.projects | where: "featured", true %}
{% for project in featured_projects limit: 6 %}
  <article class="home-card">
    <h3><a href="{{ project.blog | relative_url }}">{{ project.title }}</a></h3>
    <p>{{ project.summary }}</p>
    {% if project.code or project.demo %}
    <p>{% if project.code %}<a href="{{ project.code }}">Code</a>{% endif %}{% if project.code and project.demo %} · {% endif %}{% if project.demo %}<a href="{{ project.demo | relative_url }}">Demo</a>{% endif %}</p>
    {% endif %}
  </article>
{% endfor %}
</div>

[All projects]({{ '/projects/' | relative_url }})

## Recent writing

<div class="home-grid home-grid--two">
{% for post in site.posts limit: 6 %}
  <article class="home-card">
    <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    <p><time datetime="{{ post.date | date: '%Y-%m-%d' }}">{{ post.date | date: '%b %-d, %Y' }}</time></p>
  </article>
{% endfor %}
</div>

[All writing]({{ '/blog/' | relative_url }})
