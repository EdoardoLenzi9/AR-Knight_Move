from knights_tour.domain.task import Task
from knights_tour.domain.pos import Pos
import knights_tour.utils.localizations as loc


class CommandBuilder(object):
    
    @staticmethod
    def build_command(task: Task):
        if task.target == loc.CLINGO:
            return CommandBuilder.build_clingo_command(task)
        else:
            return CommandBuilder.build_mzn_command(task)


    @staticmethod
    def build_mzn_command(task: Task):
        return "ls -la"


    @staticmethod
    def build_clingo_command(task: Task):
        cmd = loc.CLINGO_CMD
        cmd = cmd.replace('[[n]]', str(task.n))
        cmd = cmd.replace('[[path]]', 'asp/knights_tour.lp')
        return cmd