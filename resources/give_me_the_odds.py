#!/usr/bin/env python
import sys
import os
from src.model.solver import give_me_the_odds
from src.utils.data import build_millenium_falcon, build_empire, open_json_file

if __name__ == '__main__':
    """
    A command-line executable solving the overall galaxy saving problem, and just print the best odds of the Millennium
    Falcon of countering the empire in time without getting caught by the bounty hunters.
    
    :param: The first inline argument should be the path to the Millennium Falcon's file
    :param: The second inline argument should be the path to the Empire's file
    :return: Nothing
    """
    if not (isinstance(sys.argv[1], str) and sys.argv[1].endswith('.json') and os.path.isfile(sys.argv[1])):
        sys.stderr.write('Error give_me_the_odds.py: Could not load first argument file\n')
        sys.exit()

    if not (isinstance(sys.argv[2], str) and sys.argv[2].endswith('.json') and os.path.isfile(sys.argv[2])):
        sys.stderr.write('Error give_me_the_odds.py: Could not load second argument file\n')
        sys.exit()

    millennium_falcon_path = sys.argv[1]
    empire_path = sys.argv[2]

    empire_data = open_json_file(empire_path)

    millennium_falcon = build_millenium_falcon(millennium_falcon_path)
    empire = build_empire(empire_data)
    best_odd = give_me_the_odds(millennium_falcon, empire)

    print(best_odd)
