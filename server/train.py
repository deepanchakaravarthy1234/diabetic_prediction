from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle

# Load dataset
df = pd.read_csv("diabetes.csv")
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train Logistic Regression
model = LogisticRegression()
model.fit(X_scaled, y)

# Save scaler and model
pickle.dump(scaler, open("scaler.pkl", "wb"))
pickle.dump(model, open("lr.pkl", "wb"))
