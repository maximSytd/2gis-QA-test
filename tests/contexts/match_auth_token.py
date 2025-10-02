import re

import vedro

@vedro.context
def match_auth_token(token_string: str) -> bool:
    """Return bool and check if string pass token regex."""
    token_match = re.search(r"token=([a-f0-9]+);", token_string)
    return token_match is not None
