import json
from task import Task

def save_tasks(task_manager, filename="tasks.json"):
    tasks_data = [{"description": task.description, "completed": task.completed} for task in task_manager.tasks]
    with open(filename, "w") as file:
        json.dump(tasks_data, file)

def load_tasks(task_manager, filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            tasks_data = json.load(file)
            for task_data in tasks_data:
                task = Task(task_data['description'])
                if task_data['completed']:
                    task.mark_done()
                task_manager.tasks.append(task)
    except FileNotFoundError:
        pass
