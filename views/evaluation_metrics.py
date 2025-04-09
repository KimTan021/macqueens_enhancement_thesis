import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from utils.evaluation_metrics_calculation import calculate_metrics

def app():
    noise_level = 0.1  # Adjust the noise level as needed

    # Define the algorithms and metrics
    algorithms = ["lloyd", "elkan", "macqueen", "macqueen_adaptive"]
    metrics = ["Silhouette Score", "Standard Deviation Index", "Davies-Bouldin Index", "WCSS"]

    # Add a dropdown to select the metric with "Silhouette Score" as the default
    selected_metric = st.selectbox("Select Metric", metrics, index=0)

    # Initialize a dictionary to store the selected metric values
    if "metric_values" not in st.session_state:
        st.session_state.metric_values = {}

    if selected_metric not in st.session_state.metric_values:
        metric_values = []
        for algorithm in algorithms:
            if algorithm == "macqueen_adaptive":
                init = "adaptive"
            else:
                init = "random"

            avg_silhouette, sd_index, db_index, wcss = calculate_metrics(st.session_state.data, algorithm.split('_')[0], init, noise_level)
            metric_value = None
            # Select the appropriate metric value
            if selected_metric == "Silhouette Score":
                metric_value = avg_silhouette
            elif selected_metric == "Standard Deviation Index":
                metric_value = sd_index
            elif selected_metric == "Davies-Bouldin Index":
                metric_value = db_index
            elif selected_metric == "WCSS":
                metric_value = wcss

            metric_values.append(metric_value)

        st.session_state.metric_values[selected_metric] = metric_values
    else:
        metric_values = st.session_state.metric_values[selected_metric]

    # Plot the selected metric using Streamlit
    st.write(f"### {selected_metric} of Different Clustering Algorithms")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(algorithms, metric_values)
    ax.set_ylabel(selected_metric)
    ax.set_title(f"{selected_metric} of Different Clustering Algorithms")
    st.pyplot(fig)

    # Create a DataFrame to store the selected metric
    metrics_df = pd.DataFrame({
        "Algorithm": [algorithm.capitalize() for algorithm in algorithms],
        selected_metric: metric_values
    })

    # Display the DataFrame as a table in Streamlit
    st.write(f"### {selected_metric} Table")
    st.table(metrics_df)

    # Add a description based on the metric selected
    if selected_metric == "Silhouette Score":
        st.write("The **Silhouette Score** measures how similar a data point is to its own cluster compared to other "
                 "clusters. It ranges from -1 to +1, where **a score close to +1 indicates that the data point is "
                 "well-clustered, while scores near 0 suggest overlapping clusters, and negative scores indicate "
                 "misclassification** (Rousseeuw, 1987). This metric provides insight into both cluster cohesion and "
                 "separation, making it a valuable tool for assessing the quality of clustering.")
    elif selected_metric == "Standard Deviation Index":
        st.write("The **Standard Deviation (SD)** Index is utilized to assess the spread of data points within each "
                 "cluster. **A lower standard deviation indicates that data points are closely packed within their "
                 "respective clusters**, which is desirable for effective clustering (Javatpoint). This metric can "
                 "help identify potential biases in cluster formation by examining how tightly or loosely data "
                 "points are grouped.")
    elif selected_metric == "Davies-Bouldin Index":
        st.write("The **Davies-Bouldin Index** evaluates the compactness and separation of clusters by comparing the "
                 "average similarity of each cluster with its most similar neighbor. **A lower DB index indicates "
                 "better-defined clusters**, as it reflects higher intra-cluster similarity and lower inter-cluster "
                 "similarity (Davies & Bouldin, 1979). This metric helps in determining the effectiveness of the "
                 "clustering algorithm in distinguishing between different clusters.")
    elif selected_metric == "WCSS":
        st.write("The **Within-Cluster Sum of Squares (WCSS)** quantifies how tightly clustered the data points are "
                 "within each cluster. **A lower WCSS value signifies more compact clusters, suggesting that the "
                 "clustering algorithm has effectively grouped similar data points together**. Comparing WCSS values "
                 "between the existing MacQueen's algorithm and the enhanced algorithm will provide quantitative "
                 "evidence of improvement in clustering performance.")