"""
Week 05 - Pandas Fundamentals
Topic: Selecting Data
"""
import pandas as pd

df=pd.read_csv("../../Datasets/Week-05/week05_power_consumption.csv")

print("\n=== Example 1: Select One Column ===")
print(df[df.columns[0]])

print("\n=== Example 2: Select Multiple Columns ===")
print(df[df.columns[:2]])

print("\n=== Example 3: Select First Three Rows ===")
print(df[:3])

print("\n=== Example 4: Select Rows 2 to 5 ===")
print(df.iloc[2:6])

print("\n=== Example 5: Engineering Example ===")
if len(df.columns)>=2:
    print(df[[df.columns[0],df.columns[1]]].head())

print("\nSummary")
print("Use column names, slicing and iloc to select data.")
