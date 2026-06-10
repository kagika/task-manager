"""
task_utils.py - Core task management functions for the Task Manager application.
"""
 
from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)
 
 
def add_task(tasks, title, description, due_date):
    """
    Add a new task to the tasks list after validating all inputs.
 
    Args:
        tasks (list): The current list of task dictionaries.
        title (str): The title of the task.
        description (str): A description of the task.
        due_date (str): The due date in YYYY-MM-DD format.
 
    Returns:
        tuple: (bool, str) - (success, message)
    """
    is_valid, error = validate_task_title(title)
    if not is_valid:
        return False, error
 
    is_valid, error = validate_task_description(description)
    if not is_valid:
        return False, error
 
    is_valid, error = validate_due_date(due_date)
    if not is_valid:
        return False, error
 
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False,
    }
    tasks.append(task)
    return True, f"Task '{title}' added successfully!"
 
 
def mark_task_as_complete(tasks, title):
    """
    Mark a task as complete by its title.
 
    Args:
        tasks (list): The current list of task dictionaries.
        title (str): The title of the task to mark as complete.
 
    Returns:
        tuple: (bool, str) - (success, message)
    """
    if not title or not isinstance(title, str):
        return False, "Error: Please provide a valid task title."
 
    for task in tasks:
        if task["title"].lower() == title.lower():
            if task["completed"]:
                return False, f"Task '{task['title']}' is already marked as complete."
            task["completed"] = True
            return True, f"Task '{task['title']}' marked as complete!"
 
    return False, f"Error: No task found with the title '{title}'."
 
 
def view_pending_tasks(tasks):
    """
    Retrieve all tasks that have not yet been completed.
 
    Args:
        tasks (list): The current list of task dictionaries.
 
    Returns:
        list: A list of pending (incomplete) task dictionaries.
    """
    pending = [task for task in tasks if not task["completed"]]
    return pending
 
 
def calculate_progress(tasks):
    """
    Calculate the percentage of tasks that have been completed.
 
    Args:
        tasks (list): The current list of task dictionaries.
 
    Returns:
        tuple: (int completed, int total, float percentage)
    """
    total = len(tasks)
    if total == 0:
        return 0, 0, 0.0
 
    completed = sum(1 for task in tasks if task["completed"])
    percentage = (completed / total) * 100
    return completed, total, percentage
