#!/usr/bin/env python3

def uppercase(str):
    result = ""
    for char in str:
        code = ord(char)
        if code < 123 and code > 96:
            result += chr(code - 32)
        elif code < 91 and code > 64:
            result += char
        else:
            result += char
    print("{}".format(result))
            
