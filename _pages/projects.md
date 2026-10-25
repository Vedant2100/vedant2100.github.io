---
layout: editorial
permalink: /projects/
title: Projects
description: "Projects in AI agents, model evaluation, reinforcement learning, computer vision, and applied machine learning."
---


<div class="entry-list entry-list--projects">
{% for project in site.data.projects %}
  <article class="entry">
    <h2><a href="{{ project.blog | relative_url }}">{{ project.title }}</a></h2>
    {% if project.code or project.demo %}<p class="entry__links">{% if project.code %}<a href="{{ project.code }}">Code</a>{% endif %}{% if project.code and project.demo %} · {% endif %}{% if project.demo %}<a href="{{ project.demo | relative_url }}">Demo</a>{% endif %}</p>{% endif %}
  </article>
{% endfor %}
</div>
