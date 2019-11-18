from flask_cors import cross_origin
from flask import request, jsonify, Blueprint

routes_blueprint = Blueprint('routes', 'routes')

# TODO: Implement auth middleware
@routes_blueprint.route('/file', methods=['GET', 'POST'])
@cross_origin(headers=["Content-Type", "Authorization"])
def file():
    if request.method == 'GET':
        try:
            return jsonify({'data': 'data_to_send'}), 200
        except BaseException as ex:
            return jsonify({'message': 'Error occured: ' + str(ex)})
    
    if request.method == 'POST':
        try:
            return jsonify({'data': 'data_to_send'}), 200
        except BaseException as ex:
            return jsonify({'message': 'Error occured: ' + str(ex)})
