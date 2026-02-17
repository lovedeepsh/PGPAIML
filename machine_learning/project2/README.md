# Creating Cohorts of Songs – Course-end Project 2

Simplilearn AI & ML PGP | Spotify Rolling Stones Dataset

## Contents

| File | Description |
|------|-------------|
| `machine_learning_project2` | Project problem statement and objective |
| `1751025244_creating_cohorts_of_songs_problem_statement.docx` | Official problem statement document |
| `Data Dictionary - Creating cohorts of songs.xlsx` | Column/feature definitions for the dataset |
| `rolling_stones_spotify.csv` | Song data with Spotify audio features |
| `song_cohorts_analysis.ipynb` | **Main deliverable** – EDA and cluster analysis (code + outputs for submission) |
| `requirements.txt` | Python dependencies |
| `README.md` | This file |

## Objective

Perform **exploratory data analysis** and **cluster analysis** to create cohorts of songs and understand the factors that define each cohort for better song recommendations.

## How to run (for submission)

1. **Install dependencies** (from this folder):
   ```bash
   pip install -r requirements.txt
   ```

2. **Open and run the notebook**:
   - Open `song_cohorts_analysis.ipynb` in Jupyter Notebook or VS Code.
   - Run all cells (Cell → Run All) so every section has outputs.

3. **Submit**:
   - Submit the **saved notebook** (with all outputs visible) as your project code and outputs.
   - Export to PDF/HTML from Jupyter if required (File → Download as).

## What the notebook does

1. **Load data** – Reads `rolling_stones_spotify.csv` and optionally `Data Dictionary - Creating cohorts of songs.xlsx`.
2. **Data quality** – Missing values and basic statistics.
3. **EDA** – Correlation heatmap, distributions, pairplot of audio features (energy, danceability, acousticness, valence, popularity, etc.).
4. **Clustering** – K-Means on standardized Spotify features; elbow method and silhouette score to choose number of cohorts (k).
5. **Cohort profiles** – Mean features per cohort and bar chart; 2D scatter (energy vs acousticness).
6. **Summary** – Factors that create each cohort (top differentiators vs overall mean) for use in recommendations.

All code and outputs are in one notebook for easy submission.
