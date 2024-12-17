"""This module contains the utility functions for authentication."""

from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader


async def verify_api_key(
    api_key_header: str = Security(APIKeyHeader(name="x-api-key", auto_error=False))
) -> str:
    """Verify the API Key passed in the request header."""
    if api_key_header != "expected_api_key":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key"
        )
    return api_key_header
