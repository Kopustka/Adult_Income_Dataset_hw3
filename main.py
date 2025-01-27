# Importing necessary functions and modules
from modules import load_data, create_entry_table  # Import functions for loading data and inserting into the database
from modules import connector, get_average_hours, get_count_social_stat  # Import functions for SQL queries
from modules import clean_data  # Import function for cleaning the data
from modules import (plot_education_distribution,
                     plot_pairplot,
                     plot_age_distribution,
                     plot_correlation_heatmap,
                     plot_gender_income_distribution,
                     plot_work_hours_distribution,
                     plot_education_marital_status_heatmap)  # Import visualization functions

# Database connection parameters (placeholders, to be replaced with actual values)
host = 'HOST'
user = "USER"  # Username for MySQL (replace with actual)
password = "PASSWORD"  # Password for MySQL (replace with actual)
database = "DATABASE"  # Database name (replace with actual)


# Main function that brings everything together
def main():
    # Step 1: Load the data from the provided file path
    file_path = "data/raw_data/adult.csv"  # Specify the file path for the dataset
    data = load_data(file_path)  # Load the dataset into a DataFrame

    # Step 2: Clean the data by removing rows with missing values
    data = clean_data(data)  # Clean the dataset by removing rows with missing data

    # Step 3: Insert cleaned data into the database
    create_entry_table(data, host, user, password, database)  # Insert the cleaned data into MySQL database

    # Step 4: Query some statistics using SQL functions (examples)
    education_level = "11th"  # Example education level for analysis
    social_stat = "Married-civ-spouse"  # Example marital status for analysis

    # Get the average number of hours worked per week for a specific education level
    average_hours = get_average_hours(education_level=education_level)
    # Get the count of people with a specific marital status
    count_social_stat = get_count_social_stat(social_stat=social_stat)

    # Print the results of the queries if they were successful
    if average_hours is not None:
        print(f"Среднее количество рабочих часов для {education_level}: {average_hours}")
    if count_social_stat is not None:
        print(f"Количество людей с семейным статусом {social_stat}: {count_social_stat}")
    else:
        print("Не удалось получить данные.")

    # Step 5: Generate various visualizations to understand the data better
    plot_age_distribution(data)  # Plot the age distribution by income category
    plot_education_distribution(data)  # Plot the education level distribution by income category
    plot_correlation_heatmap(data)  # Plot the correlation heatmap between numerical features
    plot_work_hours_distribution(data)  # Plot the work hours distribution by income category
    plot_gender_income_distribution(data)  # Plot the income distribution by gender
    plot_education_marital_status_heatmap(data)  # Plot the education vs marital status heatmap
    plot_pairplot(data)  # Plot pairwise relationships of selected features, colored by income


# Ensure the script runs only if executed directly (not imported as a module)
if __name__ == "__main__":
    main()  # Execute the main function
