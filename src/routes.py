from app import app
from flask import request


@app.route("/")
def hello():
    print(request)
    return "hello"

