from flask import Flask, jsonify
from flask_cors import CORS
from itertools import product
from collections import Counter

app = Flask(__name__)
CORS(app)

def compute_probabilities():
    die_A = [1, 2, 3, 4, 5, 6]
    die_B = [1, 2, 3, 4, 5, 6]
    
    sums = [a + b for a, b in product(die_A, die_B)]
    sum_counts = Counter(sums)
    probabilities = {k: v / 36 for k, v in sum_counts.items()}
    
    return sum_counts, probabilities

@app.route('/compute_probabilities', methods=['GET'])
def get_probabilities():
    sum_counts, probabilities = compute_probabilities()
    return jsonify({"sum_counts": sum_counts, "probabilities": probabilities})

if __name__ == '__main__':
    app.run(debug=True)
