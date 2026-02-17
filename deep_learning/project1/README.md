# Home Loan Data Analysis – Course-end Project 1

Simplilearn Deep Learning | Finance domain

## Objective
Create a deep learning model to predict whether an applicant will repay a loan using historical data. Dataset is highly imbalanced.

## Contents
| File | Description |
|------|-------------|
| `deep_learning_project1` | Problem statement |
| `1753780327_project_home_loan_data_analysis.pdf` | Official project document |
| `loan_data (1).csv` | Home loan dataset (TARGET: 1=repaid, 0=default) |
| `Data_Dictionary.csv` | Column definitions |
| `home_loan_analysis.ipynb` | **Main deliverable** – preprocessing + deep learning model |
| `requirements.txt` | Python dependencies |

## How to run
1. `pip install -r requirements.txt`
2. Open `home_loan_analysis.ipynb` and run all cells.
3. Submit the saved notebook (with outputs).

## What the notebook does
1. Load data and check quality (missing values, target distribution).
2. Preprocess: drop ID, drop columns with >50% missing, fill missing, label-encode categoricals.
3. Train/test split, StandardScaler, SMOTE on training set.
4. Deep learning model (Keras): Dense layers, Dropout, EarlyStopping.
5. Evaluation: accuracy, precision, recall, F1, ROC-AUC, confusion matrix.
