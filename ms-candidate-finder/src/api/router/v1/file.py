from flask import request, jsonify

def create_or_get_file(request):
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