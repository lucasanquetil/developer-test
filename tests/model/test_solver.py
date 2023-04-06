import sys
import os
import unittest

sys.path.insert(0, os.getcwd())
from src.model import solver, empire, millennium_falcon, journey


class TestSolver(unittest.TestCase):
    # A simple problem going from France to USA through UK taking 8 days to complete
    # with the bounty hunter on the departure planet only so we expect 90% chance of making it and 3 possible solutions
    # Directly France-UK-USA OR France-UK-USA with 1 waiting day on France OR France-UK-USA with 1 waiting day on UK

    def setUp(self) -> None:
        self.empire = empire.Empire(countdown=9, bounty_hunters=[{'planet': 'France', 'day': 0}])
        self.millennium_falcon = millennium_falcon.MillenniumFalcon(autonomy=10, departure='France', arrival='USA',
                                                                    routes=[('France', 'UK', 1), ('UK', 'USA', 7)])
        self.valid_journey = solver.compute_all_valid_journey(self.millennium_falcon, self.empire)
        self.best_odd = solver.give_me_the_odds(self.millennium_falcon, self.empire)

    def test_best_odds_is_float(self):
        self.assertIsInstance(self.best_odd, float)

    def test_best_odds_is_positive(self):
        self.assertGreaterEqual(self.best_odd, 0)

    def test_solver_solution_is_list(self):
        self.assertIsInstance(self.valid_journey, list)

    def test_number_of_solver_solution_found_is_good(self):
        self.assertEqual(len(self.valid_journey), 3)

    def test_all_solver_solution_are_journey(self):
        for solution in self.valid_journey:
            self.assertIsInstance(solution, journey.Journey)

    def test_all_solver_solution_start_from_departure(self):
        for solution in self.valid_journey:
            self.assertEqual(solution.get_travel_plan()[0][0], 'France')

    def test_all_solver_solution_end_in_destination(self):
        for solution in self.valid_journey:
            self.assertEqual(solution.get_travel_plan()[-1][0], 'USA')

    def test_all_solver_solution_odds_are_floats(self):
        for solution in self.valid_journey:
            self.assertIsInstance(solution.get_odd(), float)

    def test_all_solver_solution_odds_are_positive(self):
        for solution in self.valid_journey:
            self.assertGreaterEqual(solution.get_odd(), 0)

    def test_all_solver_solution_takes_lower_time_than_empire_countdown(self):
        for solution in self.valid_journey:
            self.assertLessEqual(solution.get_days(), self.empire.get_countdown())


if __name__ == '__main__':
    unittest.main()
