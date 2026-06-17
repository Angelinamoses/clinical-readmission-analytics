<div align="center">

# 🏥 Clinical Readmission Analytics

### End-to-End Healthcare Data Analytics using the UCI Diabetes 130-US Hospitals Dataset

An end-to-end healthcare analytics project that explores **hospital readmission patterns**, performs **clinical data preprocessing**, **exploratory data analysis**, **statistical testing**, and **data visualization**, while following reproducible software engineering practices with reusable Python utility modules and automated unit testing.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![Pytest](https://img.shields.io/badge/Pytest-Unit%20Testing-brightgreen?logo=pytest)
![Healthcare](https://img.shields.io/badge/Domain-Healthcare-red)
![License](https://img.shields.io/badge/License-MIT-success)

</div>

---

# 📑 Table of Contents

- Project Overview
- Dataset
- Repository Structure
- Project Workflow
- Analysis Highlights
- Statistical Analysis
- Key Findings
- Visualizations
- Technologies Used
- Installation
- Running Tests
- Clinical Relevance
- Future Improvements
- Author

---

# 🩺 Project Overview

Hospital readmissions are widely recognized as an important quality indicator in healthcare systems. Identifying factors associated with patient readmissions can support hospitals in improving patient outcomes, optimizing healthcare resource utilization, and reducing avoidable costs.

This repository demonstrates a complete healthcare analytics workflow using the **Diabetes 130-US Hospitals Dataset** from the **UCI Machine Learning Repository**.

The project follows a reproducible analytical pipeline consisting of:

- Data Acquisition
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Statistical Analysis
- Clinical Interpretation
- Modular Python Utilities
- Automated Unit Testing

The repository is structured to encourage reusable, maintainable, and production-quality analytical code.

---

# 📊 Dataset

| Property | Description |
|-----------|-------------|
| Dataset | Diabetes 130-US Hospitals |
| Source | UCI Machine Learning Repository |
| Domain | Healthcare Analytics |
| Records | 100,000+ Patient Encounters |
| Features | 50+ Clinical Variables |
| Objective | Analyze hospital readmission patterns |

The dataset contains demographic, diagnostic, medication, laboratory, and healthcare utilization information collected from diabetic patient encounters across multiple hospitals.

---

# 📁 Repository Structure

```text
clinical-readmission-analytics/

│
├── 📓 notebooks/
│     Exploratory analysis notebooks
│
├── 📂 src/
│     ├── data_utils.py
│     ├── plotting_utils.py
│     └── stats_utils.py
│
├── 📊 reports/
│     └── figures/
│
├── 🧪 tests/
│     Unit tests using Pytest
│
├── requirements.txt
│
└── README.md
```

---

# 🔄 Project Workflow

```text
UCI Healthcare Dataset
          │
          ▼
Data Acquisition
          │
          ▼
Data Cleaning
          │
          ▼
Feature Exploration
          │
          ▼
Data Visualization
          │
          ▼
Statistical Testing
          │
          ▼
Clinical Interpretation
```

---

# 🔬 Analysis Highlights

## 📥 Data Acquisition

- Retrieved healthcare dataset directly from the UCI Machine Learning Repository
- Examined dataset metadata
- Reviewed feature descriptions
- Evaluated dataset dimensions and structure

---

## 🧹 Data Cleaning

Performed comprehensive preprocessing including:

- Duplicate record detection
- Missing value assessment
- Removal of low-information features
- Data quality validation
- Clinical interpretation of missingness

---

## 📈 Exploratory Data Analysis

Explored multiple aspects of patient care including:

- Readmission outcomes
- Patient demographics
- Length of hospital stay
- Medication burden
- Prior inpatient utilization
- Emergency visits
- Laboratory procedures
- Diagnostic distributions

---

## 📊 Statistical Analysis

Applied appropriate statistical methods including:

- Mann–Whitney U Test
- Chi-Square Test of Independence
- Distribution comparisons
- Statistical significance testing
- Healthcare variable comparisons

---

## 🩺 Clinical Interpretation

Statistical findings were translated into clinically meaningful observations to better understand potential drivers of hospital readmission.

---

# 📌 Key Findings

## 🏥 Healthcare Utilization

Patients with greater prior inpatient utilization demonstrated different readmission patterns, suggesting previous healthcare utilization may serve as an important indicator of future readmission risk.

---

## ⏳ Length of Stay

Hospital stay duration differed between readmission groups, potentially reflecting greater illness severity and clinical complexity.

---

## 💊 Medication Burden

Patients prescribed larger numbers of medications generally represented more clinically complex cases and demonstrated distinct healthcare utilization patterns.

---

## 🧪 Laboratory Testing

A substantial proportion of laboratory measurements were not performed, emphasizing the importance of interpreting missing healthcare data within its clinical context rather than assuming data quality issues.

---

# 📷 Visualizations

The project includes multiple healthcare-focused visualizations such as:

- Readmission Distribution
- Missing Value Analysis
- Age Distribution
- Length of Stay Analysis
- Medication Distribution
- Correlation Heatmaps
- Laboratory Utilization
- Healthcare Utilization Metrics

> Figures generated throughout the analysis can be found in the `reports/figures/` directory.

---

# ⚙️ Technologies Used

## Programming

- Python

## Data Analysis

- Pandas
- NumPy

## Visualization

- Matplotlib
- Seaborn
- Plotly
- Missingno

## Statistical Analysis

- SciPy
- Statsmodels

## Data Access

- ucimlrepo

## Testing

- Pytest

## Development Environment

- Jupyter Notebook
- VS Code

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Angelinamoses/clinical-readmission-analytics.git
```

Navigate into the project

```bash
cd clinical-readmission-analytics
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🧪 Running Tests

Execute all unit tests using Pytest.

```bash
python -m pytest
```

Expected output

```text
=========================
6 passed
=========================
```

The project currently includes unit tests covering:

- Missing value utilities
- Duplicate detection
- Readmission distribution
- Low variance feature detection
- Additional data utility functions

---

# 💻 Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Core Programming |
| 🐼 Pandas | Data Manipulation |
| 🔢 NumPy | Numerical Computing |
| 📈 Matplotlib | Data Visualization |
| 🎨 Seaborn | Statistical Graphics |
| 📊 Plotly | Interactive Visualizations |
| 📉 SciPy | Statistical Analysis |
| 🧪 Pytest | Automated Testing |
| 📒 Jupyter Notebook | Exploratory Analysis |

---

# 🏥 Clinical Relevance

This repository demonstrates a reproducible healthcare analytics workflow commonly encountered in clinical data science and health informatics.

The project emphasizes:

- Clinical data quality assessment
- Exploratory healthcare analytics
- Statistical validation
- Healthcare utilization analysis
- Reproducible Python workflows
- Modular software design
- Automated testing
- Clinically meaningful interpretation of analytical findings

---

# 🛣️ Future Improvements

Planned extensions include:

- [x] Data Cleaning
- [x] Exploratory Data Analysis
- [x] Statistical Analysis
- [x] Modular Utility Functions
- [x] Automated Unit Testing
- [ ] Logistic Regression Model
- [ ] Random Forest Classifier
- [ ] XGBoost
- [ ] Explainable AI (SHAP)
- [ ] Interactive Dashboard
- [ ] Streamlit Deployment
- [ ] GitHub Actions CI/CD
- [ ] Docker Containerization

---

# 👩‍💻 Author

## Angelina Moses

**M.Sc. Health Informatics**

Aspiring Clinical Machine Learning Engineer

GitHub

https://github.com/Angelinamoses

LinkedIn

www.linkedin.com/in/angel-darla-28511723b

---

<div align="center">

⭐ If you found this project interesting, consider giving it a star!

</div>
