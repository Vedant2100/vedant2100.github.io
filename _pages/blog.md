---
layout: editorial
permalink: /blog/
title: Blog
description: "Complete archive of technical notes, experiments, research reviews, and project write-ups by Vedant Borkute."
---

Research notes, experiments, and project write-ups. The archive includes work in progress and negative results; I try to separate measured findings from hypotheses.

<div class="entry-list entry-list--blog">
{% for post in site.posts %}
  <article class="entry">
    <p class="entry__meta"><time datetime="{{ post.date | date: '%Y-%m-%d' }}">{{ post.date | date: '%b %-d, %Y' }}</time>{% if post.tags.size > 0 %} · {{ post.tags | join: ', ' }}{% endif %}</p>
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    {% if post.description %}<p>{{ post.description }}</p>{% elsif post.excerpt %}<p>{{ post.excerpt | strip_html | truncatewords: 24 }}</p>{% endif %}
    <p class="entry__links"><a href="{{ post.url | relative_url }}">Read article ↗</a></p>
  </article>
{% endfor %}
</div>
