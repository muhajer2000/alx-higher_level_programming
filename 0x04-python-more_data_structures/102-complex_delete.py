#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for kvalue in list_keys:
        if value == a_dictionary.get(kvalue):
            del a_dictionary[kvalue]
    return (a_dictionary)
