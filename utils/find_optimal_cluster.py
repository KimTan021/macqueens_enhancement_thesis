from sklearn.cluster import KMeans
import numpy as np
from matplotlib import pyplot as plt
import warnings
from sklearn.exceptions import ConvergenceWarning
from sklearn.ensemble import IsolationForest


def gap_statistic(x, kmax=20, b=20):
    """
    Computes the gap statistic for determining the optimal number of clusters.

    Parameters:
    x (numpy.ndarray): The input data for clustering.
    kmax (int, optional): The maximum number of clusters to consider. Default is 20.
    b (int, optional): The number of reference datasets to generate. Default is 20.

    Returns:
    tuple: A tuple containing the gap values for each number of clusters and the optimal number of clusters.
    """

    gaps = []
    wks = []
    wkbs = []
    for k in range(1, kmax + 1):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=ConvergenceWarning)
            kmeans = KMeans(n_clusters=k, random_state=42, n_init=27, max_iter=500, tol=1e-4).fit(x)
            inertia = kmeans.inertia_
            if inertia > 0:
                wk = np.log(inertia)
            else:
                wk = 0  # Handle zero or negative inertia
            wks.append(wk)

            ref_disps = np.zeros(b)
            for i in range(b):
                random_reference = np.random.uniform(np.min(x), np.max(x), x.shape)
                ref_kmeans = KMeans(n_clusters=k, random_state=42).fit(random_reference)
                ref_inertia = ref_kmeans.inertia_
                if ref_inertia > 0:
                    ref_disps[i] = np.log(ref_inertia)
                else:
                    ref_disps[i] = 0  # Handle zero or negative inertia

            wkb = np.mean(ref_disps)
            wkbs.append(wkb)
            gaps.append(wkb - wk)

    gaps = np.array(gaps)
    if len(gaps) > 1:
        optimal_k = np.argmax(gaps[:-1] - gaps[1:] + np.log(kmax)) + 1
    else:
        optimal_k = 1  # Default to 1 if gaps array is too small
    print(f"Gaps: {gaps}")
    print(f"Optimal k (gap statistic): {optimal_k}")
    return gaps, optimal_k


def find_optimal_clusters(X, max_k=50, plot=False, random_state=42, detect_outliers=False, plot_outliers=False):
    """
    Finds the optimal number of clusters for K-Means clustering using the gap statistic method.

    Parameters:
    X (numpy.ndarray): The input data for clustering.
    max_k (int, optional): The maximum number of clusters to consider. Default is 50.
    plot (bool, optional): Whether to plot the gap statistic. Default is False.
    random_state (int, optional): The random seed for reproducibility. Default is 42.
    detect_outliers (bool, optional): Whether to detect and remove outliers using IsolationForest. Default is False.
    plot_outliers (bool, optional): Whether to plot the outliers detected by IsolationForest. Default is False.

    Returns:
    tuple: A tuple containing the optimal number of clusters, the labels for each data point, and the outliers (if detected).
    """

    outliers = None
    if detect_outliers:
        # Detect and remove outliers using Isolation Forest
        iso_forest = IsolationForest(contamination=0.1, random_state=random_state)
        outliers = iso_forest.fit_predict(X)

        if plot_outliers:
            import matplotlib.pyplot as plt
            import pandas as pd

            # Convert to NumPy array if X is a DataFrame
            X_np = X.values if isinstance(X, pd.DataFrame) else X
            inliers = X_np[outliers == 1]
            outliers_data = X_np[outliers == -1]

            plt.figure(figsize=(8, 6))
            if inliers.shape[1] == 1:
                # Single feature: plot against an index
                plt.scatter(range(len(inliers)), inliers[:, 0], color='blue', label='Inliers')
                plt.scatter(range(len(outliers_data)), outliers_data[:, 0], color='red', label='Outliers', marker='x')
                plt.xlabel("Index")
                plt.ylabel("Feature Value")
            else:
                # Two or more features: plot the first two features
                plt.scatter(inliers[:, 0], inliers[:, 1], color='blue', label='Inliers')
                plt.scatter(outliers_data[:, 0], outliers_data[:, 1], color='red', label='Outliers', marker='x')

            plt.title("Outlier Detection using Isolation Forest")
            plt.legend()
            plt.show()

        X = X[outliers == 1]  # Keep only non-outliers

    n_samples = X.shape[0]
    if max_k >= n_samples:
        max_k = n_samples - 1

    gaps, gap_optimal_k = gap_statistic(X, max_k)
    print(f"Gaps: {gaps}, Optimal k (gap statistic): {gap_optimal_k}")

    kmeans = KMeans(n_clusters=gap_optimal_k, random_state=random_state, n_init=27, max_iter=500, tol=1e-4)
    kmeans.fit(X)
    best_labels = kmeans.labels_

    if plot:
        plt.figure(figsize=(15, 5))

        plt.subplot(1, 1, 1)
        plt.plot(range(1, len(gaps) + 1), gaps, 'bo-')
        plt.xlabel('Number of clusters (k)')
        plt.ylabel('Gap Statistic')
        plt.title('Gap Statistic Method')

        plt.tight_layout()
        plt.show()

    return gap_optimal_k, best_labels, outliers
