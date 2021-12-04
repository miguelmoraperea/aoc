import unittest

from solution import Submarine
from commands_1 import FactoryPart1
from commands_2 import FactoryPart2


class TestPart1(unittest.TestCase):

    def test_example(self):
        course = "forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2\n"
        sub = Submarine(FactoryPart1())
        res = sub.get_end_position(course)
        self.assertEqual(150, res)

    def test_large_input(self):
        course = read_input()
        sub = Submarine(FactoryPart1())
        print(sub.get_end_position(course))


class TestPart2(unittest.TestCase):

    def test_example(self):
        course = "forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2\n"
        sub = Submarine(FactoryPart2())
        res = sub.get_end_position(course)
        self.assertEqual(900, res)

    def test_large_input(self):
        course = read_input()
        sub = Submarine(FactoryPart2())
        print(sub.get_end_position(course))


def read_input():
    with open('input') as file:
        lines = file.readlines()
    data = [int(line) for line in lines]
    return data
