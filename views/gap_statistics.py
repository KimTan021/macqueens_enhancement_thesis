import matplotlib.pyplot as plt
import streamlit as st

from utils.find_optimal_cluster_app import find_optimal_clusters

def app():
        optimal_k, gaps = find_optimal_clusters(st.session_state.data[["AREA CODE"]], max_k=50, random_state=42, detect_outliers=False)

        plt.figure(figsize=(15, 5))
        plt.plot(range(1, len(gaps) + 1), gaps, 'bo-')
        plt.xlabel('Number of clusters (k)')
        plt.ylabel('Gap Statistic')
        plt.title('Gap Statistic Method')
        plt.tight_layout()

        st.pyplot(plt)

        st.write(f"**Optimal number of clusters:** {optimal_k}")

        st.write("### Interpretation of the Gap Statistic Method")
        st.write("The figure above shows the result of the Gap Statistic method for finding the optimal number of "
                 "clusters (k) in a dataset. The x-axis represents the number of clusters, while the y-axis measures "
                 "clustering quality.")
        st.write("The blue line indicates the Gap Statistic values for different cluster numbers. Based on the figure, "
                 f"the optimal number of clusters (k) is {optimal_k}, identified where the Gap Statistic reaches its maximum or "
                 "stabilizes.")
        st.write(f"- **Steep Increase:** From k = 1 to k = {optimal_k}, there is a significant increase in the Gap Statistic, "
                 "indicating improved clustering quality.")
        st.write(f"- **Plateau Behavior:** After k = {optimal_k}, the Gap Statistic becomes constant, suggesting no further "
                 "improvement in clustering.")
        st.write(f"The stabilization at k={optimal_k} implies that increasing the number of clusters beyond this point doesn't "
                 "improve clustering, hence it is chosen as the optimal number of clusters.")