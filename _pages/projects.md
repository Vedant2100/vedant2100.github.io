---
layout: editorial
permalink: /projects/
title: Projects
description: "Research experiments, shipped systems, and technical investigations. Every project links to its own write-up."
---

A working index of my research and engineering projects. Each entry links to a technical note documenting the problem, approach, available evidence, and limitations. Code and live artifacts are linked where public.

<div class="entry-list entry-list--projects">
{% for project in site.data.projects %}
  <article class="entry">
    <p class="entry__meta">{{ project.area }}</p>
    <h2><a href="{{ project.blog | relative_url }}">{{ project.title }}</a></h2>
    <p>{{ project.summary }}</p>
    <p class="entry__links"><a href="{{ project.blog | relative_url }}">Read the project write-up ↗</a>{% if project.code %} · <a href="{{ project.code }}">Source / artifact ↗</a>{% endif %}{% if project.demo %} · <a href="{{ project.demo | relative_url }}">Demo ↗</a>{% endif %}</p>
  </article>
{% endfor %}
</div>
