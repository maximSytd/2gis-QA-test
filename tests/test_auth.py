import re

import vedro
import httpx

from .interfaces.auth_api import AuthApi

class Scenario(vedro.Scenario):
    subject = "Get authentication token"

    async def when_user_authenticates(self):
        self.response = await AuthApi().authenticate()

    def then_it_should_return_success_response(self):
        assert self.response.status_code == httpx.codes.OK

    def then_it_should_have_token(self):
        token_match = re.search(
            r"token=([a-f0-9]+);",
            self.response.headers["Set-Cookie"],
        )
        assert token_match is not None, self.response.headers

    def then_it_should_contain_token_life_span(self):
        assert "Max-Age=2" in self.response.headers["Set-Cookie"], (
            self.response.headers
        )

