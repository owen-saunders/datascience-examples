import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Create/show random data as 'blob' clusters
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_start=0)
plt.scatter(X[:,0], X[:,1])
plt.show()

 # Max No. Clusters to try
k_max = 30
# Error margin
wcss = [] 

# Test runs for K values
for i in range(1, k_max):
    kmeans = KMeans(n_clusters=i, max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Plotting error margins for each attempted cluster number (K-value)
plt.plot(range(1, k_max), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

