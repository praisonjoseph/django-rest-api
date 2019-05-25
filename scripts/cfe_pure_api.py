import requests
import json

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/updates/"

def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    print(r.status_code)
    status_code = r.status_code
    if status_code != 200:
        print("probably not a good sign")
    data = r.json()
    # for obj in data:
    #     # print(obj['id'])
    #     if obj['id'] == 1:
    #         r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
    #         return r2.json()
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
        "content": "Some awesome new content"
    }
    r = requests.delete(BASE_URL + ENDPOINT + "5" + "/", data=json.dumps(new_data))
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text

# print(get_list())
# print(create_update())
print(do_obj_update())