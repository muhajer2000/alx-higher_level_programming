#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        items = []
        items = my_list[::-1]
        for item in items:
            print("{:d}".format(item))
