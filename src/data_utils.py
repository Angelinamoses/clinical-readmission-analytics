"""
Utility functions for data loading,
data quality assessment,
and preprocessing.

Author: Angelina Moses
Project: Clinical Readmission Analytics
"""

import pandas as pd
import numpy as np

# function 1
def dataset_summary(df):
    """
    Generate a high-level dataset summary.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
        Summary statistics about dataset structure.
    """

    summary = pd.DataFrame({
        "Metric": [
            "Rows",
            "Columns",
            "Numeric Columns",
            "Categorical Columns"
        ],
        "Value": [
            df.shape[0],
            df.shape[1],
            len(
                df.select_dtypes(
                    include="number"
                ).columns
            ),
            len(
                df.select_dtypes(
                    include="object"
                ).columns
            )
        ]
    })

    return summary

# function 2
def get_missing_summary(df):
    """
    Generate missing value statistics.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
    """

    summary = pd.DataFrame({
        "Missing Count": df.isnull().sum(),
        "Missing Percent":
            (df.isnull().mean() * 100).round(2)
    })

    return (
        summary
        .sort_values(
            by="Missing Percent",
            ascending=False
        )
    )


# function 3
def create_binary_readmission(df):
    """
    Convert readmission outcome
    into a binary variable.
    """

    df = df.copy()

    df["readmitted_binary"] = np.where(
        df["readmitted"] == "NO",
        "Not Readmitted",
        "Readmitted"
    )

    return df
# function 4
def find_low_variance(df):
    """
    Identify columns with one
    unique value.
    """

    return (
        df.nunique()
        [df.nunique() <= 1]
    )

# function 5
def count_duplicates(df):
    """
    Count duplicate rows.
    """

    return df.duplicated().sum()

# function 6
def readmission_distribution(df):
    """
    Return readmission counts
    and percentages.
    """

    counts = df["readmitted"].value_counts()

    percentages = (
        df["readmitted"]
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
    )

    return pd.DataFrame({
        "Count": counts,
        "Percent": percentages
    })