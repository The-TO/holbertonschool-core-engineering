#!/usr/bin/env python3
"""Module for open a file"""


def write_file(filename="", text=""):
    """Fonction to write a file"""
    with open(filename, "w", encoding="utf-8") as f:
        content = f.write(text)

    return content
