---
layout: editorial
title: "Vegetation anomalies before forest disease outbreaks"
description: "Satellite-imagery transformation and evaluation for a cloud-native vegetation stress pipeline."
date: 2026-10-25
permalink: /blog/vegetation-anomaly-pipeline/
tags: [data-engineering, geospatial, evaluation]
---

[Source](https://github.com/Vedant2100/CS226-Final-Project)

## The question

Can changes in satellite vegetation indices be used to spot stress before a visible plant-health event? A useful investigation needs repeatable image ingestion, spatial indexing, time-aware baselines, and a way to inspect false alarms.

## Approach

Our **CS226 team project** combined Sentinel-2/Landsat scenes, Cloud Optimized GeoTIFFs in S3, PostgreSQL/PostGIS, PySpark, NDVI/NDMI transformations, Z-score anomalies, and a Flask/Leaflet dashboard. **My documented contributions** were early dataset-source research, exploratory timelapses, establishing project and report structure, implementing parts of data transformation and evaluation, producing tables/run metadata, and coordinating integration. Other team members led ingestion, the UI, and Z-score thresholding; the [README credits each contributor](https://github.com/Vedant2100/CS226-Final-Project).

## Evidence and results

The team report discusses indexed-query gains of roughly **15–25×** and an anomaly-detection recall figure around **71%** in its evaluated setup. These are team-level results, not personal sole-authorship claims. Consult the [project report](https://github.com/Vedant2100/CS226---Project-Report) for data and measurement assumptions.

## Limitations

Vegetation stress is not uniquely attributable to one disease or pest; cloud artifacts, seasons, forest masking, and study-area selection affect the signal.

[← Back to all projects](/projects/)
