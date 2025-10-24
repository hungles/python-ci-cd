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

def test_subtract():
    client = app.test_client()
    response = client.get("/subtract/5/3")
    assert response.status_code == 200
    assert response.data == b'2'  # La resta de 5 y 3 es 2

def test_divide():
    client = app.test_client()
    response = client.get("/divide/6/3")
    assert response.status_code == 200
    assert response.data == b'2.0'  # La división de 6 entre 3 es 2.0

    response = client.get("/divide/6/0")
    assert response.status_code == 400
    assert response.json["error"] == "Division by zero is not allowed"

