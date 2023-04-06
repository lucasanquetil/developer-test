import os
import sys
from src.controller.odds import app

if __name__ == '__main__':
    assert isinstance(sys.argv[1], str), "main.py: Invalid command-line argument, should be a string"
    assert sys.argv[1].endswith('.json'), "main.py: Invalid command-line argument, should be a JSON file"
    assert os.path.isfile(sys.argv[1]), "main.py: Invalid command-line argument, should be a valid file"

    app.run(port=8000)
