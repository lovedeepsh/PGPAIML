# Lending Club Loan Data Analysis – Course-end Project 2

Simplilearn Deep Learning | Finance domain

## Objective
Create a deep learning model to predict whether a loan will default using Lending Club historical data (2007–2015). Dataset is highly imbalanced.

## Contents
| File | Description |
|------|-------------|
| `deep_learning_project2` | Problem statement |
| `1753780576_project_lending_club_data_analysis.pdf` | Official project document |
| `loan_data.csv` | Lending Club dataset (not.fully.paid: 1=default, 0=repaid) |
| `lending_club_analysis.ipynb` | **Main deliverable** – preprocessing + deep learning model |
| `requirements.txt` | Python dependencies |

## How to run
1. `pip install -r requirements.txt`
2. Open `lending_club_analysis.ipynb` and run all cells.
3. Submit the saved notebook (with outputs).

## What the notebook does
1. Load data and check quality (target distribution, missing values).
2. Preprocess: encode categorical (purpose), fill missing, numeric features only.
3. Train/test split, StandardScaler, SMOTE on training set.
4. Deep learning model (Keras): Dense layers, Dropout, EarlyStopping.
5. Evaluation: accuracy, precision, recall, F1, ROC-AUC, confusion matrix.
