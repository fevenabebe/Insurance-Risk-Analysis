import numpy as np


def calculate_loss_ratio(df):
    df["LossRatio"] = np.where(
        df["TotalPremium"] > 0,
        df["TotalClaims"] / df["TotalPremium"],
        0
    )

    return df


def calculate_margin(df):
    df["Margin"] = df["TotalPremium"] - df["TotalClaims"]

    return df
