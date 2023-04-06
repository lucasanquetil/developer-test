import sys
import os
import unittest

sys.path.insert(0, os.getcwd())
from src.utils import data
from src.model import millennium_falcon, empire


class TestData(unittest.TestCase):
    def setUp(self) -> None:
        self.millennium_falcon_path = os.getcwd() + '/examples/example1/millennium-falcon.json'
        self.empire_file_path = os.getcwd() + '/examples/example1/empire.json'
        self.routes_database_path = os.getcwd() + '/examples/example1/universe.db'
        self.true_empire_raw_data = {'countdown': 7, 'bounty_hunters': [{"planet": 'Hoth', 'day': 6},
                                                                        {"planet": "Hoth", "day": 7},
                                                                        {"planet": "Hoth", "day": 8}]}
        self.true_routes = [('Tatooine', 'Dagobah', 6), ('Dagobah', 'Endor', 4),
                            ('Dagobah', 'Hoth', 1), ('Hoth', 'Endor', 1), ('Tatooine', 'Hoth', 6)]

    def test_data_open_json_file_reads_well(self):
        raw_data = data.open_json_file(self.empire_file_path)
        self.assertEqual(self.true_empire_raw_data, raw_data)

    def test_data_get_routes_reads_well(self):
        data_routes = data.get_routes(self.routes_database_path)
        self.assertEqual(self.true_routes, data_routes)

    def test_data_build_millenium_falcon_is_millennium_falcon(self):
        print(self.millennium_falcon_path)
        millennium_falcon_built = data.build_millenium_falcon(self.millennium_falcon_path)
        self.assertIsInstance(millennium_falcon_built, millennium_falcon.MillenniumFalcon)

    def test_data_build_empire_is_empire(self):
        raw_data = data.open_json_file(self.empire_file_path)
        empire_built = data.build_empire(raw_data)
        self.assertIsInstance(empire_built, empire.Empire)


if __name__ == '__main__':
    unittest.main()
