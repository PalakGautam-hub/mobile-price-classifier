# Mobile Price Range Classifier Using Machine Learning and Flask

An AI-powered web application that classifies mobile phones into price ranges (Low, Medium, High, Very High) based on hardware specifications using a Random Forest Classifier.

## Features

- Predicts mobile price range from 11 hardware features
- Real-time client-side and server-side input validation with range hints
- Color-coded results with descriptive explanations
- Modern glassmorphism UI with animated background
- Responsive design for all screen sizes

## Tech Stack

- **Backend:** Python, Flask
- **ML:** scikit-learn (Random Forest Classifier), pandas, NumPy
- **Frontend:** HTML5, CSS3, JavaScript
- **Dataset:** [Mobile Price Classification Dataset (Kaggle)](https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification)

## Input Parameters

| Feature | Description | Valid Range |
|---------|-------------|-------------|
| Battery Power | Battery capacity in mAh | 500 - 2000 |
| RAM | RAM in MB | 256 - 4000 |
| Internal Memory | Storage in GB | 2 - 64 |
| Clock Speed | Processor speed in GHz | 0.5 - 3.0 |
| Weight | Device weight in grams | 80 - 200 |
| Primary Camera | Rear camera in MP | 0 - 20 |
| Front Camera | Front camera in MP | 0 - 19 |
| Pixel Height | Screen resolution height | 0 - 1960 |
| Pixel Width | Screen resolution width | 500 - 1998 |
| Screen Height | Screen height in cm | 5 - 19 |
| Screen Width | Screen width in cm | 0 - 18 |

## Setup & Run

```bash
# Install dependencies
pip install -r requirements.txt

# Train the model (generates model.pkl and scaler.pkl)
python train_model.py

# Run the web application
python main.py
```

Open **http://127.0.0.1:5000** in your browser.

## Project Structure

```
mobile-price-classifier/
├── main.py              # Flask server with prediction API
├── train_model.py       # Model training script
├── model.pkl            # Trained Random Forest model
├── scaler.pkl           # Fitted StandardScaler
├── requirements.txt     # Python dependencies
├── report.md            # Project report
├── dataset/
│   └── train.csv        # Training dataset (2000 samples)
├── templates/
│   └── index.html       # Web interface
└── static/
    ├── style.css        # Glassmorphism styling
    └── script.js        # Frontend validation & API calls
```

## Team

Developed as part of **Application Development Laboratory (CS33002)**, Spring 2026, KIIT University.
