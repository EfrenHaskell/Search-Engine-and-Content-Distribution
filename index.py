#!usr/bin/env Python
"""
Test webserver for search engine
"""

__author__ = "Efren Haskell"
__email__ = "efrenhask@gmail.com"

from flask import Flask, render_template, request, jsonify
import content_manager as cm
from engine import Engine, Thomas

app = Flask(__name__)
THOMAS_THE_TANK_ENGINE: Thomas = Thomas(5)
ENGINE = THOMAS_THE_TANK_ENGINE
RESPONSE = ""


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/receive_input', methods=['POST'])
def receive_query():
    global RESPONSE
    RESPONSE = request.get_json().get('variable')
    return jsonify({"message": "Query successfully received"})


@app.route('/send_recs', methods=['GET'])
def send_recommendations():
    return jsonify(ENGINE.make_recommendation(RESPONSE))


if __name__ == "__main__":
    # cm.on_startup()
    ENGINE.manual_create_trie(['cat', 'apple', 'sand', 'catfish', 'catch', 'cap'])
    app.run(debug=True)
