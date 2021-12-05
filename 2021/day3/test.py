import unittest

from solution import Submarine


class TestPart1(unittest.TestCase):

    def test_example(self):
        data = [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]
        s = Submarine(data)
        self.assertEqual(198, s.get_power_consuption())

    def test_large_input(self):
        data = read_input()
        s = Submarine(data)
        print(s.get_power_consuption())


class TestPart2(unittest.TestCase):

    def test_example(self):
        data = [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]
        s = Submarine(data)
        self.assertEqual(230, s.get_life_support_rating())

    def test_large_input(self):
        data = read_input()
        s = Submarine(data)
        print(s.get_life_support_rating())


def read_input():
    with open('input') as file:
        lines = file.readlines()
    data = [line.strip() for line in lines]
    return data
