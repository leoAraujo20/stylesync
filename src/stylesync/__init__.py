from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('src.stylesync.config.Config')
    from .routes.main import main_bp
    app.register_blueprint(main_bp)
    return app
