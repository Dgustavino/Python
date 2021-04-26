from flask import Flask, request, render_template , jsonify
from services import Service_Sqlite

api = Flask(__name__)       
service_db = Service_Sqlite()

query = ""

@api.route('/table/<string:name>', methods=['GET'])
def get_table(name):
    service_db.todos_los_registros(name)