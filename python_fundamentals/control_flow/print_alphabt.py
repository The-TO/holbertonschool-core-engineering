#!/usr/bin/env python3

lettre = ""
for i in range(97, 123):
    if i != ord('e') and i != ord('q'):
        lettre += chr(i)
print(f"{lettre}")
