from app.main import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "Hello CI/CD with Python!"

def test_get_users():
    client = app.test_client()
    response = client.get("/users")
    assert response.status_code == 200
    assert "users" in response.json
    assert len(response.json["users"]) == 3

def test_sumar():
    client = app.test_client()
    response = client.get("/sum/2/3")
    assert response.status_code == 200
    assert response.data == b'5'  # La suma de 2 y 3 es 5