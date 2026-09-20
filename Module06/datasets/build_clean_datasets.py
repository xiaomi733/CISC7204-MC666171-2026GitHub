# -*- coding: utf-8 -*-
"""Replicate the data-wrangling steps of both Module06 notebooks
and save the cleaned datasets."""
import pandas as pd
import numpy as np

base = r'D:\CISC7204\cisc7204-Assgn01-2026-MC666171\Module06\datasets'

# ---------------- Final Project: King County house sales ----------------
df = pd.read_csv(base + r'\kc_house_data_NaN.csv')
df.drop(["id", "Unnamed: 0"], axis=1, inplace=True)

mean = df['bedrooms'].mean()
df['bedrooms'].replace(np.nan, mean, inplace=True)
mean = df['bathrooms'].mean()
df['bathrooms'].replace(np.nan, mean, inplace=True)

assert df['bedrooms'].isnull().sum() == 0, 'bedrooms still has NaN'
assert df['bathrooms'].isnull().sum() == 0, 'bathrooms still has NaN'
df.to_csv(base + r'\kc_house_data_clean.csv', index=False)
print('house_clean shape:', df.shape)
print('bedrooms NaN:', df['bedrooms'].isnull().sum(), '| bathrooms NaN:', df['bathrooms'].isnull().sum())

# ---------------- Practice Project: medical insurance ----------------
df2 = pd.read_csv(base + r'\medical_insurance_dataset.csv', header=None)
headers = ["age", "gender", "bmi", "no_of_children", "smoker", "region", "charges"]
df2.columns = headers
df2.replace('?', np.nan, inplace=True)

is_smoker = df2["smoker"].value_counts().idxmax()
df2["smoker"].replace(np.nan, is_smoker, inplace=True)

mean_age = df2["age"].astype("float").mean(axis=0)
df2["age"].replace(np.nan, mean_age, inplace=True)

df2[["age", "smoker"]] = df2[["age", "smoker"]].astype("int")
df2[["charges"]] = np.round(df2[["charges"]], 2)

assert df2.isnull().sum().sum() == 0, 'insurance still has NaN'
df2.to_csv(base + r'\medical_insurance_dataset_clean.csv', index=False)
print('insurance_clean shape:', df2.shape)
print('NaN total:', int(df2.isnull().sum().sum()))
print(df2.head())
