#!/usr/bin/env python3

def pow(a, b):
    if b < 0:
        result = 1
        for i in range(-b):
            result = result * a
        return 1 / result
    
    else:
        result = 1
        for i in range(b):
            result = result * a
    return result

