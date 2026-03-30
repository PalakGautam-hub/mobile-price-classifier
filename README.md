# Mobile Price Classifier 📱💻

A Machine Learning web application built with Flask that predicts the price range of mobile phones based on their hardware specifications. 

## Overview
This project uses a Random Forest Classifier trained on a mobile phone dataset to predict whether a mobile phone falls into one of four price categories:
- **Low Price** (0)
- **Medium Price** (1)
- **High Price** (2)
- **Very High Price** (3)

The frontend allows users to input various specifications (like RAM, Battery Power, Camera Megapixels, etc.) to get a real-time price range prediction.

## Features
- Scaled Input Features via Scikit-Learn
- Real-time Price Prediction Interface
- Lightweight Flask API
- High Accuracy Random Forest Model

## Project Structure

```
mobile-price-classifier/
├── dataset/                # Contains training data (train.csv)
├── static/                 # CSS/JS and static assets
├── templates/              # HTML frontend templates (index.html)
├── main.py                 # Flask server and API endpoints
├── train_model.py          # Script to train and export ML models
├── requirements.txt        # Python package dependencies
├── model.pkl               # Saved Random Forest model
└── scaler.pkl              # Saved Scikit-Learn StandardScaler
```

## Getting Started

### Prerequisites
Make sure you have Python 3.8+ installed on your system.

### Installation
1. Open your terminal and navigate to the project directory:
   ```bash
   cd mobile-price-classifier
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Training the Model (Optional)
If you want to re-train the model, update the dataset in `dataset/train.csv` and run:
```bash
python train_model.py
```
This script processes the data, trains a Random Forest Classifier, and saves `model.pkl` and `scaler.pkl` to the root directory.

### Running the Application
Start the Flask development server:
```bash
python main.py
```
The application will be accessible at: `http://127.0.0.1:5000/`

## Usage
1. Open the web interface at `http://localhost:5000/`.
2. Enter the mobile hardware specifications via the provided form.
3. Submit the form to view the predicted price category dynamically.

## Technologies Used
- **Backend:** Python, Flask
- **Machine Learning:** Scikit-Learn, Pandas, NumPy, Joblib
- **Frontend:** HTML, CSS, JavaScript (via Jinja2 Templates)
