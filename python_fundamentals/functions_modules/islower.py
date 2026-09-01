#!/usr/bin/env python3

def islower(c):
    char = ord(c)
    if char < 123 and char > 96:
        return True
    else:
        return False
