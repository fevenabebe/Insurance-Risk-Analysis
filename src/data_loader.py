import pandas as pd


def load_data(filepath):
    df= "../data/ML.txt",

    df = pd.read_csv(
        filepath,
        sep='|',
        parse_dates=['TransactionMonth'],
        low_memory=False
    )

    return df