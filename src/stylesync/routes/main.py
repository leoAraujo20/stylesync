from flask import Blueprint, jsonify, request, current_app
from ..schemas.user import LoginPayload
from pydantic import ValidationError
from .. import db
from bson import ObjectId
from ..schemas.product import ProductDBModel, Product, ProductUpdateModel
import jwt
from datetime import datetime, timedelta, timezone
from ..decorators.decorators import token_required

main_bp = Blueprint("main_bp", __name__)


@main_bp.route("/")
def index():
    return jsonify({"message": "Bem-vindo ao StyleSync!"})


# RF: O sistema deve permitir que os usuários visualizem uma lista de produtos.
@main_bp.route("/produtos")
def get_products():
    products_db = db.Products.find()
    products_list = [
        ProductDBModel(**product).model_dump(by_alias=True, exclude_none=True)
        for product in products_db
    ]
    return jsonify(products_list)


# RF: O sistema deve permitir que os usuários visualizem detalhes de um produto específico.
@main_bp.route("/produtos/<string:produto_id>")
def get_product(produto_id):
    try:
        oid = ObjectId(produto_id)
    except Exception as e:
        return jsonify({"error": f"Erro ao converter ID: {e}"}), 400
    product = db.Products.find_one({"_id": oid})
    if product:
        product = ProductDBModel(**product).model_dump(by_alias=True, exclude_none=True)
        return jsonify(product)
    else:
        return jsonify({"error": "Produto não encontrado"}), 404


# RF: O sistema deve permitir que os usuários criem novo produtos.
@main_bp.route("/produtos", methods=["POST"])
@token_required
def create_product(token_data):
    try:
        product_data = Product(**request.json)
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400

    result = db.Products.insert_one(product_data.model_dump(exclude_none=True))
    return jsonify(
        {"message": "Produto criado com sucesso!", "id": str(result.inserted_id)}
    ), 201


# RF: O sistema deve permitir que os usuários atualizem produtos existentes.
@main_bp.route("/produtos/<string:produto_id>", methods=["PUT"])
@token_required
def update_product(token_data, produto_id):
    try:
        product_data = ProductUpdateModel(**request.json)
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400

    result = db.Products.update_one(
        {"_id": ObjectId(produto_id)},
        {"$set": product_data.model_dump(exclude_none=True)}
    )
    if result.modified_count:
        return jsonify({"message": f"Produto {produto_id} atualizado com sucesso!"})
    else:
        return jsonify({"error": "Produto não encontrado"}), 404


# RF: O sistema deve permitir que os usuários excluam produtos.
@main_bp.route("/produtos/<int:produto_id>", methods=["DELETE"])
def remove_product(produto_id):
    return jsonify({"message": f"Produto {produto_id} removido com sucesso!"})


# RF: O sistema deve permitir que o usuario se autentique para obter um token.
@main_bp.route("/login", methods=["POST"])
def login():
    try:
        payload = LoginPayload(**request.json)
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400

    if payload.username == "admin" and payload.password == "password":
        token = jwt.encode(
            {
                "user": payload.username,
                "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
            },
            current_app.config["SECRET_KEY"],
            algorithm="HS256",
        )
        return jsonify({"access_token": token})

    return jsonify({"message": "Credenciais inválidas"}), 401


# RF: O sistema deve permitir a importação de vendas através de arquivos.
@main_bp.route("/importar_vendas", methods=["POST"])
def import_sales():
    return jsonify({"message": "Essa é a rota de importação de vendas"})
