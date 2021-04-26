from flask import Flask,jsonify
from file_handler import File_Handler

api = Flask(__name__)     

obj_file = File_Handler()


@api.route('/file/<string:columna>', methods=['GET']) data_get(columna):
        datos = obj_file._data_from_file

        return jsonify({
                    "La data del file es ": datos
                    })



@api.route('/file', methods=['POST'])
def data_post():
    input_from_client = request.json['propiedad']

    if obj_file.write_file(input_from_client):
        STATUS_CODE = 200
    else:
        STATUS_CODE = 400

    return jsonify({
                    "code": STATUS_CODE
                    })


if __name__ == "__main__":      
    api.run(debug=True)        
