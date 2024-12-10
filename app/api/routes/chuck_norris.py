"""API route for generating random jokes."""

from typing import Optional

from app.core.services.chuck_norris_jokes import get_joke_categories, get_random_joke
from app.schemas.chuck_norris_jokes import (
    JokeCategoriesResponse,
    RandomJokeRequest,
    RandomJokeResponse,
)
from app.utils.auth import verify_api_key

from fastapi import APIRouter, HTTPException, Header

router = APIRouter()


@router.post("/random_joke")
async def random_joke(
    random_joke_request: Optional[RandomJokeRequest] = None,
    api_key: str = Header(..., alias="x-api-key"),
) -> RandomJokeResponse:
    """Get a random joke."""
    await verify_api_key(api_key)
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
    api_key: str = Header(..., alias="x-api-key"),
) -> JokeCategoriesResponse:
    """Get joke categories."""
    await verify_api_key(api_key)
    try:
        categories = get_joke_categories()
        return JokeCategoriesResponse(categories=categories)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
