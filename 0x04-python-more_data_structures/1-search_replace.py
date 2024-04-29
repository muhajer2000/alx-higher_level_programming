#!/usr/bin/python3
def search_replace(my_list, serach, replace):
    new_list = my_list.copy()
    for n in range(len(new_list)):

        if new_list[n] == serach:
            new_list[n] = replace
    return(new_list)
