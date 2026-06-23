"""
Detect unusual sensor readings using simple statistics.
This is not fancy AI, but it is a good first step toward intelligent monitoring.
Install if needed: pip install numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt

# Simulated pH readings around 6.2, with a few suspicious spikes
np.random.seed(2)
ph = 6.2 + 0.08 * np.random.randn(60)
ph[20] = 7.4
ph[42] = 5.1

mean = np.mean(ph)
std = np.std(ph)
z_score = (ph - mean) / std
anomaly = np.abs(z_score) > 3

print("Anomaly positions:", np.where(anomaly)[0].tolist())
print("Anomaly pH values:", ph[anomaly])

plt.figure(figsize=(8, 4))
plt.plot(ph, marker="o", label="pH reading")
plt.scatter(np.where(anomaly)[0], ph[anomaly], s=120, label="flagged anomaly")
plt.axhline(mean + 3*std, linestyle="--", label="upper limit")
plt.axhline(mean - 3*std, linestyle="--", label="lower limit")
plt.xlabel("Time step")
plt.ylabel("pH")
plt.title("Simple Sensor Anomaly Detection")
plt.legend()
plt.tight_layout()
plt.show()
