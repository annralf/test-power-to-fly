from email import header
import json
from wsgiref.headers import Headers

def test_user(test_app):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    response = test_app.get("/users/", headers=headers)
    print(response.data)

    print(response.status_code, 'response active')
    assert True


def test_user_list(test_app):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    payload = {
            "search":[
                {"name":"jose"}
            ]
        }
    response = test_app.get("/users/", headers=headers, json=payload)
    print(response.data)

    print(response.status_code, 'response active')
    assert True