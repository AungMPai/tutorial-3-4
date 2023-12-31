# Problem 2: Print information about the data frame contents
from pathlib import Path

import pandas as pd


def create_dataframe(csv_file):
    """ Creates, prints and returns a pandas dataframe containing data from a csv file

    Args:
        csv_file: The raw data in csv format

    Returns:
        df: A pandas dataframe with the data

    """

    # Create a dataframe with the csv file as its contents
    df = pd.read_csv(csv_file)

    # Change the pandas display options for the max_rows and max_columns
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)

    # Print the dataframe contents (remove the # from the line below)
    # print("\nDataFrame contents:\n", df)

    # Return the dataframe
    return df


def print_df_information(df):
    """ Prints information that the describes the contents of the DataFrame.

    Args:
        df: A pandas dataframe containing the data
    """
    # Print the number of rows and columns in the DataFrame using `.shape()`
    print("\nNumber of rows and columns:\n")
    num_rows, num_columns = df.shape
    print(f"Number of rows: {num_rows}")
    print(f"Number of columns: {num_columns}")  # Add your code inside the brackets

    # Print the first 7 rows of data using `.head()` and the last 6 rows using `.tail()`
    print("\nFirst 7 rows:\n")
    print(df.head(7))  # Add your code inside the brackets
    print("\nLast 6 rows:\n")
    print(df.tail(6))  # Add your code inside the brackets

    #  Print the column labels using `.info()` or `.columns`.
    #  Are there any columns that you don't think will be needed to answer the questions?
    print("\nColumn labels:\n")
    print(df.columns)  # Add your code inside the brackets

    # Print the column data types using `.info()` or `.dtypes`
    print("\nColumn data types:\n")
    print(df.dtypes)  # Add your code inside the brackets

    # Print general statistics using `.describe()`
    # Why are some columns not shown in the output?
    print("\nStatistics:\n")
    print(df.describe())  # Add your code inside the brackets


if __name__ == '__main__':
    # Code from problem 1
    raw_data_file = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')
    raw_df = create_dataframe(raw_data_file)
    # Run the code for problem 2
    print_df_information(raw_df)
