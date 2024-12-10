"""Chuck Norris Jokes Service."""

from typing import Optional

from app.core.config import CHUCK_NORRIS_API_URL
from app.models.joke import RandomJoke

import requests


def get_random_joke(category: Optional[str] = None) -> RandomJoke:
    """Get a random joke."""
    url = (
        f"{CHUCK_NORRIS_API_URL}/random?category={category}"
        if category
        else f"{CHUCK_NORRIS_API_URL}/random"
    )
    response = requests.get(url)
    response.raise_for_status()
    category = (
        response.json()["categories"][0]
        if len(response.json()["categories"]) > 0
        else "N/A"
    )
    return RandomJoke(
        id=response.json()["id"], category=category, joke=response.json()["value"]
    )


def get_joke_categories() -> list[str]:
    """Get joke categories."""
    url = f"{CHUCK_NORRIS_API_URL}/categories"
    response = requests.get(url)
    response.raise_for_status()
    categories = response.json()
    assert isinstance(categories, list), "Something went wrong"
    return categories
