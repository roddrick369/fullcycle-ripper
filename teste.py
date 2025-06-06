import json
import re
import os

filenames = ["parsed_01.json", "parsed_02.json", "parsed_03.json", "parsed_04.json", "parsed_05.json", "parsed_06.json",
             "parsed_07.json", "parsed_08.json", "parsed_09.json", "parsed_10.json", "parsed_11.json", "parsed_12.json",
             "parsed_13.json"]

json_list = os.path.join("result_module-list.json")
parsed = os.path.join("parsed.json")

html_re = re.compile(r'<.*?(?=\},\\"|\}\]|,\\")')
json_re = re.compile(r'"\[\{.*?\}\]"')
fst_lst_quote_re = re.compile(r'^"|"$')
transcript_entry = re.compile(r'\\"(?:video_transcription_nivo\\":.*?\\"(?=,\\))')

with open(json_list, 'r', encoding='utf-8') as file:
    data = file.read()

matching_html = html_re.findall(data)
new_data = html_re.sub('\\"', data)
clean_data = json_re.findall(new_data)
new_clean_data = json_re.findall(transcript_entry.sub('\\"video_transcription_nivo\\":\\"\\"', new_data)) # type: ignore

#print(new_data[:500])

# with open(parsed, "w", encoding='utf-8') as file:
#     file.write(new_data)


# # exemplo real que veio com escape duplo ou colado de HTML
# text = '{\\"texto\\":\\"<div class=\\"message\\">\\"}'

# # primeiro, substituir aspas duplas escapadas por reais
# clean = text.replace('\\"', '"')
# print(new_clean_data[2])

# # depois fazer o parse
# parsed_json = json.loads(json.loads(new_clean_data[2])) # type: ignore
# print(parsed_json)
#######reparsed_json = json.loads(parsed_json)

parsed_json = []
for json_text in new_clean_data:
    # try:
    parsed_json.append(json.loads(json.loads(json_text)))
    # except :
    #     log = os.path.join('log.json')
    #     with open(log, 'w', encoding='utf-8') as f:
    #         f.write(json.dumps(json.loads(json_text)))

# print(parsed_json)

for file_path, json_data, in zip(filenames, parsed_json): # type: ignore
    file = os.path.join(file_path)
    
    with open(file, "w", encoding='utf-8') as f:
        f.write(json.dumps(json_data, indent=4))

# with open(parsed, "w", encoding='utf-8') as file:
#     file.write(json.dumps(parsed_json,indent=2))
