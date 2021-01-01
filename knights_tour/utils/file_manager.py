#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Edoardo Lenzi'
__version__ = '1.0'
__license__ = 'WTFPL2.0'


import shutil
import json
import os
from os import path

import knights_tour.utils.localizations as loc
from knights_tour.utils.logger import Logger
LOG = Logger.getLogger(__name__)
import sys 


def rmdir(dir_path):
    shutil.rmtree(dir_path)


def to_json(obj, path):
    with open(path, 'w') as outfile:
        json.dump(obj, outfile, indent = 4)


def json_stringify(obj):
    return json.dumps(obj, indent=4)


def from_json(path):
    with open(path) as json_file:
        return json.load(json_file)


def to_txt(text, path):
    with open(path, 'w') as file:
        file.write(text)


def from_txt(path):
    with open(path, 'r') as file:
        return file.read()