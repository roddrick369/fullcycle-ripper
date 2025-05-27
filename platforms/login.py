from utils.http_client import post, set_auth_token

def login(username: str, password: str) -> str:
    """Login to the platform and return the authentication token."""
    
    url = "https://portal.fullcycle.com.br/api/login_check"

    boundary = "----WebKitFormBoundaryxZqud18BCKBITb7K"
    headers = {
        "Content-Type": f"multipart/form-data; boundary={boundary}",
        "Origin": "https://plataforma.fullcycle.com.br",
        "Referer": "https://plataforma.fullcycle.com.br/",
    }

    body = (
        f"{boundary}\r\nContent-Disposition: form-data; name=\"_username\"\r\n\r\n{username}\r\n"
        f"{boundary}\r\nContent-Disposition: form-data; name=\"_password\"\r\n\r\n{password}\r\n"
        f"{boundary}--\r\n"
    )

    res = post(url, headers=headers, data=body.encode('utf-8'))
    set_auth_token(res['token']) # type: ignore
    return res['token'] # type: ignore

