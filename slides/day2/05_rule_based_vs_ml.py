"""
Rule-based AI vs machine learning.
Rule-based system: humans write the rules.
ML system: the computer learns the pattern from examples.
"""

# Rule-based example

def rule_based_fan_control(temp_c, humidity_percent):
    if temp_c > 28 or humidity_percent > 85:
        return "Turn fan ON"
    return "Keep fan OFF"

print("Rule-based decision:", rule_based_fan_control(30, 70))

# Simple ML-like example without external libraries:
# We learn a rough relationship by finding a threshold from examples.
examples = [
    # temp, humidity, fan_needed
    (22, 70, 0),
    (24, 75, 0),
    (26, 80, 0),
    (28, 82, 1),
    (30, 78, 1),
    (31, 90, 1),
]

# Try many temperature thresholds and keep the one with best accuracy.
best_threshold = None
best_accuracy = -1
for threshold in range(20, 34):
    correct = 0
    for temp, humidity, label in examples:
        prediction = 1 if temp >= threshold else 0
        if prediction == label:
            correct += 1
    accuracy = correct / len(examples)
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_threshold = threshold

print(f"Learned temperature threshold: {best_threshold}°C")
print(f"Training accuracy: {best_accuracy:.2f}")

new_temp = 29
prediction = "Turn fan ON" if new_temp >= best_threshold else "Keep fan OFF"
print(f"For {new_temp}°C: {prediction}")
