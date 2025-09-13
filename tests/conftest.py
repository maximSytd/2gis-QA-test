import pytest
import pytest_asyncio

from .utils import (
    BASE_URL,
    client_manager,
    get_auth_token,
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
async def async_authorized_client() -> ClientManagerType:
    """Return authorized with token async client."""
    async with client_manager(
        base_url=BASE_URL,
        cookies={
            "token": await get_auth_token(),
        },
    ) as c:
        yield c


@pytest.fixture(scope="function")
def dummy_place() -> FavoritePlaceType:
    """Return dict of dummy favorite place for tests."""
    return FavoritePlaceFactory()
