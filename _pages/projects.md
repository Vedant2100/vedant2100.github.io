---
layout: single
permalink: /projects/
title: Projects
author_profile: true
description: "Projects in AI agents, model evaluation, reinforcement learning, computer vision, and applied machine learning."
---

<div class="home-grid home-grid--two">
{% for project in site.data.projects %}
  <article class="home-card">
    <h3><a href="{{ project.blog | relative_url }}">{{ project.title }}</a></h3>
    <p>{{ project.summary }}</p>
    {% if project.code or project.demo %}
    <p>{% if project.code %}<a href="{{ project.code }}">Code</a>{% endif %}{% if project.code and project.demo %} · {% endif %}{% if project.demo %}<a href="{{ project.demo | relative_url }}">Demo</a>{% endif %}</p>
    {% endif %}
  </article>
{% endfor %}
</div>
