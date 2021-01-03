#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Edoardo Lenzi'
__version__ = '1.0'
__license__ = 'WTFPL2.0'


import argparse
import sys
import os 

from knights_tour.cli_handler import CliHandler


class Parser(object):
    '''Cli entry point of the script, based on the library argparse
    see also: https://docs.python.org/3.9/library/argparse.html'''

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter, 
            description = '''                              Welcome to Knights Tour Script :)  

+-----------------------------------------------------------------------------------------------------------------------------+
|                                                                                       ,----,                                | 
|        ,--.                                                                         ,/   .`|                                | 
|    ,--/  /|                                 ,---,        ___                      ,`   .'  :                                | 
| ,---,': / '              ,--,             ,--.' |      ,--.'|_                  ;    ;     /                                | 
| :   : '/ /       ,---, ,--.'|             |  |  :      |  | :,'               .'___,/    ,'  ,---.           ,--,   __  ,-. | 
| |   '   ,    ,-+-. /  ||  |,     ,----._,.:  :  :      :  : ' :  .--.--.      |    :     |  '   ,'\        ,'_ /| ,' ,'/ /| | 
| '   |  /    ,--.'|'   |`--'_    /   /  ' /:  |  |,--..;__,'  /  /  /    '     ;    |.';  ; /   /   |  .--. |  | : '  | |' | | 
| |   ;  ;   |   |  ,"' |,' ,'|  |   :     ||  :  '   ||  |   |  |  :  /`./     `----'  |  |.   ; ,. :,'_ /| :  . | |  |   ,' | 
| :   '   \  |   | /  | |'  | |  |   | .\  .|  |   /' ::__,'| :  |  :  ;_           '   :  ;'   | |: :|  ' | |  . . '  :  /   | 
| |   |    ' |   | |  | ||  | :  .   ; ';  |'  :  | | |  '  : |__ \  \    `.        |   |  ''   | .; :|  | ' |  | | |  | '    | 
| '   : |.  \|   | |  |/ '  : |__'   .   . ||  |  ' | :  |  | '.'| `----.   \       '   :  ||   :    |:  | : ;  ; | ;  : |    | 
| |   | '_\.'|   | |--'  |  | '.'|`---`-'| ||  :  :_:,'  ;  :    ;/  /`--'  /       ;   |.'  \   \  / '  :  `--'   \|  , ;    | 
| '   : |    |   |/      ;  :    ;.'__/\_: ||  | ,'      |  ,   /'--'.     /        '---'     `----'  :  ,      .-./ ---'     | 
| ;   |,'    '---'       |  ,   / |   :    :`--''         ---`-'   `--'---'                            `--`----'              | 
| '---'                   ---`-'   \   \  /                                                                                   | 
|                                   `--`-'                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------+''',
            epilog = 'Source: https://github.com/EdoardoLenzi9/AR-Knights_Tour' )


        self.parser.add_argument('-c', '--clean', dest='clean', action='store_const',
                                const=True, default=False,
                                help='Clean temporary/useless files')


        self.parser.add_argument('--generate', dest='generate', metavar='N', type=str, nargs=1,
                                help='Generate a new random benchmark (run) with the specified name')


        self.parser.add_argument('--run', dest='run', metavar='N', type=str, nargs=1,
                                help='Run an array of tasks (remember to specify the name of your run .json)')


        self.parser.add_argument('--eval', dest='eval', metavar='N', type=str, nargs=1,
                                help='Evaluate the results of a benchmark (remember to specify the name of your run .json)')
                                


    def parse(self):    
        return self.parser.parse_args()


    def parse_args(self, command):    
        return self.parser.parse_args(command)