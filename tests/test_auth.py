import vedro

from .interfaces.auth_api import AuthApi
from .contexts.match_auth_token import match_auth_token
from .constants import OkStatusSchema

class Scenario(vedro.Scenario):
    subject = "User gets authentication token"

    async def when_user_authenticates(self):
        self.response = await AuthApi().authenticate()

    def then_it_should_return_success_response(self):
        assert self.response.status_code == OkStatusSchema

    def then_it_should_have_token(self):
        assert match_auth_token(self.response.headers["Set-Cookie"]) is True, self.response.headers

    def and_it_should_contain_token_life_span(self):
        assert "Max-Age=2" in self.response.headers["Set-Cookie"], self.response.headers
