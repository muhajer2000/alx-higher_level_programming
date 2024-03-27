#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    a = dir()
    for i in (0, len(a)):
        if a[i][:2] != "__":
            print(a[i])
