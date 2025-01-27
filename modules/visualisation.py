import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Function to visualize age distribution by income categories
def plot_age_distribution(data):
    """
    This function visualizes the distribution of age for different income categories.

    :param data: The input dataset (DataFrame).
    """
    plt.figure(figsize=(10, 6))  # Set the figure size
    sns.histplot(data=data, x="age", hue="income", kde=True, multiple="stack",
                 bins=20)  # Histogram with KDE (Kernel Density Estimation)
    plt.title('Age Distribution by Income Category')  # Title of the plot
    plt.xlabel('Age')  # X-axis label
    plt.ylabel('Frequency')  # Y-axis label
    plt.show()  # Display the plot


# Function to visualize education level distribution by income categories
def plot_education_distribution(data):
    """
    This function visualizes the distribution of education levels for different income categories.

    :param data: The input dataset (DataFrame).
    """
    plt.figure(figsize=(10, 6))  # Set the figure size
    sns.countplot(data=data, x="education", hue="income", palette="Set2")  # Count plot with different hues for income
    plt.title('Education Level Comparison by Income Category')  # Title of the plot
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.xlabel('Education Level')  # X-axis label
    plt.ylabel('Count')  # Y-axis label
    plt.show()  # Display the plot


# Function to plot a heatmap of the correlation between numerical features
def plot_correlation_heatmap(data):
    """
    This function visualizes the correlation between numerical features in the dataset using a heatmap.

    :param data: The input dataset (DataFrame).
    """
    numeric_columns = ['age', 'fnlwgt', 'educational-num', 'hours-per-week']  # Columns to analyze
    correlation_matrix = data[numeric_columns].corr()  # Compute the correlation matrix

    plt.figure(figsize=(8, 6))  # Set the figure size
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')  # Plot the heatmap with correlation values
    plt.title('Correlation Between Numerical Features')  # Title of the plot
    plt.show()  # Display the plot


# Function to visualize the distribution of work hours by income categories
def plot_work_hours_distribution(data):
    """
    This function visualizes the distribution of work hours for different income categories.

    :param data: The input dataset (DataFrame).
    """
    plt.figure(figsize=(10, 6))  # Set the figure size
    sns.histplot(data=data, x="hours-per-week", hue="income", kde=True, bins=20)  # Histogram with KDE for work hours
    plt.title('Work Hours Distribution by Income Category')  # Title of the plot
    plt.xlabel('Hours Worked per Week')  # X-axis label
    plt.ylabel('Frequency')  # Y-axis label
    plt.show()  # Display the plot


# Function to visualize income distribution by gender
def plot_gender_income_distribution(data):
    """
    This function visualizes the distribution of income by gender.

    :param data: The input dataset (DataFrame).
    """
    plt.figure(figsize=(10, 6))  # Set the figure size
    sns.countplot(data=data, x="gender", hue="income", palette="Set1")  # Count plot for gender and income
    plt.title('Income Distribution by Gender')  # Title of the plot
    plt.xlabel('Gender')  # X-axis label
    plt.ylabel('Count')  # Y-axis label
    plt.show()  # Display the plot


# Function to create a pivot table heatmap showing education and marital status
def plot_education_marital_status_heatmap(data):
    """
    This function visualizes a heatmap based on the relationship between education and marital status.

    :param data: The input dataset (DataFrame).
    """
    # Create a pivot table aggregating counts based on education and marital status
    pivot_table = data.groupby(['education', 'marital-status']).size().reset_index(name='count')
    pivot_table = pivot_table.pivot(index='education', columns='marital-status', values='count')  # Reshape the table

    plt.figure(figsize=(12, 8))  # Set the figure size
    sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt=".2f", linewidths=.5)  # Plot heatmap with annotation
    plt.title('Pivot Table: Education and Marital Status')  # Title of the plot
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability
    plt.yticks(rotation=0)  # Rotate y-axis labels for better readability
    plt.show()  # Display the plot


# Function to create pair plots for selected numerical features with income as hue
def plot_pairplot(data):
    """
    This function visualizes pairwise relationships of selected numerical features, using income as the hue.

    :param data: The input dataset (DataFrame).
    """
    sns.pairplot(data, hue="income", vars=['age', 'educational-num', 'hours-per-week'],
                 palette="Set1")  # Pairplot for selected columns
    plt.title('Pairwise Plots: Numerical Features and Income')  # Title of the plot
    plt.show()  # Display the plot
