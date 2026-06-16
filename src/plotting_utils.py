"""
Visualization utility functions.

Author: Angelina Moses
Projects: Clinical Readmission Analytics
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Consistent plot styling

sns.set_theme(style="whitegrid")

# function 1

def plot_readmission_distribution(df):
    """
    Plot readmission category distribution.

    Parameters
    ----------
    df : pandas.DataFrame
    """

    plt.figure(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="readmitted"
    )

    plt.title(
        "Distribution of Readmission Outcomes",
        fontsize=14,
        fontweight="bold"
    )

    plt.xlabel("Readmission Status")
    plt.ylabel("Patient Count")

    plt.tight_layout()
    plt.show()


# function 2

def plot_missing_values(df):
    """
    Plot missing value percentages.
    """

    missing_percent = (
        df.isnull()
        .mean()
        .mul(100)
        .sort_values(ascending=False)
    )

    missing_percent = (
        missing_percent[missing_percent > 0]
    )

    plt.figure(figsize=(12, 6))

    sns.barplot(
        x=missing_percent.index,
        y=missing_percent.values
    )

    plt.title(
        "Missing Values by Feature (%)",
        fontsize=14,
        fontweight="bold"
    )

    plt.xticks(
        rotation=90
    )

    plt.xlabel("Features")
    plt.ylabel("Missing Percentage")

    plt.tight_layout()
    plt.show()

# function 3

def plot_time_in_hospital(df):
    """
    Compare hospital stay length
    across readmission groups.
    """

    plt.figure(figsize=(8, 5))

    sns.boxplot(
        data=df,
        x="readmitted",
        y="time_in_hospital"
    )

    plt.title(
        "Hospital Stay by Readmission Status",
        fontsize=14,
        fontweight="bold"
    )

    plt.xlabel("Readmission Status")
    plt.ylabel("Days in Hospital")

    plt.tight_layout()
    plt.show()

# function 4

def plot_medication_distribution(df):
    """
    Distribution of medication count.
    """

    plt.figure(figsize=(10, 5))

    sns.histplot(
        data=df,
        x="num_medications",
        bins=30
    )

    plt.title(
        "Distribution of Number of Medications",
        fontsize=14,
        fontweight="bold"
    )

    plt.xlabel("Number of Medications")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()
