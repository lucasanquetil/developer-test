import sys
import os
import unittest

sys.path.insert(0, os.getcwd())
from src.model import journey


class TestJourney(unittest.TestCase):
    def setUp(self) -> None:
        self.journey = journey.Journey(autonomy_max=10, departure='France')

    def test_journey_is_instance_of_journey(self):
        self.assertIsInstance(self.journey, journey.Journey)

    def test_journey_time_before_refuel_is_int(self):
        self.assertIsInstance(self.journey.get_time_before_refuel(), int)

    def test_journey_current_planet_is_string(self):
        self.assertIsInstance(self.journey.get_current_planet(), str)

    def test_journey_refuel_plan_is_list(self):
        self.assertIsInstance(self.journey.get_refuel_plan(), list)

    def test_journey_waiting_plan_is_list(self):
        self.assertIsInstance(self.journey.get_waiting_plan(), list)

    def test_journey_travel_plan_is_list(self):
        self.assertIsInstance(self.journey.get_travel_plan(), list)

    def test_journey_days_is_integer(self):
        self.assertIsInstance(self.journey.get_days(), int)

    def test_journey_odds_is_integer(self):
        self.assertIsInstance(self.journey.get_odd(), int)

    def test_journey_days_is_positive(self):
        self.assertGreaterEqual(self.journey.get_days(), 0)

    def test_journey_odds_is_positive(self):
        self.assertGreaterEqual(self.journey.get_odd(), 0)

    def test_journey_travel_plan_is_of_right_format(self):
        for checkpoint in self.journey.get_travel_plan():
            self.assertIsInstance(checkpoint[0], str)
            self.assertIsInstance(checkpoint[1], int)

    def test_journey_waiting_plan_is_of_right_format(self):
        for checkpoint in self.journey.get_travel_plan():
            self.assertIsInstance(checkpoint[0], str)
            self.assertIsInstance(checkpoint[1], int)

    def test_journey_refuel_plan_is_of_right_format(self):
        for checkpoint in self.journey.get_travel_plan():
            self.assertIsInstance(checkpoint[0], str)
            self.assertIsInstance(checkpoint[1], int)


if __name__ == '__main__':
    unittest.main()
