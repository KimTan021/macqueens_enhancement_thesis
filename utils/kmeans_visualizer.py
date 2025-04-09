import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

class KMeansVisualizer:
    def __init__(self, n_clusters, data, algorithm, init, max_iter, ax, anim):
        self.kmeans = KMeans(n_clusters=n_clusters, algorithm=algorithm, init=init, max_iter=max_iter, random_state=42)
        self.data = data
        self.n_clusters = n_clusters
        self.labels = np.zeros(len(data))
        self.centroids = np.random.rand(n_clusters, 2)
        self.max_iter = max_iter
        self.ax = ax
        self.anim = anim
        self.current_index = 0  # Track the current data point being added
        self.partial_data = np.empty((0, data.shape[1]))  # Store the data points incrementally

    def fit(self, frame):
        self.ax.clear()

        # Add the next data point to the partial dataset
        if self.current_index < len(self.data):
            self.partial_data = np.vstack([self.partial_data, self.data[self.current_index]])
            self.current_index += 1

        # Perform clustering on the partial dataset
        if len(self.partial_data) >= self.n_clusters:
            self.kmeans.fit(self.partial_data)
            self.labels = self.kmeans.labels_
            self.centroids = self.kmeans.cluster_centers_

        # Plot the partial dataset
        self.ax.scatter(self.partial_data[:, 0], self.partial_data[:, 1], c=self.labels[:len(self.partial_data)], marker='.')
        self.ax.scatter(self.centroids[:, 0], self.centroids[:, 1], c='red', marker='x', label='Centroids')

        # Add titles and labels
        self.ax.set_title(f"K-Means Clustering (Frame {frame})")
        self.ax.set_xlabel("Feature 1")
        self.ax.set_ylabel("Feature 2")
        self.ax.legend()

        # Stop the animation when all data points are added
        if self.current_index >= len(self.data):
            self.anim.event_source.stop()