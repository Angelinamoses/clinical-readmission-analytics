"""
Tests for data_utils.py
"""

import pandas as pd
import numpy as np

from src.data_utils import (
    dataset_summary,
    get_missing_summary,
    create_binary_readmission,
    count_duplicates,
    find_low_variance,
    readmission_distribution
)

# dataset summary

def test_dataset_summary_returns_dataframe():

    df = pd.DataFrame({
        "A": [1, 2, 3],
        "B": ["x", "y", "z"]
    })

    result = dataset_summary(df)

    assert isinstance(      #assert means this must be true
        result,
        pd.DataFrame
    )

# missing summary

def test_missing_summary_detects_missing_values():

    df = pd.DataFrame({
        "A": [1, None, 3],
        "B": [1, 2, 3]
    })

    result = get_missing_summary(df)

    assert result.loc[
        "A",
        "Missing Count"
    ] == 1


# binary readmission

def test_create_binary_readmission():

    df = pd.DataFrame({
        "readmitted": [
            "NO",
            "<30",
            ">30"
        ]
    })

    result = create_binary_readmission(df)

    expected = [
        "Not Readmitted",
        "Readmitted",
        "Readmitted"
    ]

    assert (
        result["readmitted_binary"]
        .tolist()
        == expected
    )

# Duplicate count

def test_count_duplicates():

    df = pd.DataFrame({
        "A": [1, 1],
        "B": [2, 2]
    })

    result = count_duplicates(df)

    assert result == 1

# low variance columns

def test_find_low_variance_columns():
    
    df = pd.DataFrame({
        "constant": [1, 1, 1],
        "variable": [1, 2, 3]
    })

    result = find_low_variance(df)

    assert "constant" in result.index

# readmission distribution

def test_readmission_distribution():

    df = pd.DataFrame({
        "readmitted": [
            "NO",
            "NO",
            "<30"
        ]
    })

    result = readmission_distribution(df)

    assert result.loc[
        "NO",
        "Count"
    ] == 2
