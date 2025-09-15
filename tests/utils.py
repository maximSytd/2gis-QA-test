import typing
import datetime
from contextlib import asynccontextmanager

import httpx
import httpx_retries

from .factories import COLOR_CHOICES

BASE_URL = "https://regions-test.2gis.com"
AUTH_URL = "/v1/auth/tokens"
FAVORITES_URL = "/v1/favorites"
REQUEST_TIMEOUT_SEC = 3
MAX_RETRIES = 3
RETRY_BACKOFF = 0.5

UNAUTHORIZED_ERR_MSG = "Параметр 'token' является обязательным"
TITLE_ERR_MSG = "Параметр 'title' должен содержать не более 999 символов"
LAT_LESS_ERR_MSG = "Параметр 'lat' должен быть не менее -90"
LAT_MORE_ERR_MSG = "Параметр 'lat' должен быть не более 90"
LON_LESS_ERR_MSG = "Параметр 'lon' должен быть не менее -180"
LON_MORE_ERR_MSG = "Параметр 'lon' должен быть не более 180"
COLOR_ERR_MSG = (
    "Параметр 'color' может быть одним из следующих "
    f"значений: {", ".join(COLOR_CHOICES)}"
)


ClientManagerType = typing.AsyncGenerator[httpx.AsyncClient, None]
FavoritePlaceType = dict[str, str | int]

@asynccontextmanager
async def client_manager(base_url: str, **kw) -> ClientManagerType:
    """Yield httpx async client."""
    transport = httpx_retries.RetryTransport(
        retry=httpx_retries.Retry(
            total=MAX_RETRIES,
            backoff_factor=RETRY_BACKOFF,
        ),
    )
    async with httpx.AsyncClient(
        base_url=base_url,
        transport=transport,
        timeout=REQUEST_TIMEOUT_SEC,
        **kw,
    ) as c:
        yield c


def token_from_response(response: httpx.Response) -> str:
    """Return token from auth response headers."""
    set_cookie_header = response.headers.get("Set-Cookie", "")
    token_part = set_cookie_header.split("token=")[1]
    return token_part.split(";")[0]


async def get_auth_token() -> str:
    """Return token string from auth request headers."""
    async with client_manager(base_url=BASE_URL) as client:
        response = await client.post(AUTH_URL)
        return token_from_response(response)


def is_iso8601_date_string(date_string: str) -> bool:
    """Return bool and check if date string have correct iso format."""
    try:
        datetime.datetime.fromisoformat(date_string.replace("Z", "+00:00"))
        return True
    except (ValueError, TypeError):
        return False
