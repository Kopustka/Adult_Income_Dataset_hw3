# Importing necessary libraries
import pandas as pd
import mysql.connector
from mysql.connector import Error

# SQL query to create the 'adult' table in MySQL if it doesn't exist
create_table_qwerty = '''
CREATE TABLE IF NOT EXISTS adult (
    age INT,  
    workclass VARCHAR(255),  
    fnlwgt INT,  
    education VARCHAR(255),  
    educational_num INT,  
    marital_status VARCHAR(255), 
    occupation VARCHAR(255),  
    relationship VARCHAR(255), 
    race VARCHAR(255), 
    gender VARCHAR(10), 
    capital_gain INT,  
    hours_per_week INT,  
    native_country VARCHAR(255), 
    income VARCHAR(10) 
);
'''


# Function to load data from a CSV file
def load_data(file_path):
    """
    Loads data from a CSV file and returns it as a pandas DataFrame.

    Parameters:
    - file_path (str): The path to the CSV file to load

    Returns:
    - DataFrame: The loaded data
    """
    data = pd.read_csv(file_path)  # Reads the CSV file into a DataFrame
    print(data.head())  # Display the first 5 rows of the data for verification
    return data  # Returns the loaded data


# Function to connect to MySQL, create a table, and insert data
def create_entry_table(df, host, user, password, database):
    """
    Connects to MySQL, creates a table if it doesn't exist, and inserts the data from a DataFrame.

    Parameters:
    - df (DataFrame): The DataFrame containing the data to be inserted
    - host (str): The host where the MySQL database is located
    - user (str): MySQL username
    - password (str): MySQL password
    - database (str): The database where the data will be stored
    """
    try:
        # Establishing a connection to the MySQL database
        connection = mysql.connector.connect(
            host=host,  # Host where MySQL server is running
            user=user,  # Username for MySQL connection
            password=password,  # Password for MySQL user
            database=database  # Name of the database to connect to
        )

        # Check if the connection is successful
        if connection.is_connected():
            print("Connection to MySQL established successfully!")

            # Create a cursor object to interact with MySQL
            cursor = connection.cursor()

            # Execute the SQL query to create the table if it doesn't exist
            cursor.execute(create_table_qwerty)
            print("Table 'adult' created successfully.")

        # Loop through the rows of the DataFrame and insert data into the MySQL table
        for _, row in df.iterrows():
            cursor.execute(
                """
                INSERT INTO adult (
                    age, workclass, fnlwgt, education, educational_num, marital_status, 
                    occupation, relationship, race, gender, capital_gain, 
                    capital_loss, hours_per_week, native_country, income
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                tuple(row)  # Insert each row as a tuple
            )
        print("Data imported successfully!")

    except Error as e:
        # Handle any exceptions that occur during the connection or query execution
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Closing the connection and cursor objects to ensure the resources are released
        if connection.is_connected():
            connection.commit()  # Commit any pending transaction
            cursor.close()  # Close the cursor
            connection.close()  # Close the connection
        print("Connection to MySQL closed.")
