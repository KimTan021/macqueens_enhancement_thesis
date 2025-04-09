import streamlit as st
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest
from utils.find_optimal_cluster import gap_statistic

@st.cache_data
def find_optimal_clusters(X, max_k=50, random_state=42, detect_outliers=False):
    """
    Finds the optimal number of clusters for K-Means clustering using the gap statistic method.

    Parameters:
    X (numpy.ndarray): The input data for clustering.
    max_k (int, optional): The maximum number of clusters to consider. Default is 50.
    random_state (int, optional): The random seed for reproducibility. Default is 42.
    detect_outliers (bool, optional): Whether to detect and remove outliers using IsolationForest. Default is False.

    Returns:
    tuple: A tuple containing the optimal number of clusters and the gap values for each number of clusters.
    """

    if detect_outliers:
        # Detect and remove outliers using IsolationForest
        iso_forest = IsolationForest(contamination=0.1, random_state=random_state)
        outliers = iso_forest.fit_predict(X)
        X = X[outliers == 1]  # Keep only non-outliers

    n_samples = X.shape[0]
    if max_k >= n_samples:
        max_k = n_samples - 1

    gaps, gap_optimal_k = gap_statistic(X, max_k)
    print(f"Gaps: {gaps}, Optimal k (gap statistic): {gap_optimal_k}")

    return gap_optimal_k, gaps