#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Edoardo Lenzi'
__version__ = '1.0'
__license__ = 'WTFPL2.0'


from knights_tour.domain.pos import Pos
import knights_tour.utils.localizations as loc
import os


class Task(object):
    

    def __init__(self, name: str, target: str, n: int, k: int, 
                 knight1: Pos, knight2: Pos, occ: list, params: dict):
        self.name = name
        self.target = target
        self.n = n
        self.k = k
        self.knight1 = knight1
        self.knight2 = knight2
        self.occ = occ
        self.params = params
        self.folder = loc.abs_path([loc.LOGS_PATH, name])
        try:
            os.mkdir(self.folder)
        except: pass 
           

    def __eq__(self, other):
        return self.name == other.name and \
               self.target == other.target and \
               self.n == other.n and \
               self.k == other.k and \
               self.knight1 == other.knight1 and \
               self.knight2 == other.knight2 and \
               self.occ == other.occ and \
               self.params == other.params