from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_auth():
    response = client.post(
        '/api/v1/auth/login',
        json = {
            "username": "test",
            "password": "test"
        }
    )

    assert response.status_code == 200
    assert response.json() == {
        "data": {
            "_id": "6363e9c00577f555062cb70d",
            "fullname": "test",
            "bibCode": "123",
            "identityImages": []
        },
        "code": 200,
        "message": "Login successfully.",
        "error": False
    }

def test_auth_wrong_account():
    response = client.post(
        '/api/v1/auth/login',
        json = {
            "username": "footest",
            "password": "footest"
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "data": None,
        "code": 200,
        "message": "Login failure, please check your account information!",
        "error": True
    }
