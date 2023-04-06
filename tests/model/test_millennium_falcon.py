import sys
import os
import unittest

sys.path.insert(0, os.getcwd())
from src.model import millennium_falcon


class TestMillenniumFalcon(unittest.TestCase):
    def setUp(self) -> None:
        self.millennium_falcon = millennium_falcon.MillenniumFalcon(autonomy=10, departure='France', arrival='USA',
                                                                    routes=[('France', 'UK', 1), ('UK', 'USA', 7)])

    def test_millennium_falcon_is_instance_of_millennium_falcon(self):
        self.assertIsInstance(self.millennium_falcon, millennium_falcon.MillenniumFalcon)

    def test_millennium_falcon_autonomy_is_int(self):
        self.assertIsInstance(self.millennium_falcon.get_autonomy(), int)

    def test_millennium_falcon_departure_is_string(self):
        self.assertIsInstance(self.millennium_falcon.get_departure(), str)

    def test_millennium_falcon_arrival_is_string(self):
        self.assertIsInstance(self.millennium_falcon.get_arrival(), str)

    def test_millennium_falcon_routes_is_list(self):
        self.assertIsInstance(self.millennium_falcon.get_routes(), list)

    def test_millennium_falcon_autonomy_is_positive(self):
        self.assertGreater(self.millennium_falcon.get_autonomy(), 0)

    def test_millennium_falcon_routes_entry_is_of_right_format(self):
        for route in self.millennium_falcon.get_routes():
            self.assertIsInstance(route[0], str)
            self.assertIsInstance(route[1], str)
            self.assertIsInstance(route[2], int)


if __name__ == '__main__':
    unittest.main()
