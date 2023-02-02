import requests
from pytest_voluptuous import S

from schemas.user import single_user_schema


def test_get_users_satus_code():
    response = requests.get(url='https://reqres.in/api/users')
    assert response.status_code == 200


def test_check_users_email():
    response = requests.get(url='https://reqres.in/api/users/3')
    assert response.json()['data']['email'] == 'emma.wong@reqres.in'


def test_get_users_schema():
    response = requests.get(url='https://reqres.in/api/users/3')
    assert S(single_user_schema) == response.json()


def test_create_user():
    response = requests.post(url='https://reqres.in/api/users', json={
        "name": "morpheus",
        "job": "leader"
    })
    assert response.status_code == 201


def test_delete_user():
    response = requests.delete(url='https://reqres.in/api/users/3')
    assert response.status_code == 204
