from flask import Blueprint

api_blueprint = Blueprint('api', __name__)

from api import endpoints
