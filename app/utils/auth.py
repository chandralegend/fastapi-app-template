"""This module contains the utility functions for authentication."""

from fastapi import HTTPException


async def verify_api_key(api_key: str) -> None:
    """Verify the API Key passed in the request header."""
    if api_key != "expected_api_key":
        raise HTTPException(status_code=403, detail="Invalid API Key")
