"""Schemas for Chuck Norris jokes."""

from typing import Optional

from app.models.joke import RandomJoke as RandomJokeResponse

from pydantic import BaseModel


class RandomJokeRequest(BaseModel):
    """Random joke request model."""

    category: Optional[str] = None


class JokeCategoriesResponse(BaseModel):
    """Joke categories response model."""

    categories: list[str]


__all__ = [
    "RandomJokeRequest",
    "RandomJokeResponse",
    "JokeCategoriesResponse",
]
