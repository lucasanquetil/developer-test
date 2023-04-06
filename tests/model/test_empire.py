import sys
import os
import unittest

sys.path.insert(0, os.getcwd())
from src.model import empire


class TestEmpire(unittest.TestCase):
    def setUp(self) -> None:
        self.empire = empire.Empire(countdown=10, bounty_hunters=[{'planet': 'France', 'day': 8}])

    def test_empire_is_instance_of_empire(self):
        self.assertIsInstance(self.empire, empire.Empire)

    def test_empire_bounty_hunter_is_list(self):
        self.assertIsInstance(self.empire.get_bounty_hunters(), list)

    def test_empire_countdown_is_int(self):
        self.assertIsInstance(self.empire.get_countdown(), int)

    def test_empire_countdown_is_positive(self):
        self.assertGreater(self.empire.get_countdown(), 0)

    def test_empire_bounty_hunter_entry_is_of_right_format(self):
        for bounty_hunter in self.empire.get_bounty_hunters():
            self.assertIn("planet", bounty_hunter)
            self.assertIn("day", bounty_hunter)


if __name__ == '__main__':
    unittest.main()
