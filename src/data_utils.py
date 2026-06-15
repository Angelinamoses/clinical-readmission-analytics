import pandas as pd
import numpy as np

# function 1
def get_missing_summary(df):
    """
    Generate missing value summary.
    """

    summary = pd.DataFrame({
        "Missing Count": df.isnull().sum(),
        "Missing Percent":
        (df.isnull().mean() * 100).round(2)
    })

    return(
        summary
        .sort_values(
            by="Miaaing Percent",
            ascending=False
        )
    )

# function 2
def dataset_summary(df):
    """
    Generate dataset overview.
    """

    return pd.DataFrame({
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


# function 3
def create_binary_readmission(df):
    """
    Create binary readmission outcome.
    """

    df = df.copy()

    df["readmitted_binary"] = np.where(
        df["readmitted"] == "NO",
        "Not readmitted",
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