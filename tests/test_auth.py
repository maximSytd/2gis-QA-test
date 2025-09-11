import re

import pytest
import httpx

from .utils import AUTH_URL

@pytest.mark.asyncio
async def test_get_token(async_client: httpx.AsyncClient):
    """Ensure that user can get auth token."""
    response = await async_client.post(AUTH_URL)
    token_match = re.search(
        r"token=([a-f0-9]+);",
        response.headers["Set-Cookie"],
    )
    assert response.status_code == httpx.codes.OK
    assert token_match is not None, response.headers
    assert "Max-Age=2" in response.headers["Set-Cookie"], response.headers
