from flask import Flask
from stylesync.routes.main import main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('stylesync.config.Config')
    app.register_blueprint(main_bp)
    return app
