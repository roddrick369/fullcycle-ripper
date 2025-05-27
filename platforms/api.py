from utils.http_client import get

def get_courses() -> list: # type: ignore
    url = "https://portal.fullcycle.com.br/api/curses/my.json"
    return get(url)  # type: ignore

