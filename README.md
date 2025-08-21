# Psychedelic Experience Report Summarization

This repository contains code, preprocessing scripts, and evaluation materials for the paper: **"Unsupervised Automatic Summarization of Psychedelic User Experience Reports"**

## Overview

We developed and evaluated unsupervised extractive summarization methods for 1,200 narrative reports of LSD, psilocybin, and DMT experiences sourced from **Erowid**. The goal is to preserve **experiential depth** and **clinical relevance** while improving readability and accessibility for research use.

## Key Contributions

* **Corpus construction**: 1,200 Erowid trip reports (balanced across substances)
* **Preprocessing pipeline**: cleaning, segmentation, and **NER-based de-identification** to remove any residual personal identifiers
* **Models compared**:
   * LexRank
   * LSA + HDBSCAN clustering
   * SBERT + Maximal Marginal Relevance (MMR)
* **Custom scoring function**: combines semantic coverage, narrative coherence, and experiential preservation
* **Evaluation**: GPT-4 rubric-based rating + multi-criteria aggregation using TOPSIS

## Results

* **LexRank** achieved the best overall balance across metrics
* **SBERT+MMR** excelled in experiential richness but showed coherence challenges
* Trade-offs highlight the complexity of summarizing verbose psychedelic reports

## Ethics & Data

* Reports are **publicly available** on Erowid and cannot be redistributed
* We provide preprocessing scripts, and evaluation code only
* Study deemed **exempt from IRB review** under institutional guidelines

## Repository Structure

```
├── data scrapers/  # Scrapy Library based code for data collection
├── notebooks/      # Text cleaning, Summarization pipelines, Custom scoring, LLM rubric evaluation, Radar Chart Visualization, and TOPSIS aggregation
└── results/        # LLM Score, Hyperparameter Selections, One representative example
```


For inquiries, please contact [badhon279@gmail.com]
