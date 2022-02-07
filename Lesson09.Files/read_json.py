import json

with open('file.json') as json_file:
    python_dict = json.load(json_file)

print(python_dict.get('userId'))