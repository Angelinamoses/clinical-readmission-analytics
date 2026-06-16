"""
Statistical utility functions.

Author: Angelina Moses
Project: Clinical Readmission Analytics
"""

import pandas as pd
import numpy as np
from scipy import stats

# Mann-Whitney U Tests Function

def perform_mann_whitney(
    df,
    group_col,
    value_col,
    group_1,
    group_2
):
    """
    Perform Mann-Whitney U test
    between two groups.

    Parameters
    ----------
    df : pandas.DataFrame

    group_col : str
        Grouping column

    value_col : str
        Numeric variable

    group_1 : str

    group_2 : str

    Returns
    -------
    dict
    """

    sample_1 = df[
        df[group_col] == group_1
    ][value_col]

    sample_2 = df[
        df[group_col] == group_2
    ][value_col]

    statistic, p_value = stats.mannwhitneyu(
        sample_1,
        sample_2,
        alternative="two-sided"
    )

    return {
        "Variable": value_col,
        "Statistic": statistic,
        "P-value": p_value
    }

# Chi-Square Test

def perform_chi_square(
    df,
    categorical_col,
    target_col
):
    """
    Perform Chi-Square test
    of independence.
    """

    table = pd.crosstab(
        df[categorical_col],
        df[target_col]
    )

    chi2, p_value, dof, expected = (
        stats.chi2_contingency(table)
    )

    return {
        "Variable": categorical_col,
        "Chi-Square": chi2,
        "P-value": p_value,
        "Degrees of Freedom": dof
    }

# Satistical Significance Helper

def is_significant(
    p_value,
    alpha=0.05
):
    """
    Determine statistical significance.
    """

    return p_value < alpha

# Effect Size (Cohen's d)
def calculate_cohens_d(
    sample_1,
    sample_2
):
    """
    Calculate Cohen's d effect size.
    """

    mean_diff = (
        np.mean(sample_1)
        - np.mean(sample_2)
    )

    pooled_std = np.sqrt(
        (
            np.var(sample_1, ddof=1)
            +
            np.var(sample_2, ddof=1)
        ) / 2
    )

    return mean_diff / pooled_std

# interpret Cohen's d

def interpret_effect_size(
    d
):
    """
    Interpret Cohen's d.
    """

    abs_d = abs(d)

    if abs_d < 0.2:
        return "Negligible"

    elif abs_d < 0.5:
        return "Small"

    elif abs_d < 0.8:
        return "Medium"

    else:
        return "Large"
    

# Statistical Summary Table

def create_results_table(
    results
):
    """
    Convert results list
    into DataFrame.
    """

    return pd.DataFrame(results)

# Readable P-Value Formatter

def format_p_value(
    p_value
):
    """
    Format p-value.
    """

    if p_value < 0.001:
        return "<0.001"

    return round(
        p_value,
        4
    )


