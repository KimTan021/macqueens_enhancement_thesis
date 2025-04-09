from utils.perform_kmeans import perform_kmeans
from sklearn.metrics import silhouette_score
import numpy as np
import streamlit as st
from sklearn.metrics import davies_bouldin_score

@st.cache_data
def calculate_metrics(data, algorithm, init, noise_level):
    """
    Calculate various clustering evaluation metrics.

    Parameters:
    data (pandas.DataFrame): The input data containing the clusters.
    algorithm (str): The clustering algorithm to use.
    init (str): The method for initialization of centroids.
    noise_level (float): The level of noise to add to the data.

    Returns:
    tuple: A tuple containing the average silhouette score, standard deviation index, Davies-Bouldin index, and within-cluster sum of squares.
    """

    avg_silhouette, _, best_labels = average_silhouette_score(data, n_clusters=len(data['cluster'].unique()),
                                                              algorithm=algorithm, init=init,
                                                              noise_level=noise_level)
    sd_index = standard_deviation_index(data[["AREA CODE"]].values, best_labels)
    db_index = davies_bouldin_score(data[["AREA CODE"]].values, best_labels)
    wcss = within_cluster_sum_of_squares(data[["AREA CODE"]].values, best_labels)
    return avg_silhouette, sd_index, db_index, wcss

@st.cache_data
def average_silhouette_score(data, n_clusters, algorithm, init="random", iterations=3, noise_level=0.0):
    """
    Calculate the average silhouette score for a given clustering algorithm.

    Parameters:
    data (pandas.DataFrame): The input data containing the clusters.
    n_clusters (int): The number of clusters to form.
    algorithm (str): The clustering algorithm to use.
    init (str, optional): The method for initialization of centroids. Default is "random".
    iterations (int, optional): The number of iterations to run the clustering algorithm. Default is 3.
    noise_level (float, optional): The level of noise to add to the data. Default is 0.0.

    Returns:
    tuple: A tuple containing the average silhouette score, the maximum silhouette score, and the labels for the best clustering.
    """

    scores = []
    max_score = -1
    best_labels = None

    for _ in range(iterations):
        labels = perform_kmeans(data, n_clusters, algorithm, init, noise_level=noise_level)
        score = silhouette_score(data[["AREA CODE"]], labels)
        scores.append(score)
        if score > max_score:
            max_score = score
            best_labels = labels
    avg_score = np.mean(scores)
    return avg_score, max_score, best_labels


# Define the functions for the additional metrics
@st.cache_data
def standard_deviation_index(X, labels):
    """
    Calculate the standard deviation index for clustering.

    Parameters:
    X (numpy.ndarray): The input data points.
    labels (numpy.ndarray): The cluster labels for each data point.

    Returns:
    float: The standard deviation index, which measures the dispersion of cluster means from the overall mean.
    """

    clusters = np.unique(labels)
    cluster_means = np.array([X[labels == cluster].mean(axis=0) for cluster in clusters])
    overall_mean = X.mean(axis=0)
    sd_index = np.sqrt(np.sum((cluster_means - overall_mean) ** 2) / len(clusters))
    return sd_index

@st.cache_data
def within_cluster_sum_of_squares(X, labels):
    """
    Calculate the within-cluster sum of squares (WCSS) for clustering.

    Parameters:
    X (numpy.ndarray): The input data points.
    labels (numpy.ndarray): The cluster labels for each data point.

    Returns:
    float: The within-cluster sum of squares, which measures the total variance within each cluster.
    """

    clusters = np.unique(labels)
    wcss = 0
    for cluster in clusters:
        cluster_points = X[labels == cluster]
        cluster_center = cluster_points.mean(axis=0)
        wcss += np.sum((cluster_points - cluster_center) ** 2)
    return wcss