import vedro
import httpx

from ..config import Config

from ..contexts.client_manager import client_manager

class AuthApi(vedro.Interface):
    def __init__(self, base_url = Config.Api.BASE_URL):
        self.client = client_manager(base_url)

    async def authenticate(self) -> httpx.Response:
        return await self.client.post(Config.Api.AUTH_URL)
