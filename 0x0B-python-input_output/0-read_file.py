#!/usr/bin/python3
def read_file(filename="workfile"):
    """A function that reads a text file and prints it to stdout"""
    """Args:
    filename: the name of the file to be printed
    """
    with open('workfile', "r" encoding="utf-8") as f:
        content = f.read()
        print(content)
