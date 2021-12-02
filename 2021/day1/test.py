import unittest

from solution import Sonar


class TestPart1(unittest.TestCase):

    def test_example(self):
        data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        sonar = Sonar(data)
        self.assertEqual(7, sonar.get_increase_count())

    def test_large_input(self):
        sonar = Sonar(_get_large_data())
        print(sonar.get_increase_count())


class TestPart2(unittest.TestCase):

    def test_example(self):
        data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        sonar = Sonar(data)
        self.assertEqual(5, sonar.get_three_measurement_increase_count())

    def test_large_input(self):
        sonar = Sonar(_get_large_data())
        print(sonar.get_three_measurement_increase_count())


def _get_large_data():
    with open('large_input') as file:
        lines = file.readlines()
    data = [int(line) for line in lines]
    return data
