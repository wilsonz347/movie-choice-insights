# Movie Recommendation Effectiveness Analysis

An applied analysis of whether movie recommendations **match user expectations** and **lead to subsequent consumption**, using the MovieLens Beliefs Dataset.

## Product Problem

A recommendation system is only useful if its recommendations are relevant to users and ultimately lead to engagement.

This project evaluates recommendation effectiveness from two perspectives:

1. **Expectation alignment** — Does the system predict what users expect to enjoy?
2. **Consumption** — Are recommendations associated with users subsequently consuming the recommended movie?

A third analysis extends this by testing whether the observed consumption association remains after controlling for other plausible drivers of consumption.

## Key Findings

* The recommendation system **overestimates user expectations by 0.80 rating points on average**.
* The average absolute prediction error is **0.87 rating points**.
* Only **6,463 of 1.21M recommendation events (0.53%)** were followed by recorded consumption.
* Consumption rates varied little across system predicted-rating ranges, providing limited descriptive evidence that higher predicted ratings translated into higher subsequent consumption.
* Because the data is observational, the analysis focuses on **association rather than causal impact**.

## Analysis

### 1. Data Understanding

Examines dataset structure, relationships between tables, missing values, duplicates, rating histories, timestamp consistency, and data quality.

### 2. Data Preparation

Cleans and standardizes the raw datasets while preserving the longitudinal nature of the rating history.

### 3. Exploratory Data Analysis

Investigates rating behavior, recommendation activity, user expectations, movie characteristics, and temporal patterns.

### 4. Feature Engineering

Constructs recommendation-level analysis tables by:

* Matching each recommendation with the most recent prior user prediction.
* Identifying whether the user had previously consumed the movie.
* Attributing a subsequent rating to the most recent preceding recommendation for the same user–movie pair.
* Preventing repeated rating events from duplicating recommendation events.
* Producing `expectation_analysis` and `consumption_analysis` datasets.

### 5. Recommendation Effectiveness

Answers the two primary product questions using descriptive and statistical analysis of prediction error and subsequent consumption.

### 6. Controlled Consumption Analysis

Tests whether the observed association between recommendation and subsequent consumption persists after controlling for other factors that plausibly influence consumption.

## Data

**Dataset:** MovieLens Beliefs Dataset, 2024 release

Key sources include:

* User belief / expectation data
* Main longitudinal rating history
* Additional rating population
* Recommendation history
* Movie metadata

The main rating history is longitudinal: users can rate the same movie multiple times. Therefore, user–movie pairs are **not treated as unique observations**.

## Technical Stack

* **Data Processing & Visualization:** `pandas`, `matplotlib`
* **Analysis:** descriptive statistics, prediction error metrics, distribution analysis
* **Statistical modeling:** logistic regression using `statsmodels`
* **Version control:** Git

## Repository Structure

```text
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_preparation.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_recommendation_effectiveness_analysis.ipynb
│   └── 06_controlled_consumption_analysis.ipynb
├── scripts/
│   ├── fetch_data.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Why This Analysis Matters

The project separates **what the system predicts users will enjoy** from **whether users actually engage with the recommendation**, then examines whether the observed consumption relationship survives adjustment for other factors.

## Limitations & Assumptions

This analysis relies on several assumptions:

* **Consumption is proxied by a subsequent rating.** A rating after a recommendation is treated as evidence that the user consumed the movie. Watching without subsequently rating the movie is therefore not observed as consumption.
* **Recommendations are event-level observations.** Users may receive multiple recommendations for the same movie. When a rating occurs after multiple recommendations, it is attributed to the most recent preceding recommendation for that user–movie pair.
* **Prior consumption is inferred from rating history.** A valid rating recorded before a recommendation is treated as evidence that the user had previously consumed the movie.
* **User expectations are time-dependent.** The most recent user prediction before each recommendation is used as the user's expected rating at the time of recommendation.
* **The data is observational.** The consumption analysis estimates associations and does not establish that recommendations caused users to consume movies.
* **Unobserved factors may remain.** User preferences, movie availability, timing, exposure, and other behavioral factors may influence consumption but may not be fully captured by the available data.
* **Longitudinal ratings are preserved.** Because users can change their ratings over time, user–movie pairs are not assumed to be unique observations.
* **Unequal observation time:** No fixed time window is used for subsequent consumption. Recommendations made later in a user's rating history have less opportunity to be followed by a recorded rating. 

## Transparency & AI Assistance

LLMs were used as a supporting tool throughout the project, primarily to help structure the analysis outline, clarify methodological considerations, troubleshoot code, and assist with portions of code generation. All analysis decisions, assumptions, code, results, and interpretations were reviewed and validated.
