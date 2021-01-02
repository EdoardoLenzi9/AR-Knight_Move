#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Edoardo Lenzi'
__version__ = '1.0'
__license__ = 'WTFPL2.0'


import os
import json


'''Localization keys and files'''


def abs_path(relative_path: list) -> str:

    ''' given an array of localizations (relative path) 
    returns and absolute path starting from cwd '''

    abs_path = os.getcwd()
    for p in relative_path:
        abs_path = os.path.join(abs_path, p)
    if os.path.isdir(abs_path) and not os.path.exists(abs_path):
        os.mkdir(abs_path)
    return abs_path


# String Localizations

MINIZINC = 'minizinc'
CLINGO = 'clingo'


# Files Localizations

ASSETS = 'assets'
RUNS = 'runs'
LOGS = 'logs'
ASP = 'asp'

CLINGO_MODEL = "knights_tour.lp"
CLINGO_DATABASE = "database.lp"
MINIZINC_MODEL = "knights_tour.mzn"
MINIZINC_DATABASE = "database.dzn"
CLINGO_CMD = 'clingo.sh'
MINIZINC_CMD = 'minizinc.sh'


RUNS_PATH = abs_path([ASSETS, RUNS])
LOGS_PATH = abs_path([ASSETS, LOGS])
CLINGO_MODEL_PATH = abs_path([ASP, CLINGO_MODEL])
CLINGO_DATABASE_PATH = abs_path([ASP, CLINGO_DATABASE])
MINIZINC_MODEL_PATH = abs_path([MINIZINC, MINIZINC_MODEL])
MINIZINC_DATABASE_PATH = abs_path([MINIZINC, MINIZINC_DATABASE])
CLINGO_CMD_PATH = abs_path([ASP, CLINGO_CMD])
MINIZINC_CMD_PATH = abs_path([MINIZINC, MINIZINC_CMD])