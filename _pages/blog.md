---
layout: editorial
permalink: /blog/
title: Blog
description: "Complete archive of technical notes, experiments, research reviews, and project write-ups by Vedant Borkute."
---


<div class="entry-list entry-list--blog">
{% for post in site.posts %}
  <article class="entry">
    <p class="entry__date"><time datetime="{{ post.date | date: '%Y-%m-%d' }}">{{ post.date | date: '%b %-d, %Y' }}</time></p>
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    <p class="entry__links"><a href="{{ post.url | relative_url }}">Read article ↗</a></p>
  </article>
{% endfor %}
</div>
