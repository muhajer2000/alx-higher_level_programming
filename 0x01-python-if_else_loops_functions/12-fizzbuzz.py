#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0:
            n = "Fizz"
        elif n % 5 == 0:
            n = "Buzz"
        elif n % 3 == 0 and n % 5 == 0:
            n = "FizzBuzz"
        print("{} ".format(n), end="")
