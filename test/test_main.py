from app.main import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "Hello CI/CD with Python!"

def test_sumar():
    assert app.sumar(2, 3) == 5
    assert app.sumar(-1, 1) == 0
    assert app.sumar(0, 0) == 0