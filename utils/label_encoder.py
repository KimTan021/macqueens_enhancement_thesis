from fuzzywuzzy import fuzz
from sklearn.preprocessing import LabelEncoder

def fuzzy_group(locations, threshold=80):
    """
    Groups similar locations based on a fuzzy matching threshold.

    Parameters:
    locations (list): A list of location names to be grouped.
    threshold (int, optional): The similarity threshold for grouping locations. Default is 80.

    Returns:
    dict: A dictionary mapping each location to its grouped representative.
    """

    grouped_locations = []
    for loc in locations:
        loc = str(loc)  # Ensure the location is a string
        found = False
        for group in grouped_locations:
            similarity = fuzz.ratio(loc, group[0])
            print(f"Comparing '{loc}' with '{group[0]}': Similarity = {similarity}")
            if similarity >= threshold:
                group.append(loc)
                found = True
                break
        if not found:
            grouped_locations.append([loc])
    location_mapping = {loc: group[0] for group in grouped_locations for loc in group}
    return location_mapping


# Ensure the correct column name is used for mapping crime types
def apply_fuzzy_and_label_encoder(df, column_name, fuzzy_column_name, encoder_column_name):
    """
    Applies fuzzy matching to group similar area names and encodes the grouped names into numerical values.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the data.
    column_name (str): The name of the column to apply fuzzy matching on.
    fuzzy_column_name (str): The name of the new column to store the fuzzy matched area names.
    encoder_column_name (str): The name of the new column to store the encoded numerical values.

    Returns:
    pd.DataFrame: The DataFrame with the new fuzzy matched and encoded columns added.
    """

    # Apply fuzzy matching and group similar area names
    location_mapping_result = fuzzy_group(df[column_name].tolist())
    df[fuzzy_column_name] = df[column_name].map(location_mapping_result)

    # Convert the mapped area names to numerical values using LabelEncoder
    label_encoder = LabelEncoder()
    df[encoder_column_name] = label_encoder.fit_transform(df[fuzzy_column_name])

    return df