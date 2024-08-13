from flask import jsonify
from flask import Flask
from flask import request
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
import json
from flask_socketio import SocketIO, emit
app = Flask(__name__)

SECRET_TOKEN = '123'
CORS(app)
socketio = SocketIO(app)


def convert_objectid_to_str(document):
    if isinstance(document, dict):
        for key, value in document.items():
            if isinstance(value, ObjectId):
                document[key] = str(value)
            elif isinstance(value, dict):
                document[key] = convert_objectid_to_str(value)
            elif isinstance(value, list):
                document[key] = [convert_objectid_to_str(item) for item in value]
    elif isinstance(document, list):
        document = [convert_objectid_to_str(item) for item in document]
    return document


def get_messages():
    client = MongoClient()
    db = client.api
    collection = db.messages

    result = collection.find({})
    documents = [convert_objectid_to_str(doc) for doc in result]

    client.close()
    print(type(documents))
    return documents

def insert_message(message:dict):
    client = MongoClient()
    db = client.api
    collection = db.messages
    
    result = collection.insert_one(message)
    print('Mensaje insertado')
    client.close()
    message_json = convert_objectid_to_str(message)

    socketio.emit('new_message',message_json)

@app.route('/get-messages')
def index ():

    messages = get_messages()
    print(type(messages)) 
    return jsonify(messages),200

@app.route('/add-message',methods = ["POST"])
def add_message():

    message = request.json
    if not message:
        return jsonify({'response':'No hay mensaje'}),400
    
    if 'nombre' not in message:
        return jsonify({'response':'No hay nombre'}),400
    
    if 'mensaje' not in message:
        return jsonify({'response':'No hay contenido del mensaje'}),400
    
    insert_message(message)
    return jsonify({'response': 'Mensaje agregado'}), 200
        
if __name__ == '__main__':  
    app.run(debug = True, host = '0.0.0.0')
