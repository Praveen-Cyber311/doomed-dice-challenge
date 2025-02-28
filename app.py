from flask import Flask, jsonify
from flask_cors import CORS
import random
from collections import Counter

app = Flask(__name__)
CORS(app)

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def get_distribution():
    outcomes = [(i, j) for i in range(1, 7) for j in range(1, 7)]
    sum_counts = Counter(sum(pair) for pair in outcomes)
    probabilities = {k: v / 36 for k, v in sum_counts.items()}
    return probabilities

def undoom_dice():
    new_die_a = [1, 2, 3, 4, 1, 2]
    new_die_b = [7 - x for x in new_die_a]
    return new_die_a, new_die_b

@app.route('/roll', methods=['GET'])
def roll():
    die_a, die_b = roll_dice()
    return jsonify({'Die A': die_a, 'Die B': die_b, 'Sum': die_a + die_b})

@app.route('/probabilities', methods=['GET'])
def probabilities():
    return jsonify(get_distribution())

@app.route('/undoom', methods=['GET'])
def undoom():
    new_die_a, new_die_b = undoom_dice()
    return jsonify({'New Die A': new_die_a, 'New Die B': new_die_b})

if __name__ == '__main__':
    app.run(debug=True)
