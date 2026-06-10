"""
validation.py - Input validation functions for the Task Manager application.
"""
 
from datetime import datetime
 
 
def validate_task_title(title):
    if not title or not isinstance(title, str):
        raise ValueError("Error: Title cannot be empty.")
 
    if len(title) < 3:
        raise ValueError("Error: Title must be at least 3 characters long.")
 
    if len(title) > 100:
        raise ValueError("Error: Title must not exceed 100 characters.")
 
    return True
 
 
def validate_task_description(description):
    if not description or not isinstance(description, str):
        raise ValueError("Error: Description cannot be empty.")
 
    if len(description) < 5:
        raise ValueError("Error: Description must be at least 5 characters long.")
 
    if len(description) > 500:
        raise ValueError("Error: Description must not exceed 500 characters.")
 
    return True
 
 
def validate_due_date(due_date):
    if not due_date or not isinstance(due_date, str):
        raise ValueError("Error: Due date cannot be empty.")
 
    if len(due_date) != 10:
        raise ValueError("Error: Due date must be in YYYY-MM-DD format (e.g., 2024-06-26).")
 
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Error: Invalid date. Please use YYYY-MM-DD format (e.g., 2024-06-26).")
 
    return True