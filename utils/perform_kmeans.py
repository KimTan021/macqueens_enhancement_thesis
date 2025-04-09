from sklearn.cluster import KMeans
import numpy as np

def perform_kmeans(data, n_clusters, algorithm, init, max_iter=300, noise_level=0.0):
    """
    Performs K-Means clustering on the given data with optional noise addition.

    Parameters:
    data (pd.DataFrame): The input DataFrame containing the data to cluster.
    n_clusters (int): The number of clusters to form.
    algorithm (str): The K-Means algorithm to use ('auto', 'full', or 'elkan').
    init (str or ndarray): Method for initialization ('k-means++', 'random', or an ndarray).
    max_iter (int, optional): Maximum number of iterations of the K-Means algorithm. Default is 300.
    noise_level (float, optional): The standard deviation of Gaussian noise to add to the data. Default is 0.0.

    Returns:
    np.ndarray: Array of cluster labels for each data point.
    """

    # Add noise to the data
    noisy_data = data[["AREA CODE"]].values + noise_level * np.random.randn(*data[["AREA CODE"]].shape)

    kmeans = KMeans(n_clusters=n_clusters, algorithm=algorithm, init=init, max_iter=max_iter, random_state=42)
    labels = kmeans.fit_predict(noisy_data)
    data["cluster"] = labels

    return labels