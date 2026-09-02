#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    for lists in matrix:
        for number in range(len(lists)):
            if (number < len(lists) - 1):
                print("{:d}".format(lists[number]),  end=" ")
            else:
                print("{:d}".format(lists[number]),  end="")
        print()
