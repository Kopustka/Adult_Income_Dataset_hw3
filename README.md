# Adult Data Analysis and MySQL Integration

This project loads a dataset containing adult demographic information, processes the data, and interacts with a MySQL database. The dataset is imported, cleaned, and inserted into the MySQL database. SQL queries are executed to retrieve and analyze certain aspects of the dataset. Additionally, visualizations are created to gain insights into the data.

## Project Overview

1. **Data Loading**: The project begins by loading a CSV file containing adult demographic information into a pandas DataFrame.
2. **Data Cleaning**: The dataset is cleaned by removing any rows with missing values.
3. **MySQL Database Operations**:
   - A connection to a MySQL database is established.
   - A table (`adult`) is created in the database if it does not exist.
   - The cleaned data is inserted into the `adult` table.
4. **Data Analysis**:
   - SQL queries are executed to calculate average work hours and count the number of people in a specific marital status.
5. **Data Visualization**: Various visualizations are generated to explore the data, such as the distribution of age, education, work hours, and income.

## Requirements

Before running the project, make sure you have the following dependencies installed:

- Python 3.x
- MySQL server running
- Required Python libraries:
  - `pandas`
  - `mysql-connector-python`
  - `seaborn`
  - `matplotlib`

To install the required libraries, run:

```bash
pip install pandas mysql-connector-python seaborn matplotlib
