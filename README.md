# Aplicación de Mensajería Sencilla

Este proyecto es una aplicación de mensajería sencilla construida con Flask para el backend y un script en Python para el cliente. La aplicación permite a los usuarios enviar y recibir mensajes en tiempo real con una autenticación básica usando un token secreto.

## Estructura del Proyecto

- `app.py`: Aplicación backend con Flask
- `client.py`: Script del cliente en Python
- `functions.py`: Funciones auxiliares para el cliente
- `README.md`: Documentación del proyecto

## Requisitos

- Python 3.x
- Flask
- requests
- Flask-CORS

## Instalación

1. Clonar el repositorio:

```
git clone https://github.com/xJesusx0/simple-api.git
cd simple-api
```

2. Crear y activar un entorno virtual:

```
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
```

3. Instalar los paquetes necesarios:

```
pip install Flask requests Flask-CORS
```

## Ejecución de la Aplicación

1. Iniciar el servidor backend con Flask:

```
python app.py
```

2. En otro terminal, ejecutar el script del cliente:

```
python client.py
```

## Backend (Flask)

### `app.py`

Este es el archivo principal de la aplicación Flask que maneja la lógica del backend.

#### Rutas

- `GET /get-messages`: Retorna la lista de mensajes.
- `POST /add-message`: Agrega un nuevo mensaje.

## Cliente

### `client.py`

Este script maneja el lado del cliente de la aplicación. Los usuarios pueden enviar y recibir mensajes a través de este script.

### `functions.py`

Contiene funciones auxiliares para el cliente.

## Uso

1. Al ejecutar `client.py`, se te pedirá que ingreses tu nombre de usuario.
2. El cliente mostrará todos los mensajes obtenidos del servidor.
3. Puedes escribir mensajes para enviarlos al servidor.
4. Escribe `EXIT` para cerrar el cliente.

## Notas

- Asegúrate de que el servidor Flask esté en ejecución antes de iniciar el cliente.
- El script del cliente continuamente obtendrá mensajes del servidor y los mostrará en tiempo real.
- La autenticación se realiza usando un mecanismo sencillo de token.
