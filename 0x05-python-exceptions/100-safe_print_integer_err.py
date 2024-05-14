#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    num = True

    try:
        print("{:d}".format(value))    
    except Exception as b:
        print("Exception:", b ,file=sys.stderr)
        num = False
    return num
