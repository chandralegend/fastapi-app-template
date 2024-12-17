"""Main module to run the FastAPI application."""

from app.api.routes import chuck_norris

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Chuck Norris Jokes API",
    description="An API to generate random Chuck Norris jokes.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chuck_norris.router)


@app.get("/")
async def read_root() -> dict:
    """Health check."""
    return {"Status": "OK"}
