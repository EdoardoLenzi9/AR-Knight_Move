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
import knights_tour.utils.localizations as loc
from knights_tour.domain.pos import Pos
from knights_tour.domain.task import Task
from knights_tour.services.command_builder import CommandBuilder
from knights_tour.services.model_builder import ModelBuilder
from knights_tour.services.output_parser import OutputParser

from os import path
import subprocess
import random
import time 
import sys
import os 


class CliHandler(object):

    '''Cli business logic, given the arguments typed
    calls the right handlers/procedures of the pipeline'''


    def __init__(self, args):
        if args.generate is not None:
            self.generate_handler(args.generate[0])
        elif args.run is not None:
            self.run_handler(args.run[0])
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
        try:
            fm.rmdir(loc.LOGS_PATH)
        except: pass
        os.mkdir(loc.LOGS_PATH)


    def generate_handler(self, json_filename):
        clingo_params = [{ "varchoice": "varchoice"}, 
                         {"...": "..." }]
        minizinc_params = [{ "solver": "gecode"}, 
                           {"allsolutions": "--all-solutions" }, 
                           {"timeout": "--solver-time-limit 300000" }]
        tasks = []
        for n in [8, 10, 12, 14, 16]:
            for i in range(0,20):
                k = random.randint(4, 10)
                counter = 0
                occ = []
                mtx = [[False for y in range(1,n+1)] for x in range(1,n+1)]
                while counter < k + 2:
                    x = random.randint(1, n)
                    y = random.randint(1, n)
                    if not mtx[x-1][y-1]:
                        mtx[x-1][y-1] = True 
                        occ.append({"x": x, "y": y})
                        counter += 1
                knight1 = occ.pop()
                knight2 = occ.pop()
                for target in [loc.MINIZINC, loc.CLINGO]:
                    tasks.append({
                        "name": f"{i}_{n}x{n}_{target}",
                        "target": target,
                        "n": n,
                        "k": k,
                        "knight1": knight1,
                        "knight2": knight2,
                        "occ": occ,
                        "params": clingo_params if target == loc.CLINGO else minizinc_params
                    })
        fm.to_json(tasks, loc.abs_path([loc.RUNS_PATH, json_filename]))


    def run_handler(self, json_filename):
        json = fm.from_json(loc.abs_path([loc.RUNS_PATH, json_filename]))
        for t in json:
            knight1 = Pos(t["knight1"]["x"], t["knight1"]["y"])
            knight2 = Pos(t["knight2"]["x"], t["knight2"]["y"])
            params = {}
            for p in t['params']:
                for k in p.keys():
                    params[k] = p[k]

            occ = []
            for o in t["occ"]:
                occ.append(Pos(o["x"], o["y"]))
            task = Task( t["name"],
                         t["target"],
                         t["n"],
                         t["k"],
                         knight1,
                         knight2,
                         occ,
                         params )
            self.task_handler(task)


    def task_handler(self, task: Task):
        
        print(f"\n\nTask {task.name} started")
        ModelBuilder.build_model(task) 
        command = CommandBuilder.build_command(task) 
        
        output = self.run_command(command)   
        fm.to_txt(output, loc.abs_path([loc.LOGS_PATH, task.name+".log"]))
        solution = OutputParser.parse(task, output)
        print(solution)


    def run_command(self, command: str):
        command = ' '.join([command])
        start_time = time.time()
        output = ""
        with subprocess.Popen( command, 
                               shell=True, 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.STDOUT) as process:
            while process.poll() is None:
                time.sleep(1)
                for line in iter(process.stdout.readline, b''):
                    line = str(line, 'utf-8')
                    output += line
            print("Task ended in: " + str(int(time.time()-start_time)) + " sec\n\n")
            process.kill()
        return output
        

# Used when spawned in a new process

if __name__ == '__main__':
    LOG.info(f'Subprocess started {sys.argv}')
    sys.stdout.flush()
    from knights_tour.cli import Parser
    args = Parser().parse()    
    CliHandler(args)