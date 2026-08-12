import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from config_paths import raw_data_path, clean_customer_path
from dataloader import load_data

def inspect_data(df):
    print("HEAD:")
    print(df.head())

    print("\nSHAPE:")
    print(df.shape)

    print("\nCOLUMNS:")
    print(df.columns)

    print("\nDATA TYPES:")
    print(df.dtypes)

    print("\nINFO:")
    df.info()

    print("\nMISSING VALUES:")
    print(df.isnull().sum())

    print("\nDUPLICATES:")
    print(df.duplicated().sum())

    print("\nDESCRIBE:")
    print(df.describe())


def clean_data(df):

    df = df.copy()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Clean column names
    df.columns = df.columns.str.strip()

    # Identify categorical and numerical columns
    cat_cols = df.select_dtypes(include="object").columns
    num_cols = df.select_dtypes(include=np.number).columns

    # Fill categorical missing values with mode
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Fill numerical missing values with median
    for col in num_cols:
        df[col] = df[col].fillna(df[col].median())

    # Strip whitespace from categorical values
    for col in cat_cols:
        df[col] = df[col].str.strip()

    return df

if __name__ == "__main__":

    df = load_data(raw_data_path)

    if df is not None:
        print("Before Cleaning:")
        inspect_data(df)

        df = clean_data(df)

        print("\nAfter Cleaning:")
        inspect_data(df)

        df.to_csv(clean_customer_path, index = False)
        print(f"cleaned data saved to: {clean_customer_path}")