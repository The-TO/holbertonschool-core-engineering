#!/usr/bin/env python3
"""Module for open a file"""


def append_write(filename="", text=""):
    """Fonction to write a file"""
    with open(filename, "a", encoding="utf-8") as f:
        content = f.write(text)

    return content
