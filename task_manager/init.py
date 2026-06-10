"""
task_manager package - A simple task management system.
"""

from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress,
)

from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)