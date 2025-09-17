import pytest
import httpx

from .utils import (
    UNAUTHORIZED_ERR_MSG,
    TITLE_ERR_MSG,
    LAT_LESS_ERR_MSG,
    LAT_MORE_ERR_MSG,
    LON_LESS_ERR_MSG,
    LON_MORE_ERR_MSG,
    COLOR_ERR_MSG,
    FAVORITES_URL,
    FavoritePlaceType,
    is_iso8601_date_string,
)

@pytest.mark.asyncio
async def test_post_favorite(
    async_authorized_client: httpx.AsyncClient,
    dummy_place: FavoritePlaceType,
):
    """Ensure that user can create favorite place."""
    response = await async_authorized_client.post(
        FAVORITES_URL,
        data=dummy_place,
    )
    response_body = response.json()
    assert response.status_code == httpx.codes.OK, response_body
    assert isinstance(response_body["id"], int)
    assert response_body["title"] == dummy_place["title"]
    assert response_body["lat"] == round(float(dummy_place["lat"]), 6)
    assert response_body["lon"] == round(float(dummy_place["lon"]), 6)
    assert response_body["color"] == dummy_place["color"]
    assert is_iso8601_date_string(response_body["created_at"])


@pytest.mark.parametrize(
    argnames="field, value, err_msg",
    argvalues=[
        [
            "title", "*" * 1001, TITLE_ERR_MSG,
        ],
        [
            "lat", -90.000001, LAT_LESS_ERR_MSG,
        ],
        [
            "lat", 90.000001, LAT_MORE_ERR_MSG,
        ],
        [
            "lon", -180.000001, LON_LESS_ERR_MSG,
        ],
        [
            "lon", 181.000001, LON_MORE_ERR_MSG,
        ],
        [
            "color", "black", COLOR_ERR_MSG,
        ],
    ],
)
@pytest.mark.asyncio
async def test_invalid_field_data_post_favorite(
    async_authorized_client: httpx.AsyncClient,
    dummy_place: FavoritePlaceType,
    field: str,
    value: str | int,
    err_msg: str,
):
    """Ensure that user can't create favorite place with invalid data."""
    dummy_place[field] = value
    response = await async_authorized_client.post(
        FAVORITES_URL,
        data=dummy_place,
    )
    response_body = response.json()
    assert response.status_code == httpx.codes.BAD_REQUEST, response_body
    assert err_msg == response_body["error"]["message"], value
    assert response_body["error"]["id"]


@pytest.mark.asyncio
async def test_unauthorized_post_favorite(
    async_client: httpx.AsyncClient,
    dummy_place: FavoritePlaceType,
):
    """Ensure that unauthorized user can't create favorite places."""
    response = await async_client.post(
        FAVORITES_URL,
        data=dummy_place,
    )
    response_body = response.json()
    assert response.status_code == httpx.codes.UNAUTHORIZED, response_body
    assert response_body["error"]["message"] == UNAUTHORIZED_ERR_MSG
    assert response_body["error"]["id"]
