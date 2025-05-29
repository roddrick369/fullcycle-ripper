import json
from string import Template
import os
from utils.http_client import get

endpoints_path = os.path.join('utils', 'endpoints.json')

with open(endpoints_path, 'r') as file:
    data = json.load(file)

def get_courses() -> list: # type: ignore
    url = "https://portal.fullcycle.com.br/api/cursos/my.json"
    return get(url)  # type: ignore

def get_learning_paths(course_id: int, classroom_id: int) -> dict:
    values = {
        "course_id": course_id,
        "classroom_id": classroom_id
    }

    parsed_data = {key: Template(value).substitute(values) for key, value in data.items()}
    
    url = parsed_data["fc4"] if course_id == 215 else parsed_data["standard"]
    return get(url)  # type: ignore