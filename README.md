# ITNPA4-34-Assessments-2026-
The repository researchly-trend-tracker is organised so each numbered section of the assignment maps to a corresponding notebook and artifact folder.

# Researchly Trend Tracker

A prototype NLP pipeline that classifies research abstracts and
discovers thematic structure in a research corpus, built for the
Researchly screening tool.

## Contents

| Section | Notebook | Deliverable |
|---------|----------|-------------|
| Q1.1–Q1.3 | `notebooks/01_abstracts_classification.ipynb` | Denoised DataFrame, baseline classifier, performance report |
| Q2.1–Q2.2 | `notebooks/01_abstracts_classification.ipynb` (Part II) | Four ML models + ensemble enhancement |
| Q3.1–Q3.4 | `notebooks/02_corpus_topic_modelling.ipynb` | Corpus DataFrame, summarisations + visualisations |
| Q4.1–Q4.2 | `notebooks/02_corpus_topic_modelling.ipynb` (Part II) | LDA model, pyLDAvis interactive map |
| Q4.3 | `deployment/` + `reports/Researchly_Report.pdf` | Production deployment of Q1/Q2 + full documentation |

## Quickstart

    git clone https://github.com/<user>/researchly-trend-tracker.git
    cd researchly-trend-tracker
    pip install -r requirements.txt
    jupyter lab notebooks/

## Deployment

See `deployment/README.md` for step-by-step instructions for local,
Docker, and HuggingFace Spaces deployment of the abstract classifier.

## Reproducibility

All randomness is seeded (`random_state=42`); notebooks run
top-to-bottom from the checked-in raw data in `data/raw/`.
