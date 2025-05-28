from utils.http_client import get

def get_courses() -> list: # type: ignore
    url = "https://portal.fullcycle.com.br/api/cursos/my.json"
    return get(url)  # type: ignore

def get_learning_paths(course_id: int, classroom_id: int) -> dict:
    url = f"https://portal.fullcycle.com.br/api/learning_paths/categories/{course_id}/classrooms/{classroom_id}"
    return get(url)  # type: ignore