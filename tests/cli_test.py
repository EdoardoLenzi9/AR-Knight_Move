#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Edoardo Lenzi'
__version__ = '1.0'
__license__ = 'WTFPL2.0'


import unittest

from knights_tour.cli_handler import CliHandler
from knights_tour.cli import Parser


class CliTest(unittest.TestCase):


    def setUp(self):
        '''test fixture''' 


    def test_mzn_4(self):
        command = '--run benchmark.json'.split()
        args = Parser().parse_args(command)    
        CliHandler(args)


#    def test_lp_4(self):
#        command = '--run lp_4.json'.split()
#        args = Parser().parse_args(command)    
#        CliHandler(args)