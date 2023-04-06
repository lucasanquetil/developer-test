from src.model.empire import Empire
from src.model.millennium_falcon import MillenniumFalcon
from src.model.journey import Journey
from copy import deepcopy


def compute_all_valid_journey(millennium_falcon: MillenniumFalcon, empire: Empire) -> list:
    """
    This function returns all the valid journeys the millennium_falcon can make to counter the empire in time, without
    getting caught by the empire.
    :param millennium_falcon: A MillenniumFalcon object, see model.millenium_falcon for more details.
    :param empire: An Empire object, see model.empire for more details.
    :return valid_journey: A list of Journey objects, see model.journey for more details.
    """
    assert isinstance(millennium_falcon, MillenniumFalcon), "test_solver.py: Invalid argument, millennium_falcon " \
                                                            + "should be a MillenniumFalcon object"
    assert isinstance(empire, Empire), "test_solver.py: Invalid argument, empire should be an Empire object"

    valid_journey = []
    journey_list = []
    for (departure, arrival, days) in millennium_falcon.get_routes():
        # One way trip from departure to arrival
        # All the valid journey start from the MillenniumFalcon departure
        if departure == millennium_falcon.get_departure():
            # Only journeys that don't last more than the countdown are valid
            if days < empire.get_countdown():
                one_journey = Journey(departure, millennium_falcon.get_autonomy())
                # If the MilleniumFalcon can make it to the arrival planet
                if days <= millennium_falcon.get_autonomy():
                    one_journey.do_trip(departure, arrival, days)
                    journey_list.append(one_journey)

        # The same trip in the other direction: from arrival to departure
        # All the valid journey start from the MillenniumFalcon departure
        if arrival == millennium_falcon.get_departure():
            # Only journeys that don't last more than the countdown are valid
            if days < empire.get_countdown():
                one_journey = Journey(arrival, millennium_falcon.get_autonomy())
                # If the MilleniumFalcon can make it to the arrival planet
                if days <= millennium_falcon.get_autonomy():
                    one_journey.do_trip(arrival, departure, days)
                    journey_list.append(one_journey)

    # Or the crew can just wait 1 day on the first planet
    new_journey = Journey(millennium_falcon.get_departure(), millennium_falcon.get_autonomy())
    new_journey.wait_on_current_planet_and_refuel()
    journey_list.append(new_journey)

    # While we still have possible journey to explore that might work, we explore it
    while len(journey_list) > 0:
        one_journey = journey_list[0]

        # If the current journey arrives at the ending planet, then we're done with it
        if one_journey.get_current_planet() == millennium_falcon.get_arrival():
            valid_journey.append(one_journey)
            journey_list.remove(one_journey)
            continue

        # Exploring all the possible next planets the current Journey can lead to
        # We don't prevent from going to a previously explored planet, which would cause possible endless cycle,
        # But because there is the Empire's countdown, it prevents from cycling infinitely.
        for (departure, arrival, days) in millennium_falcon.get_routes():
            # One way trip from departure to arrival
            if departure == one_journey.get_current_planet():
                new_journey = deepcopy(one_journey)
                # If the MilleniumFalcon can make it to the other planet, we explore this path
                if days <= millennium_falcon.get_autonomy():
                    new_journey.do_trip(departure, arrival, days)
                # Only journeys lasting at maximum Empire's countdown days are authorized
                if new_journey.get_days() <= empire.get_countdown():
                    journey_list.append(new_journey)

            # The same trip in the other direction: from arrival to departure
            if arrival == one_journey.get_current_planet():
                new_journey = deepcopy(one_journey)
                # If the MilleniumFalcon can make it to the other planet, we explore this path
                if days <= millennium_falcon.get_autonomy():
                    new_journey.do_trip(arrival, departure, days)
                # Only journeys lasting at maximum Empire's countdown days are authorized
                if new_journey.get_days() <= empire.get_countdown():
                    journey_list.append(new_journey)

        # Or the crew can just wait 1 day on the current planet
        new_journey = deepcopy(one_journey)
        new_journey.wait_on_current_planet_and_refuel()
        if new_journey.get_days() <= empire.get_countdown():
            journey_list.append(new_journey)

        # All the next possibilities of the current root journey have been added to explore,
        # then we remove this old one
        journey_list.remove(one_journey)

    # Now we have all the valid journeys computed, we compute the probability to make it to the end
    # Without getting caught by the Bounty Hunters
    for journey in valid_journey:
        journey.compute_odd(empire)
    return valid_journey


def give_me_the_odds(millennium_falcon: MillenniumFalcon, empire: Empire) -> int:
    """
    This function returns the millennium_falcon's best odds of to countering the empire in time without getting caught
    by the empire's bounty hunters.
    :param millennium_falcon: A MillenniumFalcon object, see model.millenium_falcon for more details.
    :param empire: An Empire object, see model.empire for more details.
    :return best_odd: The odd of saving the galaxy.
    """
    assert isinstance(millennium_falcon, MillenniumFalcon), "test_solver.py: Invalid argument, millennium_falcon " \
                                                            + "should be a MillenniumFalcon object"
    assert isinstance(empire, Empire), "test_solver.py: Invalid argument, empire should be an Empire object"

    valid_journey = compute_all_valid_journey(millennium_falcon, empire)

    best_odd = 0
    for journey in valid_journey:
        if journey.get_odd() >= best_odd:
            best_odd = journey.get_odd()
    return best_odd
