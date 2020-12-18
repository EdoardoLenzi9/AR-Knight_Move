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


# Files Localizations

ASSETS = 'assets'
RUNS = 'runs'
LOGS = 'logs'

RUNS_PATH = abs_path([ASSETS, RUNS])
LOGS_PATH = abs_path([ASSETS, LOGS])


# String Localizations

MINIZINC = 'minizinc'
CLINGO = 'clingo'

# Commands Localizations

CLINGO_CMD = '''clingo [[path]] -c n=[[n]] --time-limit=300'''