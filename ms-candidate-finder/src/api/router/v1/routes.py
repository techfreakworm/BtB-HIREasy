from flask_cors import cross_origin
from flask import request, jsonify, Blueprint
from .file import create_or_get_file

routes_blueprint = Blueprint('routes', 'routes')

# TODO: Implement auth middleware
@routes_blueprint.route('/file', methods=['GET', 'POST'])
@cross_origin(headers=["Content-Type", "Authorization"])
def file():
    return create_or_get_file(request)
