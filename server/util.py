
import json
import pickle
import numpy as np
from pathlib import Path

__locations = None
__data_columns = None
__model = None


def get_location_names():
    return __locations


def load_saved_artifacts():

    print("Loading Saved Artifacts...Start")

    global __data_columns
    global __locations
    global __model

    # Get the directory where util.py is located
    base_dir = Path(__file__).resolve().parent

    # Find artifacts folder
    artifacts_dir = base_dir / "artifacts"

    # Load columns
    with open(artifacts_dir / "columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]

    # Load trained model
    with open(artifacts_dir / "banglore_home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)

    print("Loading Saved Artifacts...Done")


def get_estimated_price(location, sqft, bhk, bath):

    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    input_data = np.zeros(len(__data_columns))

    input_data[0] = sqft
    input_data[1] = bath
    input_data[2] = bhk

    if loc_index >= 0:
        input_data[loc_index] = 1

    return round(__model.predict([input_data])[0], 2)


if __name__ == "__main__":

    load_saved_artifacts()

    print(get_location_names())

    print(get_estimated_price("1st Phase JP Nagar", 1000, 3, 3))
    print(get_estimated_price("1st Phase JP Nagar", 1000, 2, 2))
    print(get_estimated_price("Kalhalli", 1000, 2, 2))
    print(get_estimated_price("Ejipura", 1000, 2, 2))
