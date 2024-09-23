import numpy as np
from sklearn.linear_model import LinearRegression

# Example dataset
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 2, 3, 4, 5])

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the model
import joblib
joblib

