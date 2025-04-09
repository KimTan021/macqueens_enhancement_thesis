import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from utils.process_clusters_app import process_cluster

def app():
    if "data" not in st.session_state:
        st.error("Please select a location in the Crime Hotspots tab first.")
        return


    st.write("In this tab, you can combine crimes from your selected locations. This feature helps you explore "
             "more detailed statistics and uncover different crime patterns in specific areas.")

    # Select multiple locations
    cluster_location_map = st.session_state.data.groupby("cluster")["AREA NAME"].first().to_dict()
    location_names = list(cluster_location_map.values())
    selected_locations = st.multiselect("Select locations", location_names)

    if not selected_locations:
        st.warning("Please select at least one location.")
        return

    # Process clusters for selected locations
    combined_crime_clusters = pd.DataFrame()
    for location in selected_locations:
        selected_cluster = list(cluster_location_map.keys())[list(cluster_location_map.values()).index(location)]
        _, crime_clusters = process_cluster(st.session_state.data, selected_cluster)
        combined_crime_clusters = pd.concat([combined_crime_clusters, crime_clusters])

    # Check if the column exists
    if "MAPPED CRIME TYPE" not in combined_crime_clusters.columns:
        st.error("The column 'MAPPED CRIME TYPE' does not exist in the data.")
        return

    # Select multiple crime types
    crime_types = combined_crime_clusters["MAPPED CRIME TYPE"].unique()
    selected_crime_types = st.multiselect("Select crime types", crime_types)

    if not selected_crime_types:
        st.warning("Please select at least one crime type.")
        return

    # Create a pivot table with counts of individual crimes for each location
    crime_counts_pivot = combined_crime_clusters[combined_crime_clusters["MAPPED CRIME TYPE"].isin(selected_crime_types)].pivot_table(
        index="AREA NAME",
        columns="MAPPED CRIME TYPE",
        aggfunc="size",
        fill_value=0
    )

    # Add a column for the combined counts of selected crimes for each location
    crime_counts_pivot["Combined Count"] = crime_counts_pivot.sum(axis=1)

    # Plot the combined crime counts
    if not crime_counts_pivot.empty:
        st.write("### Combined Crime Occurrences by Location")
        fig, ax = plt.subplots()
        crime_counts_pivot["Combined Count"].plot(kind='bar', ax=ax)
        ax.set_xlabel("Location")
        ax.set_ylabel("Number of Occurrences")
        ax.set_title("Combined Crime Occurrences in Selected Locations")
        st.pyplot(fig)

        # Display the updated table
        st.write("### Combined Crime Counts by Location")
        st.write(crime_counts_pivot)

        most_frequent_location = crime_counts_pivot["Combined Count"].idxmax()
        most_frequent_crime_count = crime_counts_pivot["Combined Count"].max()
        st.write(f"### Findings")
        st.write(f"The location with the highest combined occurrences of the selected crimes is **{most_frequent_location}** with **{most_frequent_crime_count}** occurrences.")