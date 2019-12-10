#!/usr/bin/env python
import sys
import time
from os import system, name
from playa import *

#If you change it for debugging, the default values are: speed: 0.05, space: 0.25.
def p(text="EMPTY PRINT FUNCTION", speed = 0.05, space = 0.25):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    time.sleep(space)
    sys.stdout.write("\n")

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

