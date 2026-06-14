# Clinical Readmission Analytics 🏥📊

A healthcare analytics project investigating factors associated with hospital readmissions among diabetic patients using real-world hospital encounter data.

---

## Project Overview

Hospital readmissions are an important quality-of-care and cost-related challenge for healthcare systems. Understanding the factors associated with readmission can help healthcare organizations identify high-risk patients and improve post-discharge care strategies.

This project analyzes over 100,000 hospital encounters from diabetic patients to explore demographic, clinical, and healthcare utilization patterns associated with readmission outcomes.

The analysis follows a complete healthcare analytics workflow including data acquisition, data cleaning, exploratory data analysis, statistical testing, and clinical interpretation.

---

## Dataset

**Source:** UCI Machine Learning Repository

**Dataset:** Diabetes 130-US Hospitals for Years 1999–2008

### Dataset Summary

| Metric             | Value                 |
| ------------------ | --------------------- |
| Patient Encounters | 101,766               |
| Hospitals          | 130                   |
| Features           | 48                    |
| Domain             | Healthcare / Diabetes |
| Outcome Variable   | Readmission Status    |

The dataset was accessed programmatically using the `ucimlrepo` package.

---

## Project Workflow

```text
Data Acquisition
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Statistical Analysis
        ↓
Clinical Insights
```

---

## Repository Structure

```text
clinical-readmission-analytics/

├── notebooks/
│   ├── 01_data_acquisition.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_exploratory_analysis.ipynb
│   ├── 04_statistical_analysis.ipynb
│   └── 05_clinical_insights.ipynb
│
├── data/
│   └── cleaned_diabetes_readmission.csv
│
├── reports/
│   └── summary_report.md
│
├── requirements.txt
└── README.md
```

---

## Analysis Highlights

### Data Acquisition

* Retrieved healthcare dataset directly from UCI
* Examined metadata and feature descriptions
* Assessed dataset dimensions and structure

### Data Cleaning

* Evaluated duplicate records
* Investigated missing values
* Removed low-information variables
* Handled clinically meaningful missingness

### Exploratory Data Analysis

Explored:

* Readmission outcomes
* Demographic distributions
* Length of stay
* Medication burden
* Prior healthcare utilization
* Laboratory measurements

### Statistical Analysis

Applied:

* Mann-Whitney U Tests
* Chi-Square Tests
* Group comparisons
* Significance testing

### Clinical Interpretation

Translated statistical findings into healthcare-focused insights and recommendations.

---

## Key Findings

### Healthcare Utilization

Patients with higher prior inpatient utilization demonstrated different readmission patterns, suggesting previous healthcare utilization may be an important indicator of future readmission risk.

### Length of Stay

Hospital stay duration showed meaningful differences between readmission groups, potentially reflecting differences in patient complexity and illness severity.

### Medication Burden

Patients receiving larger numbers of medications may represent more clinically complex cases and demonstrated distinct utilization patterns.

### Laboratory Testing

A substantial proportion of laboratory measurements were not performed, highlighting the importance of understanding healthcare data missingness within its clinical context.

---

## Technologies Used

### Data Processing

* Python
* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn
* Plotly
* Missingno

### Statistical Analysis

* SciPy
* Statsmodels

### Data Access

* ucimlrepo

---

## Clinical Relevance

This project demonstrates an end-to-end healthcare analytics workflow and highlights how clinical, demographic, and utilization-related variables can be investigated to better understand hospital readmission patterns.

The analysis emphasizes the importance of:

* Data quality assessment
* Healthcare utilization metrics
* Statistical validation
* Clinical interpretation

when working with real-world healthcare datasets.

---

## Future Work

Potential future extensions include:

* Readmission risk prediction models
* Logistic Regression
* Random Forest Classification
* Explainable AI (XAI)
* Clinical Risk Scoring Systems
* Interactive Healthcare Dashboards

---

## Author

**Angelina Moses**

Master's Student in Health Informatics

Interested in Healthcare Analytics, Clinical Machine Learning, and Data-Driven Healthcare Innovation.
