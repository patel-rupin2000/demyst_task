from flask import Flask
from config import Config
from flask_cors import CORS


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)
    from app.controllers import balance_sheet_controller, application_controller
    app.register_blueprint(balance_sheet_controller.bp)
    app.register_blueprint(application_controller.bp)

    return app
