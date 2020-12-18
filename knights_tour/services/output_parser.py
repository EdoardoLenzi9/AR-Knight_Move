from knights_tour.domain.solution import Solution
from knights_tour.domain.task import Task
from knights_tour.domain.pos import Pos
import knights_tour.utils.localizations as loc 
import knights_tour.utils.file_manager as fm

import re


class OutputParser(object):
    
    @staticmethod
    def parse(task: Task, output:str):
        if task.target == loc.CLINGO:
            return OutputParser.parse_clingo(task, output)
        else:
            return OutputParser.parse_minizinc(task, output)


    @staticmethod
    def parse_clingo(task: Task, output:str):
        checkerboard = [[0 for y in range(task.n)] for x in range(task.n)]
        tour = [None]*(task.n*task.n) 
        for m in re.findall(r'position\([0-9]+,[0-9]+,[0-9]+\)', output):
            m = m.replace("position(", "").replace(")", "")
            m = m.split(",")
            t = int(m[0])-1
            x = int(m[1])-1
            y = int(m[2])-1
            tour[t] = Pos(x,y)
            checkerboard[x][y] = t
        tour = list(filter(lambda x: x is not None, tour))
        for i in range(1, len(tour) - 1):
            assert OutputParser.valid_move(tour[i], tour[i+1])
            
        return Solution(checkerboard, task.n, task.k, len(tour))


    @staticmethod
    def valid_move(start, end):
        return (end.x == start.x + 1 and end.y == start.y + 2) or  \
               (end.x == start.x - 1 and end.y == start.y + 2) or  \
               (end.x == start.x + 1 and end.y == start.y - 2) or  \
               (end.x == start.x - 1 and end.y == start.y - 2) or  \
               (end.x == start.x + 2 and end.y == start.y + 1) or  \
               (end.x == start.x - 2 and end.y == start.y + 1) or  \
               (end.x == start.x + 2 and end.y == start.y - 1) or  \
               (end.x == start.x - 2 and end.y == start.y - 1) 


    @staticmethod
    def parse_minizinc(task: Task, output:str):
        pass