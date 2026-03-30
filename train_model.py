import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset
data = pd.read_csv("dataset/train.csv")

# Target
y = data["price_range"]

# Features
X = data.drop("price_range", axis=1)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

# Train
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Model trained successfully")