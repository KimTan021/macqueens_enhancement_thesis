import folium
import random
import webbrowser

from utils.label_encoder import apply_fuzzy_and_label_encoder
from utils.find_optimal_cluster import find_optimal_clusters


def process_cluster(df, cluster_label):
    """
    Processes a given cluster of crime data, applies fuzzy matching and label encoding,
    finds the optimal number of sub-clusters, and generates a folium map with crime markers.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing crime data.
    cluster_label (int): The label of the cluster to process.

    Returns:
    None
    """

    cluster_df = df[df["cluster"] == cluster_label].copy()

    # Apply fuzzy matching and label encoding on "Crm Cd Desc"
    cluster_df = apply_fuzzy_and_label_encoder(cluster_df, "Crm Cd Desc", "MAPPED CRIME TYPE", "CRIME CODE")

    # Find optimal number of clusters using CRIME CODE
    optimal_k, labels = find_optimal_clusters(cluster_df[["CRIME CODE"]], plot=False)
    print(f"Optimal number of clusters for cluster {cluster_label}: {optimal_k}")

    # Ensure labels are not None
    if labels is None:
        print(f"Error: No labels generated for cluster {cluster_label}.")
    else:
        cluster_df["crime_cluster"] = labels

        # Retrieve the mapped area name for the current cluster
        location = cluster_df["MAPPED AREA NAME"].iloc[0]

        # Create a folium map centered around the mean latitude and longitude of the cluster
        mean_lat = cluster_df["LAT"].mean()
        mean_lon = cluster_df["LON"].mean()
        crime_map = folium.Map(location=[mean_lat, mean_lon], zoom_start=12)

        rand_colors = [
            "red", "blue", "green", "purple", "orange", "darkred", "lightred",
            "beige", "darkblue", "darkgreen", "cadetblue", "darkpurple",
            "pink", "lightblue", "lightgreen", "gray", "black", "lightgray"
        ]
        # Generate a unique color for each crime type
        unique_crimes = cluster_df["MAPPED CRIME TYPE"].unique()
        crime_colors = {crime: random.choice(rand_colors) for crime in unique_crimes}

        # Add markers for each crime type in the cluster
        for _, row in cluster_df.iterrows():
            mapped_crime_type = row["MAPPED CRIME TYPE"]
            crime_color = crime_colors[mapped_crime_type]
            folium.Marker(
                location=[row["LAT"], row["LON"]],
                popup=(
                    f"<b>Crime Type:</b> {mapped_crime_type}<br><br>"
                    f"<b>Date Reported:</b> {row['Date Rptd']}<br><br>"
                    f"<b>Date Occurred:</b> {row['DATE OCC']}<br><br>"
                    f"<b>Time Occurred:</b> {row['TIME OCC']}<br><br>"
                    f"<b>Area Name:</b> {row['AREA NAME']}<br><br>"
                    f"<b>Victim Age:</b> {row['Vict Age']}<br><br>"
                    f"<b>Victim Sex:</b> {row['Vict Sex']}<br><br>"
                    f"<b>Status:</b> {row['Status']}<br><br>"
                    f"<b>Location:</b> {row['LOCATION']}"
                ),
                icon=folium.Icon(color=crime_color, icon="info-sign")
            ).add_to(crime_map)

        # Add a legend to the map
        crime_counts = cluster_df["MAPPED CRIME TYPE"].value_counts()
        legend_html = '''
        <div style="position: fixed; top: 10px; right: 10px; width: 200px; height: auto; max-height: 300px; overflow-y: auto; z-index:9999; font-size:14px; background-color: white; padding: 10px; border: 2px solid black; box-sizing: border-box;">
        '''
        legend_html += f'<b>Different Crimes in {location}</b><br><br>'
        for crime, count in crime_counts.items():
            color = crime_colors[crime]
            legend_html += f'<i style="background:{color};width:12px;height:12px;display:inline-block;"></i> <b style="font-size:12px;">{crime.title()}</b>: <span style="font-size:12px;">{count}</span><br><br>'
        legend_html += '</div>'
        crime_map.get_root().html.add_child(folium.Element(legend_html))

        # Save the map to an HTML file
        map_file = f'{location}_crime_map.html'
        crime_map.save(map_file)

        # Open the HTML file in the default web browser
        webbrowser.open(map_file)