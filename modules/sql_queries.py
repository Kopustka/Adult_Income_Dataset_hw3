import pandas as pd
import mysql.connector
from mysql.connector import Error


# Function to establish a database connection and wrap the target function
def connector(func):
    """
    This is a decorator function that ensures a database connection is established
    before executing the wrapped function and closes the connection afterwards.
    """

    def wrapper(*args, **kwargs):
        try:
            # Establish a connection to the MySQL database
            connection = mysql.connector.connect(
                host="127.0.0.1",  # MySQL server address (local machine)
                user="root",  # MySQL username
                password="Kostic200809",  # MySQL password
                database="adult_hw_test"  # Database to use
            )
            print("Connection to the database established.")

            # Call the actual function and pass the connection and other arguments
            result = func(connection, *args, **kwargs)
        except mysql.connector.Error as e:
            # Handle any errors that occur while connecting to the database
            print(f"Database connection error: {e}")
            result = None
        finally:
            # Close the connection if it is established
            if connection.is_connected():
                connection.close()
                print("Connection to the database closed.")
        return result

    return wrapper


# Function to get the average number of hours worked per week for a given education level
@connector
def get_average_hours(connection, education_level):
    """
    This function calculates the average number of hours worked per week for a specific education level
    from the 'adult' table in the MySQL database.
    It uses the `connector` decorator to handle the database connection.

    :param connection: The database connection passed by the decorator
    :param education_level: The education level to filter the query by
    :return: The average number of hours worked per week, or None if no data is found
    """
    # SQL query to calculate the average hours worked per week for a given education level
    query = """
        SELECT AVG(hours_per_week) AS average_hours
        FROM adult
        WHERE education = %s;
    """
    cursor = connection.cursor()  # Create a cursor to execute the query
    cursor.execute(query, (education_level,))  # Execute the query with the education level as a parameter
    result = cursor.fetchone()  # Fetch the first result (single row)
    cursor.close()  # Close the cursor
    return result[0] if result else None  # Return the average hours if found, else return None


# Function to count the number of people with a specific marital status
@connector
def get_count_social_stat(connection, social_stat):
    """
    This function counts the number of individuals with a specified marital status.
    It uses the `connector` decorator to manage the database connection.

    :param connection: The database connection passed by the decorator
    :param social_stat: The marital status to filter the query by (e.g., 'Married', 'Single', etc.)
    :return: The count of individuals with the specified marital status, or None if no data is found
    """
    # SQL query to count the number of people with a specific marital status
    query = """
        SELECT COUNT(*) AS married_count
        FROM adult
        WHERE marital_status = %s;
    """
    cursor = connection.cursor()  # Create a cursor to execute the query
    cursor.execute(query, (social_stat,))  # Execute the query with the marital status as a parameter
    result = cursor.fetchone()  # Fetch the first result (single row)
    cursor.close()  # Close the cursor
    return result[0] if result else None  # Return the count of people with the given marital status, else return None
