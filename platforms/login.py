from utils.http_client import post, set_auth_token

def login(username: str, password: str) -> str:
    """Login to the platform and return the authentication token."""
    
    url = "https://portal.fullcycle.com.br/api/login_check"

    headers = {
    
    }

    data = {
        "_username": (None, username),
        "_password": (None, password),
    }

    res = post(url, headers=headers, data=data)  # type: ignore

    if 'token' not in res: # type: ignore
        raise Exception("Login failed, no token received.")
    set_auth_token(res['token']) # type: ignore
    return res['token'] # type: ignore

