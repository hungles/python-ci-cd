# import necessary libraries
from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Simple route to test the application
@app.route("/")
def home():
    return {"message": "Hello CI/CD with Python!"}

# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# Esto es un comentario que ira a staging