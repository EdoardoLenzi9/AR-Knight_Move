#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Edoardo Lenzi'
__version__ = '1.0'
__license__ = 'WTFPL2.0'


from dotenv import load_dotenv
import json
import os 



class Env(object):

    LOG_LEVEL = 'LOG_LEVEL'
    MINIZINC = 'MINIZINC'


    @staticmethod
    def load():
        '''setup environment from .env configs'''

        load_dotenv(os.path.join(os.path.abspath('.'), '.env'))


    @staticmethod
    def get_value(key: str) -> str:
        return os.environ[key]


    @staticmethod
    def set_value(key: str, value: str) -> None:
        os.environ[key] = value