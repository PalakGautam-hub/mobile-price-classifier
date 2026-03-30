from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    features = [
        float(data["battery_power"]),
        float(data["ram"]),
        float(data["px_height"]),
        float(data["px_width"]),
        float(data["mobile_wt"]),
        float(data["int_memory"]),
        float(data["pc"]),
        float(data["fc"]),
        float(data["clock_speed"]),
        float(data["sc_h"]),
        float(data["sc_w"])
    ]

    features = np.array(features).reshape(1,-1)
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