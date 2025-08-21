# Machine_Learning_Powered_Credit_Risk_Scoring_System
### Note: This Project is still in its development stage.
## Executive Summary
Credit risk assessment is a critical process in the financial services industry. Inaccurate risk evaluation can lead to significant financial losses due to defaults, while overly conservative models can reduce lending opportunities.
This project delivers a data-driven credit risk scoring model leveraging advanced machine learning techniques to provide accurate, scalable, and explainable risk predictions.

The system is designed for integration into lending workflows, enabling institutions to optimize approval rates while maintaining portfolio quality.

## Business Problem
Traditional credit scoring models often rely on static thresholds and outdated methodologies. These approaches:
- Fail to capture evolving borrower behaviors.
- May introduce bias or inefficiency into lending decisions.
- Struggle with large, high-dimensional datasets.

## Project Objective
The objective of this project is to develop a robust, adaptive model that predicts the likelihood of loan default and outputs an interpretable credit score, reducing default rates while enabling responsible lending growth.

## Dataset Overview
The dataset used in this project contains historical loan records with borrower demographics, loan characteristics, and repayment histories.
Here is the url to the dataset: https://www.kaggle.com/datasets/imsparsh/lending-club-loan-dataset-2007-2011?resource=download 

## Methodology
### 1. Data Collection.
The original dataset contained a total of 111 columns. However, since our goal is to predict risk at the time of loan application, only features that would be known before the loan decision was made and are predictive of a borrower's ability and willingness to pay were selected.

Key feature categories include:

Borrower's profile: annual_inc, emp_length, home_ownership, verification_status, purpose, addr_state.
Loan details: loan_amnt, term, int_rate, installment, grade, sub_grade.
Credit history/behavior: dti, delinq_2yrs, inq_last_6mths, open_acc, pub_rec, revol_bal, revol_util, total_acc.
Target variable: loan_status.

### 2. Data Cleaning.
Handle Missing values
Change wrongly labeled data types into their correct form

### 3. Exploratory Data Analysis.
Risk distribution analysis across borrower segments.
Correlation studies between features and default probability.
The EDA file is available inside the notebook folder

### 4. Feature selection
Select features that are correlated to the target variable and have predictive power.

### 5. Data Preprocessing
Missing value imputation
Outlier detection and handling
Feature encoding and scaling

### 6. Feature Engineering
Debt-to-income ratio adjustments
Aggregated historical repayment metrics
Credit utilization rates

### 7. Model Development
Algorithms evaluated: Logistic Regression, Random Forest, XGBoost, HistGradientBoosting
Hyperparameter tuning.
Imbalance handling via SMOTE and class weighting

### 8. Model Evaluation
Metrics: Accuracy, ROC-AUC, Precision, Recall, F1-Score

### 9. Deployment Strategy
API exposure via Flask/FastAPI for real-time scoring


## Expected Business Impact
Improved Risk Management: Early identification of high-risk applicants.
Operational Efficiency: Automated and scalable credit assessment process.
Regulatory Compliance: Transparent and explainable scoring methodology.

## Technology Stack
Programming Language: Python
Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
Deployment: Flask or FastAPI
Version Control: Git & GitHub

#### More to follow

