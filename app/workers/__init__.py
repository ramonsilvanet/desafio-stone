from flask import Blueprint

wbp = Blueprint('workers', __name__)

from app.workers import routes