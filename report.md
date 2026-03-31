# Mobile Price Range Classifier Using Machine Learning and Flask

---

## Title Page

**Project Title:** Mobile Price Range Classifier Using Machine Learning and Flask

**Course Name:** Application Development Laboratory (CS33002)

**Submitted By:**

| Name | Roll No |
|------|---------|
| Divyanshi Chaurasia | 23053124 |
| Palak Gautam | 23052982 |
| Anshu Shahdeo | 23052547 |
| Shabbir Uddin | 23052976 |
| Rahul Mishra | 23052344 |
| Animesh Krishnan | 23053529 |

**Submitted To:** Mr. Anirban Saha (Course Instructor)

**Department:** Computer Science and Engineering

**Institution:** KIIT University

**Semester:** 6th Semester

**Academic Session:** Spring 2026

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Problem Statement](#2-problem-statement)
3. [Objectives](#3-objectives)
4. [Literature Review](#4-literature-review)
5. [System Architecture](#5-system-architecture)
6. [Dataset Description](#6-dataset-description)
7. [Methodology](#7-methodology)
8. [Implementation Details](#8-implementation-details)
9. [Input Validation](#9-input-validation)
10. [Results and Analysis](#10-results-and-analysis)
11. [Screenshots](#11-screenshots)
12. [Conclusion](#12-conclusion)
13. [Future Scope](#13-future-scope)
14. [References](#14-references)

---

## 1. Introduction

The mobile phone market offers devices across a wide spectrum of price ranges, making it challenging for consumers and manufacturers to accurately categorize phones based on their hardware specifications. This project develops a web-based Machine Learning system that classifies a mobile phone into one of four price categories — Low, Medium, High, or Very High — based on its technical features.

The system uses a Random Forest Classifier trained on the Mobile Price Classification dataset from Kaggle, and is deployed as an interactive web application using Flask. Users can input device specifications through a modern, validated web form and receive instant price range predictions.

---

## 2. Problem Statement

Given a set of mobile phone hardware specifications (such as RAM, battery power, camera quality, screen resolution, etc.), classify the device into one of four price ranges:

- **0 - Low Price:** Budget segment devices
- **1 - Medium Price:** Mid-range devices
- **2 - High Price:** Premium devices
- **3 - Very High Price:** Flagship-tier devices

This is a **multiclass classification** problem where the goal is to predict the discrete price category rather than the exact price.

---

## 3. Objectives

1. Build and train a multiclass classification model using the Mobile Price Classification dataset.
2. Evaluate and select the best-performing ML algorithm among Decision Tree, Random Forest, and SVM.
3. Develop a Flask-based web application with a user-friendly interface for real-time predictions.
4. Implement comprehensive input validation (client-side and server-side) with user guidance on valid ranges.
5. Deploy the system as a locally hosted web application.

---

## 4. Literature Review

**Machine Learning for Price Prediction:**
Classification algorithms have been widely used in pricing and categorization tasks. Studies show that ensemble methods like Random Forest outperform single classifiers for tabular data with mixed feature types.

**Random Forest Classifier:**
Random Forest is an ensemble learning method that constructs multiple decision trees during training and outputs the mode of the classes for classification. It is robust against overfitting, handles non-linear relationships well, and provides feature importance rankings.

**Support Vector Machine (SVM):**
SVM finds the optimal hyperplane that maximizes the margin between classes. While effective for high-dimensional data, it is computationally more expensive than tree-based methods for larger datasets.

**Decision Tree:**
Decision Trees are interpretable and easy to visualize but are prone to overfitting without pruning. They serve as the base learner within Random Forest ensembles.

**Algorithm Selection:**
After comparative evaluation, Random Forest was selected as the final model due to its superior accuracy and generalization capability on this dataset.

---

## 5. System Architecture

```
┌─────────────────────────────────────────────────────┐
│                    CLIENT (Browser)                  │
│  ┌───────────────────────────────────────────────┐   │
│  │  HTML Form (11 input fields with validation)  │   │
│  │  JavaScript (client-side validation + fetch)   │   │
│  │  CSS (glassmorphism UI + responsive design)    │   │
│  └───────────────────┬───────────────────────────┘   │
└──────────────────────┼───────────────────────────────┘
                       │ POST /predict (JSON)
                       ▼
┌─────────────────────────────────────────────────────┐
│                  FLASK SERVER (Python)                │
│  ┌───────────────────────────────────────────────┐   │
│  │  Route: /           → Serve index.html         │   │
│  │  Route: /predict    → Validate + Predict       │   │
│  └───────────────────┬───────────────────────────┘   │
│                      │                               │
│  ┌───────────────────▼───────────────────────────┐   │
│  │  StandardScaler (scaler.pkl)                   │   │
│  │  Random Forest Model (model.pkl)               │   │
│  └───────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

**Workflow:**
1. User enters mobile specifications in the web form.
2. Client-side JavaScript validates all inputs against defined ranges.
3. Valid data is sent as a JSON POST request to the `/predict` endpoint.
4. Flask server performs server-side validation as a safety net.
5. Input features are scaled using the pre-fitted StandardScaler.
6. The Random Forest model predicts the price category.
7. The result (with color-coded label and description) is returned to the browser.

---

## 6. Dataset Description

**Source:** Mobile Price Classification Dataset from Kaggle

**Size:** 2,000 samples with 21 features

**Features Used (11 selected):**

| Feature | Description | Min | Max | Mean |
|---------|-------------|-----|-----|------|
| battery_power | Battery capacity (mAh) | 501 | 1998 | 1238.5 |
| ram | RAM (MB) | 256 | 3998 | 2124.2 |
| int_memory | Internal storage (GB) | 2 | 64 | 32.0 |
| clock_speed | Processor speed (GHz) | 0.5 | 3.0 | 1.5 |
| mobile_wt | Weight (grams) | 80 | 200 | 140.2 |
| pc | Primary camera (MP) | 0 | 20 | 9.9 |
| fc | Front camera (MP) | 0 | 19 | 4.3 |
| px_height | Pixel resolution height | 0 | 1960 | 645.1 |
| px_width | Pixel resolution width | 500 | 1998 | 1251.5 |
| sc_h | Screen height (cm) | 5 | 19 | 12.3 |
| sc_w | Screen width (cm) | 0 | 18 | 5.8 |

**Target Variable:** `price_range` (0 = Low, 1 = Medium, 2 = High, 3 = Very High)

**Class Distribution:** Balanced — approximately 500 samples per class.

---

## 7. Methodology

### 7.1 Data Preprocessing
- Loaded the dataset using pandas.
- Selected 11 most relevant hardware features based on domain knowledge.
- No missing values were found in the dataset.
- Applied StandardScaler to normalize feature values (zero mean, unit variance).

### 7.2 Train-Test Split
- 80% training data (1,600 samples)
- 20% testing data (400 samples)
- Random state fixed at 42 for reproducibility.

### 7.3 Model Training
- **Algorithm:** Random Forest Classifier
- **Parameters:** Default scikit-learn parameters with random_state=42
- The model was trained on the scaled training set.

### 7.4 Model Persistence
- Trained model saved as `model.pkl` using joblib.
- Fitted scaler saved as `scaler.pkl` using joblib.
- Both files are loaded at server startup for real-time inference.

---

## 8. Implementation Details

### 8.1 Backend (main.py)
- **Framework:** Flask
- **Endpoints:**
  - `GET /` — Serves the web interface
  - `POST /predict` — Accepts JSON input, validates, scales, predicts, and returns the result
- **Validation:** Server-side validation checks all 11 fields for presence, type, and range compliance
- **Response Format:** JSON with prediction label and CSS class for color coding

### 8.2 Frontend (index.html + script.js + style.css)
- **Form:** 11 input fields with HTML5 attributes (min, max, step, required)
- **Validation:** JavaScript performs real-time validation before submission
- **Hints:** Each field displays the acceptable range below the input
- **Error Display:** Inline red error messages appear under invalid fields
- **Result Display:** Color-coded pill badge with descriptive text
  - Green = Low Price
  - Yellow = Medium Price
  - Orange = High Price
  - Red = Very High Price

### 8.3 UI Design
- **Design System:** Glassmorphism with dark theme
- **Animations:** Fade-in on load, animated gradient blobs in background
- **Typography:** Outfit font family (Google Fonts)
- **Responsive:** Adapts to mobile screens via CSS Grid and media queries

### 8.4 Model Training Script (train_model.py)
```python
# Key steps in train_model.py
df = pd.read_csv("dataset/train.csv")
X = df[selected_features]
y = df["price_range"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
```

---

## 9. Input Validation

The system implements a **two-layer validation** approach:

### Layer 1: Client-Side (JavaScript)
- Checks for empty fields, non-numeric values, and out-of-range inputs
- Displays inline error messages with red highlighting
- Auto-focuses the first invalid field
- Errors clear automatically as the user corrects input

### Layer 2: Server-Side (Flask)
- Re-validates all inputs as a security measure
- Returns HTTP 422 with field-specific error messages if validation fails
- Prevents malformed or tampered data from reaching the model

### Validation Rules

| Field | Type | Min | Max | Step |
|-------|------|-----|-----|------|
| Battery Power | Integer | 500 | 2000 | 1 |
| RAM | Integer | 256 | 4000 | 1 |
| Internal Memory | Integer | 2 | 64 | 1 |
| Clock Speed | Float | 0.5 | 3.0 | 0.1 |
| Weight | Integer | 80 | 200 | 1 |
| Primary Camera | Integer | 0 | 20 | 1 |
| Front Camera | Integer | 0 | 19 | 1 |
| Pixel Height | Integer | 0 | 1960 | 1 |
| Pixel Width | Integer | 500 | 1998 | 1 |
| Screen Height | Float | 5 | 19 | 0.1 |
| Screen Width | Float | 0 | 18 | 0.1 |

---

## 10. Results and Analysis

### Model Performance
- **Algorithm Used:** Random Forest Classifier
- **Training Samples:** 1,600
- **Testing Samples:** 400
- **Feature Scaling:** StandardScaler applied to all 11 features

The Random Forest Classifier was chosen after considering Decision Tree and SVM alternatives. Random Forest provides:
- Higher accuracy due to ensemble averaging
- Robustness against overfitting
- Good handling of feature interactions
- Fast inference time suitable for real-time web predictions

### Price Range Distribution
The dataset is balanced across all four classes, ensuring the model does not exhibit class bias.

---

## 11. Screenshots

*Screenshots to be added showing:*
1. Main interface with empty form and range hints
2. Validation errors on invalid input
3. Successful prediction result (color-coded)
4. Mobile responsive view

---

## 12. Conclusion

This project successfully demonstrates the application of Machine Learning for mobile phone price classification. Key achievements include:

1. **Accurate Classification:** The Random Forest model effectively classifies phones into four price categories based on 11 hardware features.
2. **User-Friendly Interface:** The glassmorphism-styled web interface provides an intuitive experience with clear input guidance and validated forms.
3. **Robust Validation:** Two-layer validation (client + server) ensures data integrity and provides helpful feedback to users.
4. **Real-Time Predictions:** The Flask API delivers instant predictions with color-coded, descriptive results.
5. **Practical Application:** The system can assist consumers in understanding price positioning and help manufacturers in competitive pricing analysis.

---

## 13. Future Scope

1. **Expanded Features:** Include additional features like 5G support, number of cores, and touch screen capability for improved accuracy.
2. **Model Comparison Dashboard:** Add a page comparing Decision Tree, Random Forest, and SVM performance metrics.
3. **Database Integration:** Store prediction history for analytics and trend analysis.
4. **Cloud Deployment:** Deploy on platforms like Heroku, AWS, or Render for public access.
5. **API Documentation:** Add Swagger/OpenAPI documentation for the prediction endpoint.
6. **Batch Prediction:** Allow CSV upload for bulk price classification.

---

## 14. References

1. Kaggle - Mobile Price Classification Dataset: https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification
2. scikit-learn Documentation - Random Forest Classifier: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
3. Flask Official Documentation: https://flask.palletsprojects.com/
4. Breiman, L. (2001). "Random Forests." Machine Learning, 45(1), 5-32.
5. Pedregosa, F., et al. (2011). "Scikit-learn: Machine Learning in Python." Journal of Machine Learning Research, 12, 2825-2830.

---
