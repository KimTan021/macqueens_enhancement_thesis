import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from utils.kmeans_visualizer import KMeansVisualizer

def visualize_kmeans(data, n_clusters, algorithm, init, max_iter=300, noise_level=0.0):
    """
    Visualizes the K-Means clustering process on a given dataset.

    Parameters:
    data (pd.DataFrame): The input data containing 'LAT' and 'LON' columns for latitude and longitude.
    n_clusters (int): The number of clusters to form.
    algorithm (str): The K-Means algorithm to use.
    init (str): Method for initialization, defaults to 'k-means++'.
    max_iter (int, optional): Maximum number of iterations of the K-Means algorithm for a single run. Default is 300.
    noise_level (float, optional): The level of noise to add to the data. Default is 0.0.

    Returns:
    None
    """

    noisy_data = data[["LAT", "LON"]].values + noise_level * np.random.randn(*data[["LAT", "LON"]].shape)
    maxval = noisy_data.max(axis=0).max()
    normalized_data = noisy_data / maxval

    fig, ax = plt.subplots()

    visualizer = KMeansVisualizer(n_clusters, normalized_data, algorithm, init, max_iter, ax, None)
    anim = FuncAnimation(fig, visualizer.fit, frames=max_iter, interval=1000, repeat=False)
    visualizer.anim = anim
    plt.show()