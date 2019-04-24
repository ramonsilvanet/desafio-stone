from flask import Flask

from app.errors import bp as errors_bp
from app.workers import wbp as workers_bp

app.register_blueprint(errors_bp)
app.register_blueprint(workers_bp)

from app import routes


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    return app
