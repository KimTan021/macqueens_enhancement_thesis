import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.metrics import davies_bouldin_score
from utils.find_optimal_cluster import find_optimal_clusters
from utils.label_encoder import apply_fuzzy_and_label_encoder
from utils.evaluation_metrics_calculation import average_silhouette_score
from utils.evaluation_metrics_calculation import standard_deviation_index, within_cluster_sum_of_squares

# Load and preprocess the data
df = pd.read_csv("data/Crime_Data_from_2020_to_Present.csv")
df = df[:500]
df = apply_fuzzy_and_label_encoder(df, "AREA NAME", "MAPPED AREA NAME", "AREA CODE")

# Find optimal number of clusters using AREA CODE
detect_outliers = True
optimal_k, labels, outliers = find_optimal_clusters(df[["AREA CODE"]], plot=True, detect_outliers=detect_outliers)
print(f"Optimal number of clusters: {optimal_k}")

# Ensure labels are not None
if labels is None:
    print("Error: No labels generated.")
elif detect_outliers:
    # Create a mask for non-outliers
    # iso_forest = IsolationForest(contamination=0.1, random_state=42)
    # outliers = iso_forest.fit_predict(df[["AREA CODE"]])
    non_outlier_mask = outliers == 1

    # Assign labels to the original DataFrame
    df["cluster"] = -1  # Initialize with -1 for outliers
    df.loc[non_outlier_mask, "cluster"] = labels
else:
    df["cluster"] = labels

# Calculate average silhouette scores for different algorithms
noise_level = 0.1  # Adjust the noise level as needed

# Calculate additional metrics for each algorithm
algorithms = ["lloyd", "elkan", "macqueen", "macqueen_kmeans++", "macqueen_adaptive"]
metrics = {
    "Silhouette Score": [],
    "Standard Deviation Index": [],
    "Davies-Bouldin Index": [],
    "WCSS": []
}

for algorithm in algorithms:
    if algorithm == "macqueen_adaptive":
        init = "adaptive"
    elif algorithm == "macqueen_kmeans++":
        init = "k-means++"
    else:
        init = "random"

    avg_silhouette, _, best_labels = average_silhouette_score(df, n_clusters=len(df['cluster'].unique()),
                                                      algorithm=algorithm.split('_')[0], init=init,
                                                      noise_level=noise_level)

    # Calculate metrics based on the labels generated by the current algorithm
    sd_index = standard_deviation_index(df[["AREA CODE"]].values, best_labels)
    db_index = davies_bouldin_score(df[["AREA CODE"]].values, best_labels)
    wcss = within_cluster_sum_of_squares(df[["AREA CODE"]].values, best_labels)

    metrics["Silhouette Score"].append(avg_silhouette)
    metrics["Standard Deviation Index"].append(sd_index)
    metrics["Davies-Bouldin Index"].append(db_index)
    metrics["WCSS"].append(wcss)

    print(f"{algorithm.capitalize()} Algorithm:")
    print(f"  Silhouette Score: {avg_silhouette}")
    print(f"  Standard Deviation Index: {sd_index}")
    print(f"  Davies-Bouldin Index: {db_index}")
    print(f"  WCSS: {wcss}")

# Plot the results
for metric, values in metrics.items():
    plt.figure(figsize=(10, 6))
    plt.bar(algorithms, values)
    plt.ylabel(metric)
    plt.title(f"{metric} of Different Clustering Algorithms")
    plt.show()