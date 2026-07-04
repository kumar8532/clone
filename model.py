import numpy as np
from sklearn.linear_model import LogisticRegression
import joblib

# training data
X = np.array([[10], [15], [20], [25], [30], [35]])
y = ["Cold", "Cold", "Pleasant", "Pleasant", "Hot", "Hot"]

# train model
model = LogisticRegression()
model.fit(X, y)

# save model (yahi .pkl banayega)
joblib.dump(model, "weather_model.pkl")

print("Model created successfully ✅")