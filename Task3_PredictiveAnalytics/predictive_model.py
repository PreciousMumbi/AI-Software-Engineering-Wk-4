# predictive_model.py

# 📌 Import libraries
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import joblib

# 📌 Load dataset
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# 📌 Split data into features and target
X = df.drop('target', axis=1)
y = df['target']

# 📌 Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 📌 Train Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 📌 Predict on test set
y_pred = model.predict(X_test)

# 📌 Evaluate performance
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# 📌 Print metrics
print("Model Performance Metrics")
print("----------------------------")
print(f"Accuracy: {accuracy:.4f}")
print(f"F1-Score: {f1:.4f}")

# 📌 Save metrics to file
with open("Task3_PredictiveAnalytics/metrics.txt", "w") as f:
    f.write("Model Performance Metrics\n")
    f.write("----------------------------\n")
    f.write(f"Accuracy: {accuracy:.4f}\n")
    f.write(f"F1-Score: {f1:.4f}\n")

# 📌 (Optional) Save model for future use
joblib.dump(model, "Task3_PredictiveAnalytics/random_forest_model.pkl")
