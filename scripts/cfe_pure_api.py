import requests
import json

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/updates/"

def get_list(id=None):
    data = json.dumps({})
    if id is not None:
        data = json.dumps({'id': id})
    r = requests.get(BASE_URL + ENDPOINT, data=data)
    print(r.status_code)
    status_code = r.status_code
    if status_code != 200:
        print("probably not a good sign")
    data = r.json()
    return data

def create_update():
    new_data = {
        'user': 1,
        "content": "Some more new cool update"
    } 
    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print(r.status_code)
    print(r.headers)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text

def do_obj_update():
    new_data = {
        "id": 7,
        "content": "new awesome"
    }
    r = requests.put(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text

print(get_list())
# print(create_update())
# print(do_obj_update())