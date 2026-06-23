"""
Group greenhouse locations using sensor readings.
This is unsupervised learning: the model finds groups without labels.
Install if needed: pip install scikit-learn numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Each point is one location in a greenhouse: [light_PPFD, temperature_C]
X = np.array([
    [120, 21], [140, 21.5], [160, 22], [150, 22.2],
    [300, 25], [330, 25.5], [350, 26], [370, 26.2],
    [220, 23], [240, 23.5], [260, 24], [250, 24.3]
])

kmeans = KMeans(n_clusters=3, random_state=0, n_init="auto")
labels = kmeans.fit_predict(X)

print("Cluster labels:", labels)
print("Cluster centers [light_PPFD, temperature_C]:")
print(kmeans.cluster_centers_)

plt.figure(figsize=(7, 4))
plt.scatter(X[:, 0], X[:, 1], c=labels, s=120)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker="X", s=250)
plt.xlabel("Light level (PPFD)")
plt.ylabel("Temperature (°C)")
plt.title("Finding Greenhouse Zones with K-Means")
plt.tight_layout()
plt.show()
