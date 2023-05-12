import pytest
from src.task import Task


def test_constructors_of_task():
    task1 = Task('Inventory')
    task2 = Task('', True)
    assert task1.get_description() == 'Inventory'
    assert task1.get_done() == False
    assert task1.get_id() == 4

    assert task2.get_description() == ''
    assert task2.get_done() == True
    assert task2.get_id() == 5


def test_create_task():
    task3 = Task()
    task3.set_description('Mula')
    assert task3.get_done() is False
    task3.set_done()
    assert task3 is not None
    assert type(task3.get_description()) is str
    assert task3.get_done() is not False
    assert task3.get_id() is 6
    assert type(task3.get_id()) is int
