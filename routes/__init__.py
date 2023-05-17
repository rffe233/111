from flask import Blueprint
from .films import films_bp
routes_bp = Blueprint('routes', __name__)
routes_bp.register_blueprint(films_bp, url_prefix='/api/films')
