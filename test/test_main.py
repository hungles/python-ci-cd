from app.main import app
from app.main import sumar

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "Hello CI/CD with Python!"

def test_sumar():
    resultado = sumar(1, 2)
    assert resultado == 3