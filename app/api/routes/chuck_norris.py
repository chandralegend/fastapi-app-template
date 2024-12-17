"""API route for generating random jokes."""

from typing import Optional

from app.core.services.chuck_norris_jokes import get_joke_categories, get_random_joke
from app.schemas.chuck_norris_jokes import (
    JokeCategoriesResponse,
    RandomJokeRequest,
    RandomJokeResponse,
)
from app.utils.auth import verify_api_key

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security.api_key import APIKey

router = APIRouter()


@router.post("/random_joke")
async def random_joke(
    random_joke_request: Optional[RandomJokeRequest] = None,
    api_key: APIKey = Depends(verify_api_key),
) -> RandomJokeResponse:
    """Get a random joke."""
    try:
        joke = (
            get_random_joke(random_joke_request.category)
            if random_joke_request
            else get_random_joke()
        )
        return joke
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/joke_categories")
async def joke_categories(
    api_key: APIKey = Depends(verify_api_key),
) -> JokeCategoriesResponse:
    """Get joke categories."""
    try:
        categories = get_joke_categories()
        return JokeCategoriesResponse(categories=categories)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
