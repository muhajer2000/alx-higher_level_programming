#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    n = number % -10
else:
    n = number % 10
str = "Last digit of"
if (n > 5):
    print(f"{str} {number:d} is {n:d} and is greater than 5")
elif (n == 0):
    print(f"{str} {number:d} is {n:d} and is 0")
elif (n < 6 and n != 0):
    print(f"{str} {number:d} is {n:d} and is less than 6 anf not 0")
