import requests

session = requests.Session()

session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept': 'application/json',
})

def set_auth_token(token: str):
    """Set the Bearer authorization token for the session."""

    session.headers.update({
        'Authorization': f'Bearer {token}'
    })

def get(url: str, headers: dict | None = None, params: dict | None = None) -> dict | None:
    """Send a GET request to the specified URL with optional headers and parameters."""
    
    merged_headers = _merge_headers(headers) # type: ignore
    res = session.get(url, headers=merged_headers, params=params)
    
    _check_response(res)
    return res.json()

def post(url: str, headers: dict | None = None, data=None, json_data=None) -> dict | None:
    """Send a POST request to the specified URL with optional headers and data."""
    
    merged_headers = _merge_headers(headers) # type: ignore
    res = session.post(url, headers=merged_headers, data=data, json=json_data)
    
    _check_response(res)
    return res.json()

def _merge_headers(extra_headers: dict) -> dict[str, str | bytes]:
    """Merge extra headers with the session headers."""
    
    if not extra_headers:
        return session.headers  # type: ignore
    
    combined = session.headers.copy() # type: ignore
    combined.update(extra_headers)
    return combined

def _check_response(res):
    """Check the response status code and raise an exception if it's not successful."""
    
    if res.status_code >= 400:
        raise Exception(f"HTTP error {res.status_code}: {res.text}")