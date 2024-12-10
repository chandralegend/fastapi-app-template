"""Model for jokes."""

from pydantic import BaseModel


class RandomJoke(BaseModel):
    """Random joke model."""

    id: str
    category: str
    joke: str
