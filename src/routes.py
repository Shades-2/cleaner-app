from flask import request, current_app


@current_app.route("/")
def test():
    print(request)
    return "hello"

