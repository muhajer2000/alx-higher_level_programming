#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    lists = sys.argv[1:]
    length = len(sys.argv[1:])
    OpratList = ['+', '-', '/', '*']
    Olist = lists[1]
    a = int(lists[0])
    b = int(lists[2])

    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if Olist in OpratList:
            if Olist == '+':
                sum = add(a, b)
                print("{} + {} = {}".format(a, b, sum))
            elif Olist == '-':
                subrat = sub(a, b)
                print("{} - {} = {}".format(a, b, subrat))
            elif Olist == '*':
                mult = mul(a, b)
                print("{} * {} = {}".format(a, b, mult))
            elif Olist == '/':
                divit = div(a, b)
                print("{} / {} = {}".format(a, b, divit))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
