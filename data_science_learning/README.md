# Data Science Learning

A collection of self-study notebooks covering data visualisation, exploratory data analysis and machine learning fundamentals.

## Notebooks

| Folder | Notebook | Topics |
|---|---|---|
| `visualisation-exercises` | `visualisation_exercises.ipynb` | Histograms, KDE, box plots, violin plots, scatter, heatmap, bar charts, time series, interactive Plotly charts |
| `gdp-analysis` | `gdp_life_expectancy.ipynb` | Gapminder EDA: GDP per capita and life expectancy trends, correlations, historical anomalies, 3D development paths |
| `child-mortality` | `child_mortality_life_expectancy.ipynb` | Child mortality (1800–2024): data reshaping with melt, dual-axis trend chart, scatter by milestone year, crisis impact, top gainers |
| `titanic` | `titanic_survival_analysis.ipynb` | Survival analysis: feature engineering (family size), 2×2 dashboard with bar, violin and heatmap |
| `ml-fundamentals` | `ml_linear_regression.ipynb` | Exercises 1–12: simple and multiple regression, train/test split, MAE/MSE/RMSE/R², VIF, overfitting, Ridge, Lasso |

## Data

| File | Source |
|---|---|
| `gapminder.csv` | [Gapminder](https://www.gapminder.org/data/) — country-level GDP, life expectancy, population (1952–2007) |
| `lex.csv` | Gapminder — life expectancy by country (1800–2024) |
| `child_mortality_0_5_year_olds_dying_per_1000_born.csv` | Gapminder — child mortality by country (1800–2024) |

## Setup

```bash
# Install dependencies (using uv)
uv sync

# Or with pip
pip install jupyter matplotlib numpy pandas plotly scikit-learn seaborn statsmodels

# Launch Jupyter
jupyter lab
```

## Figures

The `figures/` directory contains the four charts from the child mortality analysis, also saved automatically when you run that notebook.

## Tech stack

Python 3.12 · NumPy · Pandas · Matplotlib · Seaborn · Plotly Express · scikit-learn · statsmodels · Jupyter
