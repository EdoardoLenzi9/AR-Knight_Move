from knights_tour.domain.task import Task
from knights_tour.domain.pos import Pos
import knights_tour.utils.file_manager as fm
import knights_tour.utils.localizations as loc

import re 
import os 

class ModelBuilder(object):


    @staticmethod
    def build_model(task: Task):
        if task.target == loc.CLINGO:
            ModelBuilder.build_clingo_model(task)
        else:
            ModelBuilder.build_minizinc_model(task)


    @staticmethod
    def build_clingo_model(task: Task):
        model = fm.from_txt(loc.CLINGO_MODEL_PATH)
        for m in re.findall(r'\[\[[a-zA-Z_]+\]\]', model):
            model = model.replace(m, task.params[m.replace("[[", "").replace("]]", "")])
        fm.to_txt(model, os.path.join(task.folder, loc.CLINGO_MODEL))

        database = ""
        for o in task.occ:
            database += f"position(1,{o.x},{o.y}).\n"
        database += f"position(2,{task.knight1.x},{task.knight1.y}).\n"
        database += f"position(3,{task.knight2.x},{task.knight2.y}).\n"
        fm.to_txt(database, os.path.join(task.folder, loc.CLINGO_DATABASE))


    @staticmethod
    def build_minizinc_model(task: Task):
        model = fm.from_txt(loc.MINIZINC_MODEL_PATH)
        for m in re.findall(r'\[\[[a-zA-Z_]+\]\]', model):
            model = model.replace(m, task.params[m.replace("[[", "").replace("]]", "")])
        fm.to_txt(model, os.path.join(task.folder, loc.MINIZINC_MODEL))

        database = f"""n = {task.n};
initial_occ = array2d(CELL_DOMAIN, CELL_DOMAIN, ["""
        for x in range(1, task.n+1):
            for y in range(1, task.n+1):
                value = next(filter(lambda p: p.x == x and p.y == y, task.occ), None)      
                value = 0 if value is None else 1
                if task.knight1.x == x and task.knight1.y == y:
                    value = 2
                if task.knight2.x == x and task.knight2.y == y:
                    value = 3
                database += f" {value},"
            database += "\n" + "\t"*12 + " "
        database += "]);"
        fm.to_txt(database, os.path.join(task.folder, loc.MINIZINC_DATABASE))