from flask import Flask
from pymongo import MongoClient
import os

db = None

def create_app():
    app = Flask(__name__)
    app.config.from_object('src.stylesync.config.Config')
    global db
    try:
        client = MongoClient(os.environ.get('MONGO_URI'))
        db = client.get_database('stylesync')
    except Exception as e:
        print(f'Erro ao conectar ao banco de dados: {e}')
    from .routes.main import main_bp
    from .routes.users import users_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(users_bp)
    return app
