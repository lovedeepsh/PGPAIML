# Employee Turnover Analytics – Course-end Project 1

Simplilearn AI & ML PGP | Portobello Tech HR Dataset

## Contents

| File | Description |
|------|-------------|
| `machine_learning_project1` | Project problem statement and requirements |
| `HR_comma_sep.csv` | HR dataset (satisfaction, evaluation, projects, hours, turnover, etc.) |
| `1751024678_employee_turnover_problem_statement.docx` | Official problem statement document |
| `employee_turnover_analysis.ipynb` | **Main deliverable** – full analysis (code + outputs for submission) |
| `requirements.txt` | Python dependencies |
| `README.md` | This file |

## How to run (for submission)

1. **Install dependencies** (from this folder):
   ```bash
   pip install -r requirements.txt
   ```

2. **Open and run the notebook**:
   - Open `employee_turnover_analysis.ipynb` in Jupyter Notebook or VS Code.
   - Run all cells (Cell → Run All) so that every section has outputs.

3. **Submit**:
   - Submit the **saved notebook** (with all outputs visible) as your project code and outputs.
   - You can also export to PDF/HTML from Jupyter if required (File → Download as).

## What the notebook does

1. **Data quality checks** – Loads `HR_comma_sep.csv`, checks missing values.
2. **EDA** – Factors contributing to turnover (correlations, salary/department, satisfaction/tenure/hours).
3. **Clustering** – K-means on employees who left (satisfaction vs evaluation).
4. **SMOTE** – Handles class imbalance on the training set.
5. **K-fold CV** – Stratified 5-fold cross-validation for Logistic Regression, Random Forest, Gradient Boosting.
6. **Best model** – Compares metrics (Accuracy, Precision, Recall, F1, ROC-AUC) and justifies choice (e.g. F1/ROC-AUC for imbalanced target).
7. **Retention strategies** – Targeted recommendations based on EDA and model (satisfaction, tenure, salary, promotions, department).

All code and outputs are in one notebook for easy submission.
