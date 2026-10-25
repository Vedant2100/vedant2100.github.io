---
layout: editorial
permalink: /projects/
title: Projects
description: "Research experiments, shipped systems, and technical investigations. Every project links to its own write-up."
---


<div class="entry-list entry-list--projects">
{% for project in site.data.projects %}
  <article class="entry">
    <h2><a href="{{ project.blog | relative_url }}">{{ project.title }}</a></h2>
    <p class="entry__links"><a href="{{ project.blog | relative_url }}">Read the project write-up ↗</a>{% if project.code %} · <a href="{{ project.code }}">Source / artifact ↗</a>{% endif %}{% if project.demo %} · <a href="{{ project.demo | relative_url }}">Demo ↗</a>{% endif %}</p>
  </article>
{% endfor %}
</div>
