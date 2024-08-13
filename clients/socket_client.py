import socketio
import requests
from functions import *
socket = socketio.Client()
URL = 'http://localhost:5000'

username = input("Ingrese su nombre de usuario > ")

socket.connect(URL)

@socket.on('new_message')
def on_message(data):
    global username
    print_message(data,username)

while True:
    message_to_send = input("> ")

    if message_to_send.strip() == '':
        print('El mensaje no puede estar vacio')
        continue

    if message_to_send == 'EXIT':
        break

    data = {
        'nombre':username,
        'mensaje':message_to_send
    }

    response = requests.post(f'{URL}/add-message',json=data)
