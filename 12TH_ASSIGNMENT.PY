import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("customer_churn.csv")

print("First 5 Records:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

if "TotalCharges" in df.columns:
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"], errors="coerce"
    )

numeric_columns = df.select_dtypes(include=np.number).columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

categorical_columns = df.select_dtypes(include="object").columns

for column in categorical_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].mode()[0])

print("\nNumber of duplicate records:",
      df.duplicated().sum())

df = df.drop_duplicates()

print("\nSummary Statistics:")
print(df.describe())

if "Churn" in df.columns:

    print("\nCustomer Churn Count:")
    print(df["Churn"].value_counts())

    print("\nCustomer Churn Percentage:")
    print(df["Churn"].value_counts(normalize=True) * 100)

if "MonthlyCharges" in df.columns:

    charges = df["MonthlyCharges"].to_numpy()

    print("\nMonthly Charges Analysis:")
    print("Mean     :", np.mean(charges))
    print("Median   :", np.median(charges))
    print("Minimum  :",