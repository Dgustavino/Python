from flask import Flask, request, render_template , jsonify

api = Flask(__name__)       

@api.route('/ping/<string:cod>', methods=['GET'])
def ping(cod):
  if cod=='1':
      return "Hello"
  if cod=='2': 
      return "Bye" 

@api.route('/render_html', methods=['POST'])
def renderizador():
    mi_data_json = {"key_capturado": request.json['mensaje']}
    if mi_data_json['key_capturado']==5:
        return render_template("index.html")
    else:
        STATUS_CODE_FAIL = 405
        return jsonify({
                        "code": STATUS_CODE_FAIL
                        })


if __name__ == "__main__":      
    api.run(debug=True, port=4321)        
