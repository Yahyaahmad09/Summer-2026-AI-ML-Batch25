"""
Week 05 - Pandas Fundamentals
Topic: loc() and iloc()
"""
import pandas as pd

df=pd.read_csv("../../Datasets/Week-05/week05_power_consumption.csv")

print("\n=== Example 1: loc - First Row ===")
print(df.loc[0])

print("\n=== Example 2: loc - Multiple Rows ===")
print(df.loc[0:2])

print("\n=== Example 3: iloc - First Row ===")
print(df.iloc[0])

print("\n=== Example 4: iloc - Rows and Columns ===")
print(df.iloc[0:4,0:2])

print("\n=== Example 5: Select Specific Cell ===")
print(df.iloc[0,0])

print("\nSummary")
print("loc() uses labels/index names.")
print("iloc() uses integer positions.")
