from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Validation rules matching the training dataset ranges
VALIDATION_RULES = {
    "battery_power": {"min": 500,  "max": 2000, "label": "Battery Power"},
    "ram":           {"min": 256,  "max": 4000, "label": "RAM"},
    "int_memory":    {"min": 2,    "max": 64,   "label": "Internal Memory"},
    "clock_speed":   {"min": 0.5,  "max": 3.0,  "label": "Clock Speed"},
    "mobile_wt":     {"min": 80,   "max": 200,  "label": "Weight"},
    "pc":            {"min": 0,    "max": 20,   "label": "Primary Camera"},
    "fc":            {"min": 0,    "max": 19,   "label": "Front Camera"},
    "px_height":     {"min": 0,    "max": 1960, "label": "Pixel Height"},
    "px_width":      {"min": 500,  "max": 1998, "label": "Pixel Width"},
    "sc_h":          {"min": 5,    "max": 19,   "label": "Screen Height"},
    "sc_w":          {"min": 0,    "max": 18,   "label": "Screen Width"},
}

FEATURE_ORDER = [
    "battery_power", "ram", "px_height", "px_width", "mobile_wt",
    "int_memory", "pc", "fc", "clock_speed", "sc_h", "sc_w"
]

LABELS = {
    0: "Low Price",
    1: "Medium Price",
    2: "High Price",
    3: "Very High Price"
}

CSS_CLASSES = {
    0: "price-low",
    1: "price-medium",
    2: "price-high",
    3: "price-very-high"
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    if not data:
        return jsonify({"error": "No input data provided."}), 400

    # Validate all fields
    errors = []
    values = {}
    for field in FEATURE_ORDER:
        rule = VALIDATION_RULES[field]
        raw = data.get(field)

        if raw is None or raw == "":
            errors.append({"field": field, "message": f"{rule['label']} is required."})
            continue

        try:
            val = float(raw)
        except (ValueError, TypeError):
            errors.append({"field": field, "message": f"{rule['label']} must be a valid number."})
            continue

        if val < rule["min"] or val > rule["max"]:
            errors.append({
                "field": field,
                "message": f"{rule['label']} must be between {rule['min']} and {rule['max']}."
            })
            continue

        values[field] = val

    if errors:
        return jsonify({"errors": errors}), 422

    features = np.array([values[f] for f in FEATURE_ORDER]).reshape(1, -1)
    features = scaler.transform(features)

    prediction = int(model.predict(features)[0])

    return jsonify({
        "prediction": LABELS[prediction],
        "css_class": CSS_CLASSES[prediction]
    })


if __name__ == "__main__":
    app.run(debug=True)