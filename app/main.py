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

# Run the application
if __name__ == "__main__":  # pragma: no cover
    app.run(host="0.0.0.0", port=5000)

# Esto es un comentario que ira a staging