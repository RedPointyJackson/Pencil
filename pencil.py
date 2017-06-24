#!/usr/bin/env python

from tkinter import *
from time import sleep
import numpy as np
import sys, argparse

# Parse user arguments
parser = argparse.ArgumentParser(description='Interpreter of graphics')
parser.add_argument('--width', '-w', metavar='width', type=int, nargs=1,
                    help='Width of the scene', default = 500)
parser.add_argument('--height', '-y', metavar='height', type=int,
                    nargs=1, help='Height of the scene', default = 250)
parser.add_argument('--bg-color', '-b', metavar='bgcolor',
                    nargs=1, help='Background color', default = 'white')

args = parser.parse_args()

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# Defs
master = Tk()
master.title('Pencil output')
w = Canvas(master, width=args.width, height=args.height, bg=args.bg_color)
w.pack()

current_color = 'black'

# Main method
def readin():
    while True:
        try:
            readcommand()
        except KeyboardInterrupt:
            eprint("Keyboard Interrupt. Exiting.")
            sys.exit()
        except EOFError:
            eprint("EOF error. Exiting.")
            sys.exit()


def readcommand():
    global current_color
    command = input()
    words = command.split()
    # Drawing commands
    if len(words) >= 1:
        if words[0] == 'rectangle':
            fromx = float(words[1])
            fromy = float(words[2])
            tox = float(words[3])
            toy = float(words[4])
            w.create_rectangle(fromx, fromy, tox, toy, fill=current_color, outline=current_color)
        elif words[0] == 'point':
            x = float(words[1])
            y = float(words[2])
            w.create_rectangle(x, y, x+1, y+1, outline=current_color)
        elif words[0] == 'line':
            fromx = float(words[1])
            fromy = float(words[2])
            tox = float(words[3])
            toy = float(words[4])
            w.create_line(fromx,fromy,tox,toy, fill=current_color)
        elif words[0] == 'changesize':
            width = float(words[1])
            height = float(words[2])
            w.config(width=width, height=height)
        elif words[0] == 'changebg':
            w.config(bg=words[1])
        elif words[0] == 'changecolor':
            current_color = words[1]
        elif words[0] == 'txt':
            if len(words) > 3:
                x = float(words[1])
                y = float(words[2])
                w.create_text(x, y,fill = current_color,anchor=NW ,text=words[3:])
                # Canvas commands
        elif words[0] == 'clear':
            w.delete(ALL)
        elif words[0] == 'update':
            master.update()
        elif words[0] == 'quit':
            sys.exit()
        else:
            eprint('Command', command, 'not recognized')
    else:
        eprint('Error. Empty command')



# Begin program
master.after(1000,readin)
mainloop()
