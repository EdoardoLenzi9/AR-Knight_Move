#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Edoardo Lenzi'
__version__ = '1.0'
__license__ = 'WTFPL2.0'

# load .env configs
from knights_tour.utils.env import Env
Env.load()

from knights_tour.utils.logger import Logger
LOG = Logger.getLogger(__name__)

import knights_tour.utils.file_manager as fm

from os import path
import sys
import os 


class CliHandler(object):

    '''Cli business logic, given the arguments typed
    calls the right handlers/procedures of the pipeline'''


    def __init__(self, args):
        if args.run is not None:
            pass
            #self.run_handler(args.run[0])
        elif args.clean:
            self.clean_handler()
        else:
            self.default_handler()


    # Command Handlers 

    def default_handler(self):
        LOG.info('Welcome to Knights Tour script! Type -h for help \n\n' +
                 '[You have to type at least one command of the pipeline]\n')


    def clean_handler(self):
        LOG.info('clean')
        fm.rmdir('tmp')

    
   
# Used when spawned in a new process

if __name__ == '__main__':
    LOG.info(f'Subprocess started {sys.argv}')
    sys.stdout.flush()
    from knights_tour.cli import Parser
    args = Parser().parse()    
    CliHandler(args)