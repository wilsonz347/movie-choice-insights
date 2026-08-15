# Movie Recommendation Effectiveness Analysis

An applied analysis of whether movie recommendations **match user expectations** and **lead to subsequent consumption**, using the MovieLens Beliefs Dataset.

## Product Problem

A recommendation system is only useful if its recommendations are relevant to users and ultimately lead to engagement.

This project evaluates recommendation effectiveness from two perspectives:

1. **Expectation alignment** — Does the system predict what users expect to enjoy?
2. **Consumption** — How often are recommended movies subsequently consumed by users?

A third analysis identifies factors associated with subsequent consumption.

## Key Findings

* The recommendation system **overestimates user expectations by 0.80 rating points on average**.
* The average absolute prediction error is **0.87 rating points**.
* Only **6,463 of 1.21M recommendation events (0.53%)** were followed by recorded consumption.
* Higher predicted ratings were associated with slightly lower odds of consumption (**OR = 0.91**, **p = 0.003**).
* Movie popularity and available follow-up time had the strongest associations with recorded consumption.

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
* Ensuring each rating is attributed to at most one recommendation event.
* Producing `expectation_analysis` and `consumption_analysis` datasets.

### 5. Recommendation Effectiveness

Answers the two primary product questions using descriptive and statistical analysis of prediction error and subsequent consumption.

### 6. Controlled Consumption Analysis

Tests which factors are associated with whether users subsequently consume recommended movies, where consumption is measured by a later user rating.

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
│   └── fetch_data.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Why This Analysis Matters

The project separates **what the system predicts users will enjoy** from **whether users subsequently engage with recommended movies**, then identifies which recommendation, user, movie, and timing factors are associated with recorded consumption.

## Limitations & Assumptions

This analysis relies on several assumptions:

1. **Consumption measure:** A rating after a recommendation is treated as consumption. Watching without rating is not observed.

2. **Repeated recommendations:** If a user receives the same movie more than once, a later rating is linked to the most recent recommendation.

3. **Prior consumption:** A rating before a recommendation indicates the user had previously consumed the movie.

4. **User expectations:** The most recent prediction before a recommendation represents the user’s expected rating.

5. **Time-based controls:** Movie popularity, user activity, and prior exposure are calculated using only information available at the recommendation timestamp.

6. **Follow-up time:** Recommendations with more observed time have more opportunity to receive a later rating; the model controls for this.

7. **Interpretation:** Results show associations, not causal effects. Unmeasured factors may still affect consumption.

## Transparency & AI Assistance

LLMs were used as a supporting tool throughout the project, primarily to help structure the analysis outline, clarify methodological considerations, troubleshoot code, and assist with portions of code generation. All analysis decisions, assumptions, code, results, and interpretations were reviewed and validated by the project author.
