class MillenniumFalcon:
    def __init__(self, autonomy, departure, arrival, routes):
        assert isinstance(autonomy, int), "test_millennium_falcon.py: Invalid argument, autonomy should be an integer"
        assert isinstance(departure, str), "test_millennium_falcon.py: Invalid argument, departure should be an string"
        assert isinstance(arrival, str), "test_millennium_falcon.py: Invalid argument, arrival should be an string"
        assert isinstance(routes, list), "test_millennium_falcon.py: Invalid argument, routes should be a list"
        assert 0 <= autonomy, "test_millennium_falcon.py: Invalid argument, autonomy should be a positive integer"
        for item in routes:
            assert isinstance(item, tuple), "test_millennium_falcon.py: Invalid argument, item in routes should " \
                                            "be a tuple"
            assert len(item) == 3, "test_millennium_falcon.py: Invalid argument, item in routes is not of the " \
                                   "form ('planetA', 'planetB', nbDaysToTravel) "
            assert isinstance(item[0], str), "test_millennium_falcon.py: Invalid argument, item in routes does " \
                                             "not contain a planet in the first position"
            assert isinstance(item[1], str), "test_millennium_falcon.py: Invalid argument, item in routes does " \
                                             "not contain a planet in the second position"
            assert isinstance(item[2], int), "test_millennium_falcon.py: Invalid argument, item in routes does " \
                                             "not contain an integer in the third position"

        self.__autonomy: int = autonomy
        self.__departure: str = departure
        self.__arrival: str = arrival
        self.__routes: list = routes

    # Getters
    def get_autonomy(self):
        return self.__autonomy

    def get_departure(self):
        return self.__departure

    def get_arrival(self):
        return self.__arrival

    def get_routes(self):
        return self.__routes
