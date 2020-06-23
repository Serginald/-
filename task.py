from dataclasses import dataclass

from numpy import random as rnd


@dataclass()
class TaskData:
    time: int = None
    task_type: int = None

class Task():
    def __init__(self):
        time_work = [3, 6, 9]
        task_type = rnd.randint(high=3, low=0)
        self.current_task = TaskData()
        self.current_task.time = time_work[task_type]
        self.current_task.task_type = task_type


    def get_time(self):
        return self.current_task.time

    def get_type(self):
        return self.current_task.task_type