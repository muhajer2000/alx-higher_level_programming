#!/usr/bin/python3
def subtract(list_ro):
    sub = 0
    max_list = max(list_ro)
    for num in list_ro:
        if max_list > num:
            sub += num
    return (max_list - sub)

def roman_to_int(roman_string):
    if not roman_string:
        return (0)
    if not isinstance(roman_string, str):
        return (0)
    ro_num = {'I': 1,
              'V': 5,
              'X' : 10,
              'L': 50,
              'C': 100,
              'D': 500,
              'M': 1000
              }
    list_key = list(ro_num.keys())
    num = 0
    last_ro = 0
    list_ro = [0]

    for ch in roman_string:
        for r_num in list_key:
            if r_num  == ch:
                if ro_num.get(ch) <= last_ro:
                    num += subtract(list_ro)
                    list_ro = [ro_num.get(ch)]
                else:
                    list_ro.append(ro_num.get(ch))
                last_ro = ro_num.get(ch)
    num += subtract(list_ro)
    return (num)
