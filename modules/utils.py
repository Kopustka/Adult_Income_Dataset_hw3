def clean_data(data):
    """
    This function performs data cleaning by checking for missing values and removing rows with missing data.

    :param data: The input dataset (usually a pandas DataFrame).
    :return: A cleaned version of the dataset with missing values removed.
    """
    # Checking for missing values (NaN) in each column of the dataset
    print(data.isnull().sum())  # Prints the number of missing values in each column

    # Dropping rows that contain missing values (NaN) in any column
    data = data.dropna()  # Removes any row that has at least one missing value

    # Returning the cleaned data
    return data
