import json
import sys
from flask import Flask, request, jsonify, render_template, Response

from src.model.solver import give_me_the_odds
from src.utils.data import build_empire, build_millenium_falcon

app = Flask(__name__, template_folder='../view', static_folder='../view/images')


@app.route('/', methods=['GET'])
def get_index():
    return render_template("index.html")


@app.route('/odds', methods=['POST'])
def get_odds():
    """
    This function returns the millennium_falcon's best odds of to countering the empire in time without getting caught
    by the empire's bounty hunters and displays it in the HTML file
    :return: response: the Javascript response to be displayed in the HTML file
    """
    assert isinstance(sys.argv[1], str), "test_odds.py: Invalid argument, the command-line argument should be a string"

    millennium_falcon_path = sys.argv[1]
    millennium_falcon = build_millenium_falcon(millennium_falcon_path)

    try:
        file_bytes = request.files['empire'].read()
        file = json.loads(file_bytes)
        empire = build_empire(file)
    except Exception as e:
        print(e)
        return Response(
            "Error test_odds.py: Impossible to build an Empire object with the front-end usage\n",
            status=400,
        )

    best_odd = give_me_the_odds(millennium_falcon, empire)

    response = jsonify({'result': str(best_odd)})
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
