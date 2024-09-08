import numpy as np
import joblib

# Load the saved model and scaler
model = joblib.load('breast_cancer_model.joblib')
scaler = joblib.load('scaler.joblib')

# New data point for prediction (make sure the order of features matches)
new_data = np.array([[17.99, 10.38, 122.8, 1001, 0.1184, 0.2776]])

# Scale the new data using the previously saved scaler
new_data_scaled = scaler.transform(new_data)

# Make a prediction
prediction = model.predict(new_data_scaled)

# Output the result
if prediction[0] == 1:
    print("Prediction: Malignant")
else:
    print("Prediction: Benign")
