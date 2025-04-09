import streamlit as st

def app():
    st.write("### Macqueen's Algorithm")

    st.write("MacQueen's algorithm, introduced by James MacQueen in 1967, is a variant of the k-means clustering method "
             "that enhances the traditional approach by updating centroids incrementally as data points are assigned to "
             "clusters. This algorithm operates under the principle of partitioning a dataset into k distinct clusters, "
             "where k is predetermined, by minimizing the within-cluster sum of squares (WCSS).")

    st.write("The process begins with the random selection of k initial centroids, after which each data point is "
             "assigned to the nearest centroid based on a chosen distance metric, typically Euclidean distance. Unlike "
             "the standard k-means algorithm, which recalculates centroids only after all points have been assigned, "
             "MacQueen's algorithm updates the centroid immediately after each assignment.")

    st.write("This iterative approach continues until no further changes occur in point assignments, resulting in a "
             "more dynamic and potentially faster convergence towards an optimal clustering configuration.")

    st.write("Although MacQueen's algorithm improves upon the basic k-means method by addressing centroid updates "
             "during each iteration, it remains sensitive to the initial placement of centroids and does not guarantee "
             "finding the global optimum (MacQueen, 1967; Hartigan & Wong, 1979).")