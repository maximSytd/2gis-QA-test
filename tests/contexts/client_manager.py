import vedro
import httpx
import vedro_httpx
import httpx_retries

from ..config import Config

@vedro.context
def client_manager(base_url: str, **kw) -> vedro_httpx.AsyncClient:
    """Return httpx async client."""
    transport = httpx_retries.RetryTransport(
        retry=httpx_retries.Retry(
            total=Config.HTTP.MAX_RETRIES,
            backoff_factor=Config.HTTP.RETRY_BACKOFF,
            allowed_methods=(
                "POST",
            ),
        ),
    )
    return httpx.AsyncClient(
        base_url=base_url,
        transport=transport,
        timeout=Config.HTTP.REQUEST_TIMEOUT_SEC,
        **kw,
    )
