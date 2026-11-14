
from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)

CORS(app)

# Load saved model and artifacts
util.load_saved_artifacts()


@app.route('/')
def home():
    return "House Price Prediction API is Running!"


@app.route('/get_location_names', methods=['GET'])
def get_location_names():

    response = jsonify({
        'locations': util.get_location_names()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict', methods=['POST'])
def predict():

    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    estimated_price = util.get_estimated_price(
        location, total_sqft, bhk, bath
    )

    response = jsonify({
        'estimated_price': estimated_price
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":

    print("Starting Python Flask Server For Home Price Prediction...")
    print(app.url_map)
    app.run(debug=True, port=5000)
