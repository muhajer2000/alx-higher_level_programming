#!/usr/bin/python3
def uniq_add(my_list):
    check_list = list(set(my_list))
    result = 0
    for items in check_list:
        result = result + items
    return (result)
