"""
Predict plant water use from greenhouse conditions.
This is a tiny linear regression demo for class.
Install if needed: pip install scikit-learn pandas matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Toy data: higher temperature and light usually increase water use.
data = pd.DataFrame({
    "temperature_C": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
    "humidity_percent": [80, 78, 75, 73, 70, 68, 65, 62, 60, 58],
    "light_PPFD": [150, 170, 190, 220, 250, 280, 320, 360, 390, 430],
    "water_use_mL": [45, 48, 52, 57, 63, 70, 78, 86, 94, 105]
})

X = data[["temperature_C", "humidity_percent", "light_PPFD"]]
y = data["water_use_mL"]

model = LinearRegression()
model.fit(X, y)

new_greenhouse = pd.DataFrame({
    "temperature_C": [26],
    "humidity_percent": [65],
    "light_PPFD": [330]
})

prediction = model.predict(new_greenhouse)[0]
print(f"Predicted water use: {prediction:.1f} mL/day")

# Plot measured vs predicted values
predicted = model.predict(X)
plt.figure(figsize=(6, 4))
plt.scatter(y, predicted, s=80)
plt.plot([40, 110], [40, 110], linestyle="--")
plt.xlabel("Measured water use (mL/day)")
plt.ylabel("Predicted water use (mL/day)")
plt.title("Greenhouse Water Use Prediction")
plt.tight_layout()
plt.show()
