import streamlit as st
import pandas as pd

def app():
    st.write("### Existing Algorithm")
    st.image("images/orig_macqueen.png")

    st.write("### Proposed Algorithm")

    st.write("The proposed algorithm fixes the issues regarding outlier sensitivity, predefined number of clusters, "
             "and centroid initialization. In addition, the researchers applied the isolation forest algorithm for "
             "outlier detection and removal, gap statistics for finding the optimal number of clusters (k), and an "
             "adaptive k-means++ algorithm for the centroid initialization. Below is the pseudocode of the proposed "
             "algorithm:")

    st.image("images/enhanced_macqueen.png")

    data = {
        'Problems': ["MacQueen’s K-Means Algorithm exhibits high sensitivity to the initial placement of centroids.",
                     "MacQueen’s K-Means Algorithm is sensitive and cannot handle outliers.",
                     "MacQueen’s K-Means Algorithm requires a pre-defined number of clusters."
                    ],
        'Solutions': ["Developed an improved initialization method by incorporating an adaptive k-means++ approach.",
                      "Applied isolation forest to eliminate outliers.",
                      "Applied the gap statistics method for finding the optimal number of clusters (k)."
                    ]
    }

    df = pd.DataFrame(data)
    st.markdown("### Enhancements Made")
    st.table(df)