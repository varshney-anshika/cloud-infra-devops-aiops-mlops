import numpy as np
from sklearn.ensemble import IsolationForest

# Example data: CPU usage metrics
data = np.array([[10], [15], [20], [12], [13], [70], [15], [10], [14]])

# Train isolation forest to detect anomalies
model = IsolationForest(contamination=0.1)
model.fit(data)

# Detect anomalies
anomalies = model.predict(data)
print("Anomalies detected at:", np.where(anomalies == -1)[0])

