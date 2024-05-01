#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    tupl_list = []
    num = 0
    number = 0
    mult = 0
    for tupl in my_list:
        num = tupl[0] * tupl[1]
        tupl_list.append(num)
        number += tupl[1]
    for mul in tupl_list:
        mult += mul
    return (mult / number)
