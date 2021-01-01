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
        '''
        import knights_tour.utils.file_manager as fm
        import knights_tour.utils.localizations as loc
        import subprocess
        import os
        import time 

        command = [f'clingo asp/knights_tour.lp -c n=8']
        process = subprocess.Popen(' '.join(command), shell=True, 
                                   stdout=subprocess.PIPE, 
                                   stderr=subprocess.STDOUT)
        output = ""
        while process.poll() is None:
            time.sleep(1)
            for line in iter(process.stdout.readline, b''):
                line = str(line, 'utf-8')
                output += line
        fm.to_txt(output, loc.abs_path([loc.LOGS_PATH, "clingo.log"]))
        '''

    def test(self):
        command = '--run lp.json'.split()
        #command = '--generate ciao.json'.split()
        
        args = Parser().parse_args(command)    
        CliHandler(args)