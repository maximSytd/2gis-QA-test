import vedro.config as cfg

from .factories import COLOR_CHOICES

class Config(cfg.Config):
    """Config for bdd tests."""

    class HTTP(cfg.Section):
        """Config for httpx."""

        REQUEST_TIMEOUT_SEC = 3
        MAX_RETRIES = 3
        RETRY_BACKOFF = 0.5

    class Api(cfg.Section):
        """Config with api urls."""

        BASE_URL = "https://regions-test.2gis.com"
        AUTH_URL = "/v1/auth/tokens"
        FAVORITES_URL = "/v1/favorites"

    class ErrorMessages(cfg.Section):
        """Config with error messages from invalid requests for api."""

        UNAUTHORIZED = "Параметр 'token' является обязательным"
        TITLE = "Параметр 'title' должен содержать не более 999 символов"
        LAT_LESS = "Параметр 'lat' должен быть не менее -90"
        LAT_MORE = "Параметр 'lat' должен быть не более 90"
        LON_LESS = "Параметр 'lon' должен быть не менее -180"
        LON_MORE = "Параметр 'lon' должен быть не более 180"
        COLOR = (
            "Параметр 'color' может быть одним из следующих "
            f"значений: {", ".join(COLOR_CHOICES)}"
        )


