# Product Review Engine

Turn raw Amazon product reviews into structured, actionable insights using an LLM (Groq API).

For each review the engine extracts:

| Field | Description |
|---|---|
| `sentiment` | Positive / Neutral / Negative |
| `category` | Packaging, Taste & Quality, Price & Value, Delivery & Customer Service, Other |
| `key_insight` | One-sentence summary of the main pain point or praise |
| `actionable_recommendation` | One-sentence suggestion for the brand / product team |

## What's inside

- **Data cleaning** of ~568k reviews: missing values, ~175k duplicate/multi-listing reviews, too-short reviews, inconsistent helpfulness counts, HTML tags.
- **LLM extraction** with a structured JSON prompt and a robust parser (handles code fences and `<think>` blocks).
- **Model comparison** across three Groq-hosted models (speed and output cleanliness).
- A small **CLI** that runs the whole pipeline and saves results to CSV.

## Tech stack

Python 3.12 · pandas · OpenAI SDK (Groq-compatible endpoint) · Jupyter · seaborn / matplotlib · [uv](https://docs.astral.sh/uv/)

## Setup

```bash
# 1. Install dependencies
uv sync

# 2. Add your Groq API key (free at https://console.groq.com)
cp .env.example .env
# then edit .env and set GROQ_API_KEY=...

# 3. Get the data (either option)
#    a) Download Reviews.csv from Kaggle and put it in data/
#       https://www.kaggle.com/datasets/arhamrumi/amazon-product-reviews
#    b) Do nothing: the CLI downloads it automatically via kagglehub
```

## Usage

```bash
# Check that your API key works
uv run python scripts/check_api.py

# Analyse 50 random cleaned reviews and save to results/insights.csv
uv run product-review-engine -n 50

# Explore step by step
uv run jupyter lab notebooks/project.ipynb
```

## Project structure

```
src/product_review_engine/
  config.py    # API client + model config (reads .env)
  data.py      # load + clean the dataset
  insights.py  # prompt, LLM call, JSON parsing/validation
  cli.py       # command line pipeline
notebooks/project.ipynb   # exploration, cleaning, model comparison
scripts/check_api.py      # API sanity check
```

## Model comparison (3 reviews, informal)

| Model | Latency | Notes |
|---|---|---|
| openai/gpt-oss-20b | ~0.3-0.4 s | Fastest, clean JSON |
| groq/compound | ~1.5-6.5 s | Valid JSON, variable latency |
| qwen/qwen3.6-27b | ~2-3 s | Prints reasoning before the JSON, needs extra parsing |

This is a small sample, so treat it as a first impression rather than a rigorous benchmark.

## Next steps

- Run on a larger sample and visualise sentiment/category distributions per product.
- Validate LLM sentiment against the star `Score` column.
- Add retries/rate-limit handling and batch requests.
