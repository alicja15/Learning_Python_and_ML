"""Command line entry point: clean reviews, sample N, extract insights, save to CSV."""

import argparse
from pathlib import Path

import pandas as pd

from .config import get_client, get_model
from .data import clean_reviews, load_reviews
from .insights import extract_review_insights


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract insights from Amazon reviews with an LLM.")
    parser.add_argument("-n", "--sample-size", type=int, default=50, help="Number of reviews to analyse")
    parser.add_argument("--csv", type=Path, default=None, help="Path to Reviews.csv (optional)")
    parser.add_argument("--out", type=Path, default=Path("results/insights.csv"), help="Output CSV path")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    client, model = get_client(), get_model()

    df = clean_reviews(load_reviews(args.csv))
    print(f"Cleaned dataset: {len(df):,} reviews")
    sample = df.sample(n=args.sample_size, random_state=args.seed).reset_index(drop=True)

    rows = []
    for i, row in sample.iterrows():
        print(f"[{i + 1}/{len(sample)}] {row['Summary'][:60]}")
        rows.append(extract_review_insights(client, model, row["Summary"], row["Text"]))

    result = pd.concat([sample[["Id", "ProductId", "Score", "Summary", "Text"]], pd.DataFrame(rows)], axis=1)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(args.out, index=False)

    print(f"\nSaved {len(result)} rows to {args.out}")
    print(result["sentiment"].value_counts().to_string())


if __name__ == "__main__":
    main()
