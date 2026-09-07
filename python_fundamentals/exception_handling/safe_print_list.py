#!/usr/bin/env python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for char in range(x):
        try:
            print("{}".format(my_list[char]), end="")
            count += 1
        except IndexError:
            break
    print()
    return count