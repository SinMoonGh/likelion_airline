import pytest
from fastapi.testclient import TestClient
from test_main import app  # FastAPI 서버 파일에서 앱 가져오기

client = TestClient(app)

def test_signup():
    """회원가입 데이터를 서버로 전송하고 응답 확인"""
    response = client.post(
        "/signup",
        json={
            "firstName": "남",
            "lastName": "길동",
            "email": "testuser@example.com",
            "password": "password123",
        },
    )
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["message"] == "User registered successfully"
    assert response_data["data"]["firstName"] == "남"
    assert response_data["data"]["lastName"] == "길동"
    assert response_data["data"]["email"] == "testuser@example.com"
    print("Test Passed: 회원가입 데이터 성공적으로 처리됨.")
