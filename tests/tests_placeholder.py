from src.data_loader import load_data
from src.eda import calculate_loss_ratio, calculate_margin
import pandas as pd


def test_loss_ratio():
    df = pd.DataFrame({
        "TotalPremium": [100, 200],
        "TotalClaims": [50, 300]
    })

    df = calculate_loss_ratio(df)

    assert "LossRatio" in df.columns
    assert df["LossRatio"].iloc[0] == 0.5


def test_margin():
    df = pd.DataFrame({
        "TotalPremium": [100, 200],
        "TotalClaims": [50, 300]
    })

    df = calculate_margin(df)

    assert "Margin" in df.columns
    assert df["Margin"].iloc[0] == 50