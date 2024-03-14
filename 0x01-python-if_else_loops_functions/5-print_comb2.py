#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        num = i + j
        sa = ","
        if num == 18:
            sa = " "
        print("{}{}{} ".format(i, j, sa), end="")
