#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lists = sys.argv[1:]
    length = len(sys.argv[1:])
    sum = 0

    if lists == 0:
        print("{}".format(lists))
    else:
        for list in lists:
            sum = sum + int(list)
    print("{}".format(sum))
