def print_cluster_data(df):
    """
    Prints the data for each unique cluster in the given DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing cluster data.
                       It must have a column named 'cluster' to identify clusters.

    Returns:
    None
    """

    # Iterate through unique cluster labels in the 'cluster' column
    for cluster_label in df["cluster"].unique():
        cluster_df = df[df["cluster"] == cluster_label][["AREA NAME", "MAPPED AREA NAME", "AREA CODE"]]
        print(f"\nCluster {cluster_label}:\n", cluster_df)
    print(f"Total number of unique clusters: {len(df['cluster'].unique())}")