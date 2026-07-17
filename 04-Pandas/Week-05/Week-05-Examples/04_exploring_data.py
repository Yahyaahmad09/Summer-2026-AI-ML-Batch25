"""
Week 05 - Pandas Fundamentals
Topic: Exploring Data
"""
import pandas as pd

df=pd.read_csv("../../Datasets/Week-05/week05_power_consumption.csv")

print("\n=== Example 1: First Five Rows ===")
print(df.head())

print("\n=== Example 2: Last Five Rows ===")
print(df.tail())

print("\n=== Example 3: Dataset Information ===")
print(df.info())

print("\n=== Example 4: Statistical Summary ===")
print(df.describe())

print("\n=== Example 5: Dataset Structure ===")
print("Shape:",df.shape)
print("Columns:",df.columns.tolist())
print("Data Types:")
print(df.dtypes)

print("\nSummary")
print("head(), tail(), info(), describe(), shape, columns and dtypes help understand a dataset before analysis.")
