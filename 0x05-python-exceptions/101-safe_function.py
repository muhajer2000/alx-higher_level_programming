#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        val = fct(*args)
        return val
    except Exception as b:
        print("Exception: {}".format(b), file=sys.stderr)
        return None
