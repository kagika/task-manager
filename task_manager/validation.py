"""
validation.py - Input validation functions for the Task Manager application.
"""
 
from datetime import datetime
 
 
def validate_task_title(title):
    """
    Validate the task title.
 
    Args:
        title (str): The task title to validate.
 
    Returns:
        tuple: (bool, str) - (is_valid, error_message)
    """
    if not title or not isinstance(title, str):
        return False, "Error: Title cannot be empty."
 
    if len(title) < 3:
        return False, "Error: Title must be at least 3 characters long."
 
    if len(title) > 100:
        return False, "Error: Title must not exceed 100 characters."
 
    return True, ""
 
 
def validate_task_description(description):
    """
    Validate the task description.
 
    Args:
        description (str): The task description to validate.
 
    Returns:
        tuple: (bool, str) - (is_valid, error_message)
    """
    if not description or not isinstance(description, str):
        return False, "Error: Description cannot be empty."
 
    if len(description) < 5:
        return False, "Error: Description must be at least 5 characters long."
 
    if len(description) > 500:
        return False, "Error: Description must not exceed 500 characters."
 
    return True, ""
 
 
def validate_due_date(due_date):
    """
    Validate the due date string (expected format: YYYY-MM-DD).
 
    Args:
        due_date (str): The due date string to validate.
 
    Returns:
        tuple: (bool, str) - (is_valid, error_message)
    """
    if not due_date or not isinstance(due_date, str):
        return False, "Error: Due date cannot be empty."
 
    if len(due_date) != 10:
        return False, "Error: Due date must be in YYYY-MM-DD format (e.g., 2024-06-26)."
 
    try:
        parsed_date = datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        return False, "Error: Invalid date. Please use YYYY-MM-DD format (e.g., 2024-06-26)."
 
    if parsed_date.date() < datetime.today().date():
        return False, "Error: Due date cannot be in the past."
 
    return True, ""