from typing import Generator

from app.main import app

from fastapi.testclient import TestClient

import pytest


@pytest.fixture(scope="module")
def test_client() -> Generator:
    client = TestClient(app)
    yield client
