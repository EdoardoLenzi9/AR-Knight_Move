#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Edoardo Lenzi'
__version__ = '1.0'
__license__ = 'WTFPL2.0'


from knights_tour.cli import Parser
from knights_tour.cli_handler import CliHandler


args = Parser().parse()    
CliHandler(args)