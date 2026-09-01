#!/usr/bin/env python3

lettre = ""
for i in range(97, 123):
    if lettre != 'e' and lettre != 'q':
        lettre += chr(i)
print(f"{lettre}")

