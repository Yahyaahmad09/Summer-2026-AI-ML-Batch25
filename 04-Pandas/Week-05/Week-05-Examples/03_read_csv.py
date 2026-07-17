"""
============================================================
Week 05 - Pandas Fundamentals

Topic:
Reading CSV Files

Topics Covered
--------------
- pd.read_csv()
- head()
- tail()
- info()

Author: Summer 2026 AI & ML Batch
============================================================
"""

import pandas as pd

print("\n========== Example 1 : Student Scores ==========")

students = pd.read_csv("../../Datasets/Week-05/week05_student_scores.csv")

print(students.head())

print("\n========== Example 2 : Power Consumption ==========")

power = pd.read_csv("../../Datasets/Week-05/week05_power_consumption.csv")

print(power.head())

print("\n========== Example 3 : Electrical Load ==========")

load = pd.read_csv("../../Datasets/Week-05/week05_electrical_load.csv")

print(load.head())

print("\n========== Example 4 : Last Records ==========")

print(power.tail())

print("\n========== Example 5 : Dataset Information ==========")

print(load.info())

print("\n================ Summary ================")
print("read_csv() -> Read CSV files")
print("head()     -> First five rows")
print("tail()     -> Last five rows")
print("info()     -> Dataset summary")

"""
Best Practices
--------------
* Store datasets in a dedicated Datasets folder.
* Always inspect data using head() and info().
* Verify column names before analysis.
"""
