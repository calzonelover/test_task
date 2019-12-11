import pandas as pd

def read_data():
    df = pd.read_csv("583201.csv", index_col=False, delimiter=r"\s+")
    df['YEAR'] = df.apply(lambda row: int(str(row.DATE)[0:4]), axis=1)
    df['DAY'] = df.apply(lambda row: int(str(row.DATE)[4:7]), axis=1)
    return df