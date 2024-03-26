#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    sum = add(a, b)
    print("{} + {} = {}".format(a, b, sum)
    subrat = sub(a, b)
    print("{} - {} = {}".format(a, b, subrat)
    mult = mul(a, b)
    print("{} * {} = {}".format(a, b, mult)
    divit = div(a, b)
    print("{} / {} = {}".format(a, b, divit)
