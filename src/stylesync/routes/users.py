from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from .. import db
from bson import ObjectId
from ..schemas.user import UserCreate, UserResponse
from ..decorators.decorators import token_required

users_bp = Blueprint("users_bp", __name__)


@users_bp.route("/usuarios", methods=["POST"])
def create_user():
    try:
        user_data = UserCreate(**request.json)
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400

    if db.Users.find_one({"username": user_data.username}):
        return jsonify({"error": "Usuário já existe!"}), 400

    result = db.Users.insert_one(user_data.model_dump(exclude_none=True))
    return jsonify(
        {"message": "Usuário criado com sucesso!", "id": str(result.inserted_id)}
    ), 201


@users_bp.route("/usuarios", methods=["GET"])
def get_users():
    users = db.Users.find({}, {"password": 0})
    users_list = [UserResponse(**user).model_dump() for user in users]
    return jsonify(users_list)


@users_bp.route("/usuarios/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        oid = ObjectId(user_id)
    except Exception as e:
        return jsonify({"error": f"Erro ao converter ID: {e}"}), 400

    result = db.Users.delete_one({"_id": oid})
    if result.deleted_count == 1:
        return jsonify({"message": "Usuário deletado com sucesso!"}), 200
    else:
        return jsonify({"error": "Usuário não encontrado"}), 404
