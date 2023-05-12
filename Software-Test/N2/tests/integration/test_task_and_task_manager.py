import pytest
from src.task import Task
from src.task_manager import TaskManager

manager = TaskManager()
task4 = Task('Settled before')
task5 = Task('', True)
task6 = Task()


def test_id_values():
    assert task4.get_id() == 1
    assert task5.get_id() == 2
    assert task6.get_id() == 3


def test_should_add_tasks():
    manager.add_task(task4)
    manager.add_task(task5)
    manager.add_task(task6)
    assert len(manager.tasks) == 3


def test_should_list_tasks():
    assert manager.list_tasks() == ['Settled before', '', '']


def test_should_make_task_done():
    manager.mark_task_done(1)
    manager.mark_task_done(3)
    for task in manager.tasks:
        assert task.get_done() == True


def test_should_delete_task():
    manager.remove_task(2)
    assert len(manager.list_tasks()) == 2
    assert manager.tasks[0] == task4
    assert manager.tasks[1] == task6
