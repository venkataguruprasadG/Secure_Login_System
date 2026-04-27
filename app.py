from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return f"Welcome to the Home Page!"


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    return f"Username: {username}, Password: {password}"


if __name__ == "__main__":
    app.run(debug=True)
