import json
from string import Template
import os
from utils.http_client import get
from utils.json_extract import  decode

module_list = os.path.join('result_module-list.json')

endpoints_path = os.path.join('utils', 'endpoints.json')

with open(endpoints_path, 'r') as file:
    data = json.load(file)

def get_courses() -> list: # type: ignore
    url = data["courses"]
    return get(url)  # type: ignore

def get_learning_paths(course_id: int, classroom_id: int) -> dict:
    values = {
        "course_id": course_id,
        "classroom_id": classroom_id
    }

    parsed_data = {key: Template(value).substitute(values) for key, value in data["learning_paths"].items()}  
    url = parsed_data["fc4"] if course_id == 215 else parsed_data["standard"] # type: ignore
    return get(url)  # type: ignore

def get_classrooms(catalog_id: int, classroom_id: int) -> dict:
    values = {
        "classroom_id": classroom_id,
        "catalog_id": catalog_id
    }

    parsed_data = Template(data["classrooms"]).substitute(values)
    url = parsed_data
    print(parsed_data)
    return get(url) # type: ignore

def get_modules(chapter_id: int, classroom_id: int) -> dict:
    values = {
        "classroom_id": classroom_id,
        "chapter_list_id": chapter_id
    }
    parsed_data = Template(data["modules"]).substitute(values)
    url = parsed_data
    encoded_res =  get(url) #type: ignore
    res = decode(encoded_res["content"]) # type: ignore
    decompressed_dict = json.loads(rf'''{{"content": {res}}}''')
    with open(module_list, 'a', encoding='utf-8') as file:
        json.dump(res, file, ensure_ascii=False, indent=2) # type: ignore
        
    return {"content": res}