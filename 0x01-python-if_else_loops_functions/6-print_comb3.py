#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if i == j:
            continue
        if i + j == 17:
            continue
        print("{}{}, ".format(i, j), end="")
print("89")
