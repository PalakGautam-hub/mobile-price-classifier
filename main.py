from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

FEATURE_ORDER = [
    "battery_power",
    "ram",
    "px_height",
    "px_width",
    "mobile_wt",
    "int_memory",
    "pc",
    "fc",
    "clock_speed",
    "sc_h",
    "sc_w",
]

# Broad realistic bounds to reject clearly invalid input.
FEATURE_BOUNDS = {
    "battery_power": (100, 10000),
    "ram": (128, 20000),
    "px_height": (0, 5000),
    "px_width": (100, 8000),
    "mobile_wt": (50, 500),
    "int_memory": (1, 2000),
    "pc": (0, 200),
    "fc": (0, 200),
    "clock_speed": (0.1, 10.0),
    "sc_h": (1, 50),
    "sc_w": (0, 50),
}


def parse_and_validate_features(data):
    if not isinstance(data, dict):
        return None, "Request body must be valid JSON."

    features = []
    for field in FEATURE_ORDER:
        if field not in data:
            return None, f"Missing required field: {field}"

        raw_value = data[field]
        if raw_value is None or str(raw_value).strip() == "":
            return None, f"Field '{field}' cannot be empty."

        try:
            value = float(raw_value)
        except (TypeError, ValueError):
            return None, f"Field '{field}' must be a number."

        if not np.isfinite(value):
            return None, f"Field '{field}' must be a finite number."

        min_val, max_val = FEATURE_BOUNDS[field]
        if value < min_val or value > max_val:
            return None, f"Field '{field}' must be between {min_val} and {max_val}."

        features.append(value)

    return np.array(features, dtype=float).reshape(1, -1), None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json
    features, error = parse_and_validate_features(data)
    if error:
        return jsonify({"error": error}), 400

    features = scaler.transform(features)

    prediction = model.predict(features)[0]

    labels = {
        0:"Low Price",
        1:"Medium Price",
        2:"High Price",
        3:"Very High Price"
    }

    return jsonify({"prediction":labels[int(prediction)]})

if __name__ == "__main__":
    app.run(debug=True)