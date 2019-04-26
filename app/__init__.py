from flask import Flask
from config import Config
import logging

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Blueprints da Aplicacao
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)
    
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.jobs import bp as jobs_bp
    app.register_blueprint(jobs_bp)

    # configuracao de logs
    s_handler = logging.StreamHandler()
    s_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(s_handler)

    return app