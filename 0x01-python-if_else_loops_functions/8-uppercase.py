#!/usr/bin/python3
def uppercase(str):
    for str1 in str:
        if ord(str1) >= 97 and ord(str1) <= 122:
            str1 = chr(ord(str1) - 32)
        print("{}".format(str1), end="")
    print()
