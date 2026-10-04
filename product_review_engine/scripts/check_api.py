"""Check that your Groq key works: lists available models and runs one tiny request.

Usage: uv run python scripts/check_api.py
"""

from product_review_engine.config import get_client, get_model


def main() -> None:
    client = get_client()
    try:
        models = [m.id for m in client.models.list().data]
        print("Available models:", models)
        response = client.chat.completions.create(
            model=get_model(),
            messages=[{"role": "user", "content": "Extract sentiment from this review: 'Great build quality!'"}],
        )
        print("AI response:", response.choices[0].message.content)
    except Exception as exc:
        print("API error:", exc)


if __name__ == "__main__":
    main()
