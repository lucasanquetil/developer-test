MAX_COUNTDOWN = 100000


class Empire:
    def __init__(self, countdown, bounty_hunters):
        assert isinstance(countdown, int), "test_empire.py: Invalid argument, countdown should be an integer"
        assert isinstance(bounty_hunters, list), "test_empire.py: Invalid argument, bounty_hunters should be a list"
        assert 0 <= countdown <= MAX_COUNTDOWN, "test_empire.py: Invalid argument, countdown should " \
                                                "be positive integer up to " + str(MAX_COUNTDOWN)
        for item in bounty_hunters:
            assert isinstance(item, dict), "test_empire.py: Invalid argument, item in bounty_hunters should be a dict"
            assert 'day' in item.keys(), "test_empire.py: Invalid argument, item in bounty_hunters doesn't " \
                                         "contain a day key"
            assert 'planet' in item.keys(), "test_empire.py: Invalid argument, item in bounty_hunters doesn't " \
                                            "contain a planet value"
        self.__countdown = countdown
        self.__bounty_hunters = bounty_hunters

    # Getters
    def get_countdown(self):
        return self.__countdown

    def get_bounty_hunters(self):
        return self.__bounty_hunters
