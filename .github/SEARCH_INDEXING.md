# Search indexing handoff

The GitHub Pages deployment remains on `master`; this PR does not publish the branch or grant anyone access to Google Search Console.

## Already handled in this branch

- Canonical URLs from `_includes/seo.html` using `site.url` and each page permalink
- Correct `repository` and `url` in `_config.yml`
- Real `Person` and post-level `BlogPosting` JSON-LD metadata
- Descriptive titles/metadata on the homepage, indexes, and technical articles
- Root `robots.txt` linking to the automatically generated `sitemap.xml`
- Internal links from homepage to projects, project write-ups, and the complete post index
- Retirement of inherited Academic Pages demo articles, fake publications, and sample portfolio items

## Required after merging / deployment (manual account access)

1. Open https://search.google.com/search-console and add URL-prefix property **https://vedant2100.github.io/** (unless it is already verified).
2. Choose HTML-tag verification and copy the **content** value of the Google verification meta tag into `google_site_verification` in `_config.yml`. Deploy and click Verify. Alternatively, use an ownership method supported by Google.
3. Open **Sitemaps** in Search Console and submit **https://vedant2100.github.io/sitemap.xml**.
4. Use URL Inspection on the homepage, /projects/, /blog/, and a sample of the new article URLs. Request indexing where appropriate and monitor the Pages report for crawl or indexing issues.
5. Confirm the deployed `robots.txt` and `sitemap.xml` resolve publicly and that the canonical URLs use https://vedant2100.github.io/ with no extra project prefix.

Google may crawl or index pages at its discretion. Deploying a sitemap and requesting indexing do **not** guarantee ranking or inclusion.

Guidance:
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl
