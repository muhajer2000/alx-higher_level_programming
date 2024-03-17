#!/usr/bin/python3
def element_at(my_list, idx):
    n = len(my_list) - 1
    if idx < 0 or idx > n:
        return None
    num = my_list[idx]
    return num
