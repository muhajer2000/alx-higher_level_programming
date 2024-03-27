#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lists = sys.argv[1:]
    length = len(sys.argv[1:])

    if length == 0:
        print("{} argument.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
        print("{}: {}".format(length, lists[0]))
    else:
        print("{} argument:".format(length))
        for list in lists:
            print("{}: {}".format(lists.index(list) + 1, list))
