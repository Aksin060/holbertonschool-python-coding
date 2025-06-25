#!/usr/bin/python3
'''Salam'''


class Square:
    '''Salam'''
    def __init__(self, size):
        if isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
