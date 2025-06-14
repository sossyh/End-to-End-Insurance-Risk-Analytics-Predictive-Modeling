# End-to-End-Insurance-Risk-Analytics-Predictive-Modeling

# Insurance Risk Analysis and Pricing ML Project

This project develops a robust, reproducible, and interpretable machine learning pipeline for risk analysis and premium optimization in the insurance domain. It is broken down into four key tasks focused on Exploratory Data Analysis (EDA), data versioning, statistical testing, and predictive modeling.

---

## 📁 Project Structure

End-to-End-Insurance-Risk-Analytics-Predictive-Modeling/
├── data/ # Raw, processed, and external data

│ ├── raw/

│ ├── processed/

│ └── external/

├── notebooks/ # EDA, statistical testing, modeling notebooks

├── src/ # Scripts for data prep, analysis, modeling

├── outputs/ # Visualizations and reports

│ ├── figures/

│ └── reports/

├── logs/ # Logs for data processing and modeling

├── tests/ # Unit tests for pipeline components

├── .github/workflows/ # CI/CD configuration (GitHub Actions)

├── .dvc/ # DVC metadata

├── requirements.txt # Python dependencies

├── environment.yml # Conda environment file (optional)

├── .gitignore

├── README.md

└── LICENSE


---


### 🔹 Git, GitHub, and EDA

- Initialize Git repo and setup GitHub Actions CI.
- Perform detailed Exploratory Data Analysis (EDA) to:
  - Understand distributions, outliers, and trends.
  - Compute KPIs like Loss Ratio.
  - Identify correlations between financial variables and demographics.
- Visualize 3 key insights from the data.


---

### 🔹Reproducibility with DVC

- Install and configure Data Version Control (DVC).
- Set up local remote for dataset tracking.
- Version raw data and push to remote.
- Maintain clean Git-DVC integration for full traceability of data changes.


---

### 🔹Statistical Hypothesis Testing

- Validate or reject null hypotheses such as:
  - No risk differences across provinces or gender.
  - No margin difference between zip codes.
- Conduct statistical tests (e.g., t-test, chi-squared) on key metrics:
  - Claim Frequency
  - Claim Severity
  - Margin
- Translate results into actionable business insights.


---

### 🔹 Predictive Modeling

- Build models for:
  - **Claim Severity Prediction** (Regression)
  - **Premium Prediction** (Business-guided regression)
  - **Claim Probability** (Classification)
- Train and evaluate:
  - Linear Regression
  - Random Forest
  - XGBoost
- Interpret models using SHAP or LIME.
- Report top features influencing predictions.


---

## 🔧 Setup Instructions

### 1. Clone the Repo

git clone https://github.com/sossyh/End-to-End-Insurance-Risk-Analytics-Predictive-Modeling.git
cd End-to-End-Insurance-Risk-Analytics-Predictive-Modeling
---

### 2. Create a Virtual Environment


python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

###  Visuals and Reports
outputs/
├── figures/       # Charts and visualizations
└── reports/       # Statistical summaries, hypothesis tests

### Data Versioning with DVC

dvc init
dvc remote add -d localstorage /path/to/local/storage
dvc add data/raw/insurance.csv
git add data/.gitignore insurance.csv.dvc
git commit -m "Track insurance dataset with DVC"
dvc push
