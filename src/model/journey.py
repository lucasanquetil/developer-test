from src.model.empire import Empire


class Journey:
    def __init__(self, departure, autonomy_max):
        assert isinstance(departure, str), "test_journey.py: Invalid argument, departure should be a string"
        assert isinstance(autonomy_max, int), "test_journey.py: Invalid argument, autonomy_max should be an integer"
        assert 0 <= autonomy_max, "test_journey.py: Invalid argument, autonomy_max should be a positive integer"

        self.__autonomy_max: int = autonomy_max
        self.__time_before_refuel: int = autonomy_max
        self.__current_planet: str = departure
        self.__refuel_plan: list = []
        self.__waiting_plan: list = []
        self.__travel_plan: list = [(departure, 0)]
        self.__days: int = 0
        self.__odd: int = 0

    # Getters
    def get_current_planet(self):
        return self.__current_planet

    def get_days(self):
        return self.__days

    def get_time_before_refuel(self):
        return self.__time_before_refuel

    def get_refuel_plan(self):
        return self.__refuel_plan

    def get_travel_plan(self):
        return self.__travel_plan

    def get_waiting_plan(self):
        return self.__waiting_plan

    def get_odd(self):
        return self.__odd

    def add_planet_to_trip(self, planet, day):
        assert isinstance(planet, str), "test_journey.py: add_planet_to_trip: planet should be a string"
        assert isinstance(day, int), "test_journey.py: add_planet_to_trip: day should be an integer"
        assert 0 <= day, "test_journey.py: add_planet_to_trip: day should be a positive integer"
        self.__travel_plan.append((planet, day))

    def add_planet_to_refuel(self, planet, day):
        assert isinstance(planet, str), "test_journey.py: add_planet_to_refuel: planet should be a string"
        assert isinstance(day, int), "test_journey.py: add_planet_to_refuel: day should be an integer"
        assert 0 <= day, "test_journey.py: add_planet_to_refuel: day should be a positive integer"
        self.__refuel_plan.append((planet, day))

    def add_planet_to_wait_and_refuel(self, planet, day):
        assert isinstance(planet, str), "test_journey.py: add_planet_to_wait_and_refuel: planet should be a string"
        assert isinstance(day, int), "test_journey.py: add_planet_to_wait_and_refuel: day should be an integer"
        assert 0 <= day, "test_journey.py: add_planet_to_wait_and_refuel: day should be a positive integer"
        self.__waiting_plan.append((planet, day))

    def do_trip(self, departure, arrival, days):
        assert isinstance(departure, str), "test_journey.py: do_trip: departure should be a string"
        assert isinstance(arrival, str), "test_journey.py: do_trip: arrival should be a string"
        assert isinstance(days, int), "test_journey.py: do_trip: day should be an integer"
        assert 0 <= days, "test_journey.py: do_trip: days should be a positive integer"
        assert departure != arrival, "test_journey.py: do_trip: impossible to do a trip from one planet to itself"
        # If the MillenniumFalcon can make the trip without refueling then go for it
        if days <= self.__time_before_refuel:
            assert self.__current_planet == departure, "test_journey.py: do_trip: impossible to do trip from " \
                                                       + departure \
                                                       + "to " + arrival + " because the current planet is " \
                                                       + self.__current_planet

        # Now we must refuel before making it to the arrival planet
        else:
            # Adding one refuel stop to the journey
            self.__days = self.get_days() + 1
            self.add_planet_to_refuel(self.get_current_planet(), self.get_days())
            self.__time_before_refuel = self.__autonomy_max

        # And finally we can make it to the other planet
        self.__days = self.get_days() + days
        self.__current_planet = arrival
        self.add_planet_to_trip(arrival, self.get_days())
        self.__time_before_refuel = self.get_time_before_refuel() - days

    def wait_on_current_planet_and_refuel(self):
        # Adding 1 day to rest on the current planet
        self.__days = self.get_days() + 1
        current_day = self.get_days()
        self.add_planet_to_wait_and_refuel(self.__current_planet, current_day)

    def compute_odd(self, empire: Empire):
        assert isinstance(empire, Empire), "test_journey.py: compute_odd: empire should be an Empire object"

        odd = 0
        meeting_number = 0
        travel_plan = self.__travel_plan
        refuel_plan = self.__refuel_plan
        waiting_plan = self.__waiting_plan
        all_bounty_hunter = empire.get_bounty_hunters()

        for (journey_planet, journey_day) in travel_plan:
            for hunter in all_bounty_hunter:
                if hunter['planet'] == journey_planet and hunter['day'] == journey_day:
                    odd = odd + (9 ** meeting_number / 10 ** (meeting_number + 1))
                    meeting_number = meeting_number + 1

        for (journey_planet, journey_day) in refuel_plan:
            for hunter in empire.get_bounty_hunters():
                if hunter['planet'] == journey_planet and hunter['day'] == journey_day:
                    odd = odd + (9 ** meeting_number / 10 ** (meeting_number + 1))
                    meeting_number = meeting_number + 1

        for (journey_planet, journey_day) in waiting_plan:
            for hunter in empire.get_bounty_hunters():
                if hunter['planet'] == journey_planet and hunter['day'] == journey_day:
                    odd = odd + (9 ** meeting_number / 10 ** (meeting_number + 1))
                    meeting_number = meeting_number + 1

        self.__odd = 100 - (odd * 100)
        assert 0 <= self.__odd <= 100, "test_journey.py: compute_odd: the computed odd seems incorrect"
