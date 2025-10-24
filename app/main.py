# import necessary libraries
from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Simple route to test the application
@app.route("/")
def home():
    return {"message": "Hello CI/CD with Python!"}

@app.route("/users")
def get_users():
    return {"users": ["Alice", "Bob", "Charlie"]}

@app.route("/sum/<int:a>/<int:b>")
def sumar(a, b):
    return str(a + b)

@app.route("/subtract/<int:a>/<int:b>")
def subtract(a, b):
    return str(a - b)

@app.route("/divide/<int:a>/<int:b>")
def divide(a, b):
    if b == 0:
        return {"error": "Division by zero is not allowed"}, 400
    return str(a / b)

@app.route("/power/<int:a>/<int:b>")
def power(a, b):
    return str(a ** b)

# Static users data and route to view them
    
@app.route("/users/static")
def users_static():
    USERS = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"},
        {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
    ]
    return {"users": USERS}

# Run the application
if __name__ == "__main__":  # pragma: no cover
    app.run(host="0.0.0.0", port=5000)

# Esto es un comentario que ira a staging adicional