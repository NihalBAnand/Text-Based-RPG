#!/usr/bin/env python
import sys
import time
from os import system, name

def p(text="EMPTY PRINT FUNCTION", speed = 0.0, space = 0):
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