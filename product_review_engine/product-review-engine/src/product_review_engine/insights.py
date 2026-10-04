"""LLM-based extraction of structured insights from a single review."""

import json
import re

SENTIMENTS = {"Positive", "Neutral", "Negative"}
CATEGORIES = {
    "Packaging",
    "Taste & Quality",
    "Price & Value",
    "Delivery & Customer Service",
    "Other",
}
ERROR_RESULT = {
    "sentiment": "Error",
    "category": "Error",
    "key_insight": "Error",
    "actionable_recommendation": "Error",
}

PROMPT = """You are an FMCG Consumer Insights Specialist.
Analyze the customer review below and extract key commercial insights.

Review Title/Summary: {summary}
Review Body: {text}

Return ONLY a valid JSON object with the following keys:
- "sentiment": Exactly one of ["Positive", "Neutral", "Negative"]
- "category": Choose the most relevant category from ["Packaging", "Taste & Quality", "Price & Value", "Delivery & Customer Service", "Other"]
- "key_insight": A concise 1-sentence summary of the main customer pain point or praise.
- "actionable_recommendation": A short 1-sentence recommendation for the brand or product management team.
"""


def parse_json_response(raw: str) -> dict:
    """Parse JSON from a model reply, tolerating <think> blocks, code fences and extra prose."""
    raw = re.sub(r"<think>.*?</think>", "", raw, flags=re.DOTALL).strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", raw, flags=re.DOTALL)
        if match:
            return json.loads(match.group(0))
        raise


def extract_review_insights(client, model: str, summary: str, text: str) -> dict:
    """Return sentiment, category, key insight and recommendation for one review."""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful business analytics AI that outputs only raw JSON.",
                },
                {"role": "user", "content": PROMPT.format(summary=summary, text=text)},
            ],
            temperature=0.2,
        )
        result = parse_json_response(response.choices[0].message.content)
    except Exception as exc:  # network, rate limit, bad JSON...
        print(f"API/parse error: {exc}")
        return dict(ERROR_RESULT)

    if result.get("sentiment") not in SENTIMENTS:
        result["sentiment"] = "Error"
    if result.get("category") not in CATEGORIES:
        result["category"] = "Other"
    return result
