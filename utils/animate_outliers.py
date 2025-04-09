import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from sklearn.ensemble import IsolationForest

class IsolationForestVisualizer:
    def __init__(self, data, contamination, ax, anim):
        self.data = data
        self.contamination = contamination
        self.ax = ax
        self.anim = anim
        self.current_index = 0  # Track the current data point being added
        self.partial_data = np.empty((0, data.shape[1]))  # Store the data points incrementally
        self.outliers = np.array([])  # Store outlier predictions incrementally

    def fit(self, frame):
        self.ax.clear()

        # Add the next data point to the partial dataset
        if self.current_index < len(self.data):
            self.partial_data = np.vstack([self.partial_data, self.data[self.current_index]])
            self.current_index += 1

        # Perform outlier detection on the partial dataset
        if len(self.partial_data) > 1:  # Isolation Forest requires at least two samples
            iso_forest = IsolationForest(contamination=self.contamination, random_state=42)
            self.outliers = iso_forest.fit_predict(self.partial_data)

        # Separate inliers and outliers
        inliers = self.partial_data[self.outliers == 1]
        outliers = self.partial_data[self.outliers == -1]

        # Plot the partial dataset
        if len(inliers) > 0:
            self.ax.scatter(inliers[:, 0], inliers[:, 1], color='blue', label='Inliers')
        if len(outliers) > 0:
            self.ax.scatter(outliers[:, 0], outliers[:, 1], color='red', label='Outliers', marker='x')

        # Add titles and labels
        self.ax.set_title(f"Isolation Forest Outlier Detection (Frame {frame})")
        self.ax.set_xlabel("Feature 1 (LAN)")
        self.ax.set_ylabel("Feature 2 (LON)")
        self.ax.legend()

        # Stop the animation when all data points are added
        if self.current_index >= len(self.data):
            self.anim.event_source.stop()