"""
Classic ML example: Should we play tennis outside?
This uses a decision tree to learn from examples.
Install if needed: pip install scikit-learn pandas
"""

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier, export_text

# Each row is one past day. The label says whether people played tennis.
data = pd.DataFrame([
    ["Sunny",    "Hot",  "High",   "Weak",   "No"],
    ["Sunny",    "Hot",  "High",   "Strong", "No"],
    ["Overcast", "Hot",  "High",   "Weak",   "Yes"],
    ["Rain",     "Mild", "High",   "Weak",   "Yes"],
    ["Rain",     "Cool", "Normal", "Weak",   "Yes"],
    ["Rain",     "Cool", "Normal", "Strong", "No"],
    ["Overcast", "Cool", "Normal", "Strong", "Yes"],
    ["Sunny",    "Mild", "High",   "Weak",   "No"],
    ["Sunny",    "Cool", "Normal", "Weak",   "Yes"],
    ["Rain",     "Mild", "Normal", "Weak",   "Yes"],
    ["Sunny",    "Mild", "Normal", "Strong", "Yes"],
    ["Overcast", "Mild", "High",   "Strong", "Yes"],
    ["Overcast", "Hot",  "Normal", "Weak",   "Yes"],
    ["Rain",     "Mild", "High",   "Strong", "No"],
], columns=["Outlook", "Temperature", "Humidity", "Wind", "PlayTennis"])

X = data[["Outlook", "Temperature", "Humidity", "Wind"]]
y = data["PlayTennis"]

model = Pipeline([
    ("encode", ColumnTransformer([
        ("categorical", OneHotEncoder(), ["Outlook", "Temperature", "Humidity", "Wind"])
    ])),
    ("tree", DecisionTreeClassifier(max_depth=3, random_state=0))
])

model.fit(X, y)

new_day = pd.DataFrame([["Sunny", "Cool", "High", "Strong"]],
                       columns=["Outlook", "Temperature", "Humidity", "Wind"])

print("New day:")
print(new_day)
print("Prediction:", model.predict(new_day)[0])

# Show a simple text version of the tree
feature_names = model.named_steps["encode"].get_feature_names_out()
tree = model.named_steps["tree"]
print("\nDecision tree rules:")
print(export_text(tree, feature_names=list(feature_names)))
