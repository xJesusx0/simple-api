import requests
from functions import *

URL = 'http://127.0.0.1:5000'
TOKEN = '123'
headers = { 'token':TOKEN }

username = input("Ingrese su nombre de usuario > ")


while True:

    messages = requests.get(f'{URL}/get-messages',headers=headers)
    print_messages(messages,username)

    message_to_send = input("> ")

    if message_to_send.strip() == '':
        print(print_color('red','El mensaje no puede estar vacio'))
        continue

    if message_to_send == 'EXIT':
        break

    data = {
        'nombre':username,
        'mensaje':message_to_send
    }

    response = requests.post(f'{URL}/add-message',headers=headers,json=data)