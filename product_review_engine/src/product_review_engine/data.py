"""Loading and cleaning the Kaggle Amazon product reviews dataset."""

from pathlib import Path

import pandas as pd

KAGGLE_DATASET = "arhamrumi/amazon-product-reviews"
LOCAL_CSV = Path("data") / "Reviews.csv"


def load_reviews(path: str | Path | None = None) -> pd.DataFrame:
    """Load Reviews.csv from `path`, from data/Reviews.csv, or download it via kagglehub."""
    if path is None:
        if LOCAL_CSV.exists():
            path = LOCAL_CSV
        else:
            import kagglehub

            path = Path(kagglehub.dataset_download(KAGGLE_DATASET)) / "Reviews.csv"
    return pd.read_csv(path)


def clean_reviews(df: pd.DataFrame) -> pd.DataFrame:
    """Apply the cleaning steps explored in the notebook."""
    out = df.dropna(subset=["Summary"]).copy()
    out["ProfileName"] = out["ProfileName"].fillna("Anonymous_User")

    # Remove repeated/multi-listing reviews (same user, time and text)
    out = out.drop_duplicates(subset=["UserId", "Time", "Text"], keep="first")

    # Drop very short reviews that give the LLM no context
    out = out[out["Text"].str.len() > 20]

    # Known dataset bug: numerator greater than denominator
    out = out[out["HelpfulnessNumerator"] <= out["HelpfulnessDenominator"]]

    # Strip HTML line breaks
    for col in ("Text", "Summary"):
        out[col] = out[col].str.replace(r"<br\s*/?>", " ", regex=True)

    return out.reset_index(drop=True)
