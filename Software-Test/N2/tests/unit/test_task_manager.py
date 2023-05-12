import pytest
from src.task_manager import TaskManager

manager = TaskManager()


def test_should_not_equals_none():
    assert manager is not None


def test_should_add_task_in_list():
    manager.add_task('Testing1')
    assert manager.tasks[0] is 'Testing1'

# since the method list_tasks() is based on the get_description() method of tasks
# it will be implemented in the integration test


def test_should_count_all_tasks():
    manager.add_task('Compromise')
    manager.add_task('Faith')
    assert len(manager.tasks) == 3
    assert manager.tasks[0] == 'Testing1'
    assert manager.tasks[1] == 'Compromise'
    assert manager.tasks[2] == 'Faith'

# since there is no literal object task, I can't mark then as done since it uses the method set_done()
# from the Task class, remove won't work as well - both are based on IDs -
# But I can remove these items based on index to check the functionality of the list in the class


def test_should_remove_a_task():
    manager.tasks.pop(0)
    assert manager.tasks[0] == 'Compromise'
