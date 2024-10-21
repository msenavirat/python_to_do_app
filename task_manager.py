
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        new_task = Task(description)
        self.tasks.append(new_task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)     
            
    def list_tasks(self):
        for idx, task in enumerate(self.tasks):
            print(f"{idx + 1}. {task}")

    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()

    def mark_task_undone(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_undone()

    def list_completed_tasks(self):
        completed_tasks = [task for task in self.tasks if task.completed]
        for task in completed_tasks:
            print(task)
