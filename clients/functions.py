def print_color(color:str,text:str):
    reset = "\033[0m"
    default = reset

    colors = {
        'black': "\033[30m",
        'red': "\033[31m",
        'green': "\033[32m",
        'yellow': "\033[33m",
        'blue': "\033[34m",
        'magenta': "\033[35m",
        'cyan': "\033[36m",
        'white': "\033[37m",
        'bright_black': "\033[90m",
        'bright_red': "\033[91m",
        'bright_green': "\033[92m",
        'bright_yellow': "\033[93m",
        'bright_blue': "\033[94m",
        'bright_magenta': "\033[95m",
        'bright_cyan': "\033[96m",
        'bright_white': "\033[97m",
    }

    selected_color = colors[color]
    if selected_color == None:
        selected_color = default

    return f'{selected_color}{text}{reset}'

    

def print_messages(messages:list,username:str):
    for message in messages.json():
        if username == message["nombre"]:
            print(f'{print_color("green",message["nombre"])}: {message["mensaje"]}')
            continue

        print(f'{print_color("blue",message["nombre"])}: {message["mensaje"]}')

def print_message(message,username):
    if username == message["nombre"]:
        print(f'{print_color("green",message["nombre"])}: {message["mensaje"]}')
        return
    print(f'{print_color("blue",message["nombre"])}: {message["mensaje"]}')