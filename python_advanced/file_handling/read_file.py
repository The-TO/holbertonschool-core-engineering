#!/usr/bin/env python3
"""Module for open a file"""

def read_file(filename=""):
    """Fonction to read a file"""
    with open(filename,"r" ,encoding="utf-8") as f:
        content = f.read()

    print(content)