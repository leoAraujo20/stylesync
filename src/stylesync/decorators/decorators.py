from functools import wraps
from flask import request, jsonify, current_app
import jwt


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return jsonify({"message": "Token não fornecido!"}), 401
        try:
            token_data = jwt.decode(
                token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
            )
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expirado!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Token inválido!"}), 401
        return func(token_data, *args, **kwargs)

    return wrapper
