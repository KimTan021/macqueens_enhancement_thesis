import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
import matplotlib.pyplot as plt

from utils.find_optimal_cluster import find_optimal_clusters
from utils.label_encoder import apply_fuzzy_and_label_encoder
from utils.process_clusters_app import process_cluster

@st.cache_data
def load_data():
    """
    Load and preprocess the crime data.

    This function reads the crime data from a CSV file, limits the data to the first 500 rows,
    and applies fuzzy matching and label encoding to the specified columns.

    Returns:
    pd.DataFrame: The preprocessed DataFrame containing the crime data.
    """

    df = pd.read_csv("data/Crime_Data_from_2020_to_Present.csv")
    df = df[:500]
    df = apply_fuzzy_and_label_encoder(df, "AREA NAME", "MAPPED AREA NAME", "AREA CODE")
    return df

@st.cache_data
def generate_location_clusters(df):
    """
    Generate location clusters for the given DataFrame.

    This function finds the optimal number of clusters for the 'AREA CODE' column in the DataFrame,
    detects outliers, and assigns cluster labels to the DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the 'AREA CODE' column.

    Returns:
    pd.DataFrame: The DataFrame with an additional 'cluster' column containing the cluster labels.
    """

    detect_outliers = True
    optimal_k, labels, outliers = find_optimal_clusters(df[["AREA CODE"]], plot=False, detect_outliers=detect_outliers, plot_outliers=False)
    print(f"Optimal number of clusters: {optimal_k}")
    if labels is None:
        print("Error: No labels generated.")
    elif detect_outliers:
        non_outlier_mask = outliers == 1
        df["cluster"] = -1
        df.loc[non_outlier_mask, "cluster"] = labels
    else:
        df["cluster"] = labels
    return df

def app():
    if "data" not in st.session_state:
        st.session_state.data = generate_location_clusters(load_data())

    cluster_location_map = st.session_state.data.groupby("cluster")["AREA NAME"].first().to_dict()
    location_names = list(cluster_location_map.values())

    selected_location = st.selectbox("Select a location", location_names)

    if selected_location:
        selected_cluster = list(cluster_location_map.keys())[list(cluster_location_map.values()).index(selected_location)]
        crime_map, crime_clusters = process_cluster(st.session_state.data, selected_cluster)
        st.session_state.crime_clusters = crime_clusters  # Save crime_clusters in session state
        folium_static(crime_map)

        crime_counts = crime_clusters["MAPPED CRIME TYPE"].value_counts()

        st.write("### Crime Occurrences")
        fig, ax = plt.subplots()
        crime_counts.plot(kind='bar', ax=ax)
        ax.set_xlabel("Crime Type")
        ax.set_ylabel("Number of Occurrences")
        ax.set_title("Crime Occurrences in Selected Location")
        st.pyplot(fig)

        st.write("### Crime Counts")
        st.write(crime_counts)

        most_frequent_crime = crime_counts.idxmax()
        most_frequent_crime_count = crime_counts.max()
        st.write(f"### Findings")
        st.write(f"The most frequent crime in **{selected_location}** is **{most_frequent_crime.lower()}** with **{most_frequent_crime_count}** occurrences.")