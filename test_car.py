from unittest import TestCase
from car import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car()

    def test_addition(self):
        self.assertEqual(self.car.addition(1, 1), 2)
