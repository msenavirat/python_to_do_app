
# To-Do List CLI Application

## Overview

This is a command-line interface (CLI) To-Do List application built with Python that allows users to manage tasks efficiently. The project follows modular design principles and utilizes Object-Oriented Programming (OOP) concepts such as classes, methods, and encapsulation.

### Features

- **Add tasks**: Create a new task and add it to the list.
- **Remove tasks**: Delete tasks from the list using their index.
- **Mark tasks as done/undone**: Track tasks' completion status.
- **View all tasks**: Display all tasks with their completion status.
- **View completed tasks**: Display only the tasks marked as done.
- **Save tasks to a file**: Persist tasks in a JSON file across sessions.
- **Load tasks from a file**: Automatically load tasks when starting the application.

## Prerequisites

- Python 3.x
- pandas library (for future improvement)

Install pandas using:
```bash
pip install pandas
```

## Getting Started

1. Clone this repository or download the files.
2. Navigate to the project directory in your terminal.
3. Run the main script:
```bash
python todo.py
```

## Usage

The application provides the following menu:

```
1. Add Task
2. Remove Task
3. Mark Task as Done
4. Mark Task as Undone
5. List All Tasks
6. List Completed Tasks
7. Save and Exit
```

### Example Flow:

1. **Add a Task**:
   - Select option 1 and provide the task description (e.g., "Buy groceries").
   - The task is added as a pending task.

2. **Mark a Task as Done**:
   - Choose option 3 and provide the task number to mark it as done.

3. **Save and Exit**:
   - Choose option 7 to save the tasks to a file and exit the application.

## File Structure

```
.
├── todo.py              # Main script to run the application
├── task.py              # Task class definition (OOP concept)
├── task_manager.py      # TaskManager class to handle task operations
├── file_ops.py          # Handles file saving and loading
└── tasks.json           # JSON file storing the task data

```

## Object-Oriented Programming (OOP) Concepts

The application makes use of several OOP principles:

### 1. **Classes and Objects**
   - **Classes** like `Task` and `TaskManager` represent objects that model tasks and manage them.
   - **Objects** are instances of these classes.

### 2. **Encapsulation**
   - The properties and methods related to tasks are grouped together in classes, providing a clear structure and interface.

### 3. **Abstraction**
   - Complex functionality like saving/loading tasks or managing task lists is abstracted behind simple methods.

### 4. **Method Overriding (Special Methods)**
   - The `__str__` method in `Task` class is overridden to provide a custom string representation of the task (e.g., "Buy groceries [Pending]").

## Future Development

- **pandas Integration**: We plan to use pandas DataFrames to display tasks in a tabular format for better readability and manipulation of task data.


