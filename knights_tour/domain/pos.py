#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Edoardo Lenzi'
__version__ = '1.0'
__license__ = 'WTFPL2.0'


class Pos(object):
    

    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y
           

    def __eq__(self, other):
        return self.x == other.x and \
               self.y == other.y