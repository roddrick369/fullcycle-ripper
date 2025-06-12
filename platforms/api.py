import json
from string import Template
import os
import re
from utils.http_client import get
from utils.json_extract import  decode

module_list = os.path.join('result_module-list-2.json')

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
    res =  decode(get(url)["content"]) #type: ignore
    
    #print(res)
    # check_res = os.path.join('pure_res.json')
    # with open(check_res, 'a', encoding='utf-8') as f:
    #     # f.write(json.dumps(res, ensure_ascii=False, indent=4))
    #     f.write(res)

    html_re = re.compile(r'<.*?(?=\},\{|\},\\"|\}\]|,")')
    #json_re = re.compile(r'"\[\{.*?\}\]"')
    transcript_entry_re = re.compile(r'"(?:video_transcription_nivo.*?"(?=,"))')

    res_html_removed = html_re.sub('\"', res)
    clean_res = transcript_entry_re.sub('"video_transcription_nivo":""', res_html_removed) # type: ignore

    #print(clean_res)
    # check_res = os.path.join('check_res.json')
    # with open(check_res, 'a', encoding='utf-8') as f:
    #     f.write(json.dumps(clean_res, ensure_ascii=False, indent=4))

    decompressed_dict = json.loads(clean_res)

    print(decompressed_dict)

    with open(module_list, 'a', encoding='utf-8') as f:
        f.write(json.dumps(decompressed_dict, ensure_ascii=False, indent=4))
    # decompressed_dict = json.loads(rf'''{{"content": {res}}}''')
    # with open(module_list, 'a', encoding='utf-8') as file:
    #     json.dump(res, file, ensure_ascii=False, indent=2) # type: ignore
        
    return {"content": decompressed_dict}