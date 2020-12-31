#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Edoardo Lenzi'
__version__ = '1.0'
__license__ = 'WTFPL2.0'


class Solution(object):
    

    def __init__(self, name: str, checkerboard: list, n: int, 
                 k: int, coverage:int, time: str = None):
        self.name = name
        self.checkerboard = checkerboard
        self.n = n
        self.k = k
        self.coverage = coverage
        self.time = time 
        self.pcoverage = (self.coverage*100)/ self.n**2
           

    def __eq__(self, other):
        return self.checkerboard == other.checkerboard and \
               self.n == other.n and \
               self.k == other.k and \
               self.coverage == other.coverage 


    def __str__(self):
        str_checkerboard = "" 
        for x in range(self.n):
            str_checkerboard += "-"*((self.n * 4) + 1) + "\n"
            for y in range(self.n):
                v = str(self.checkerboard[x][y])
                str_checkerboard += "|" + " "*(3-len(v)) + v 
            str_checkerboard += "|\n"
        str_checkerboard += "-"*((self.n * 4) + 1) + "\n"
        return f'''\n{str_checkerboard}\n| n = {self.n} | k = {self.k} | coverage = {self.coverage}, {self.pcoverage}%\n Time {self.time}\n Name {self.name}\n\n'''