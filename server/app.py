from flask import jsonify
from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
SECRET_TOKEN = '123'
CORS(app)

messages = []

@app.route('/get-messages')
def index ():
    return jsonify(messages),200

@app.route('/add-message',methods = ["POST"])
def add_message():

    token = request.headers.get('token')
    message = request.json

    if token != SECRET_TOKEN:
        return jsonify({'response':'Token invalido'}),401

    if not message:
        return jsonify({'response':'No hay mensaje'}),400
    
    if 'nombre' not in message:
        return jsonify({'response':'No hay nombre'}),400
    
    if 'mensaje' not in message:
        return jsonify({'response':'No hay contenido del mensaje'}),400
    
    messages.append(message)
    return jsonify({'response': 'Mensaje agregado'}), 200
        
if __name__ == '__main__':  
    app.run(debug = True)