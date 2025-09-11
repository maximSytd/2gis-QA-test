import httpx
import pytest
import pytest_asyncio

from .utils import (
    BASE_URL,
    AUTH_URL,
    client_manager,
    token_from_response,
    ClientManagerType,
    FavoritePlaceType,
)
from .factories import FavoritePlaceFactory


@pytest.fixture(scope="module")
def anyio_backend() -> str:
    return "asyncio"


@pytest_asyncio.fixture(scope="function")
async def async_client() -> ClientManagerType:
    """Yield httpx async client."""
    async with client_manager(base_url=BASE_URL) as c:
        yield c


@pytest_asyncio.fixture(scope="function")
async def async_authorized_client(
    async_client: httpx.AsyncClient,
) -> httpx.AsyncClient:
    """Return authorized with token async client."""
    response = await async_client.post(AUTH_URL)
    async_client.cookies.set("token", token_from_response(response))
    return async_client


@pytest.fixture(scope="function")
def dummy_place() -> FavoritePlaceType:
    """Return dict of dummy favorite place for tests."""
    return FavoritePlaceFactory()
