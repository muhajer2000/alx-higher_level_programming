#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    j = list_length
    result_list = []
    while i < j:

        try:
            num = my_list_1[i] / my_list_2[i]
            result_list.append(num)
        except TypeError:
            result_list.append(0)
            print("wrong type")
        except ZeroDivisionError:
            result_list.append(0)
            print("division by 0")
        except IndexError:
            result_list.append(0)
            print("out of range")
        finally:
            pass
        i += 1

    return (result_list)
