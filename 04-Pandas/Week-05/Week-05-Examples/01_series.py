"""
============================================================
Week 05 - Pandas Fundamentals

Topic:
Pandas Series

Description
-----------
This file introduces the Pandas Series data structure using
practical Electrical Engineering and AI examples.

Topics Covered
--------------
- Creating Series
- Series from List
- Series from Dictionary
- Custom Index
- Accessing Elements
- Series Attributes

Author: Summer 2026 AI & ML Batch
============================================================
"""

import pandas as pd
import numpy as np

# ============================================================
# Example 1 - Voltage Measurements
# ============================================================

print("\n========== Example 1 : Voltage Measurements ==========")

voltage = pd.Series([220, 221, 223, 219, 222])

print(voltage)
print("Average Voltage:", voltage.mean())

# ============================================================
# Example 2 - Battery State of Charge
# ============================================================

print("\n========== Example 2 : Battery SoC ==========")

battery_soc = pd.Series(
    [95, 90, 88, 84],
    index=["08:00", "09:00", "10:00", "11:00"]
)

print(battery_soc)

print("09:00 SoC:", battery_soc["09:00"])

# ============================================================
# Example 3 - Solar Generation
# ============================================================

print("\n========== Example 3 : Solar Generation ==========")

solar = pd.Series(
    {
        "Monday": 4.2,
        "Tuesday": 5.1,
        "Wednesday": 4.8,
        "Thursday": 5.4
    }
)

print(solar)

# ============================================================
# Example 4 - Current Measurements (NumPy Array)
# ============================================================

print("\n========== Example 4 : Current Measurements ==========")

current = np.array([4.8, 5.1, 5.4, 5.0])

current_series = pd.Series(current)

print(current_series)

# ============================================================
# Example 5 - CityLearn Electricity Prices
# ============================================================

print("\n========== Example 5 : Electricity Prices ==========")

prices = pd.Series(
    [18.5, 19.2, 20.1, 22.3, 21.8],
    index=["Hour-1", "Hour-2", "Hour-3", "Hour-4", "Hour-5"]
)

print(prices)

print("\nSeries Index:")
print(prices.index)

print("\nSeries Values:")
print(prices.values)

print("\nSeries Data Type:")
print(prices.dtype)

print("\nSeries Shape:")
print(prices.shape)

print("\n================ Summary ================")
print("• A Series is a one-dimensional labeled array.")
print("• Each value has an index.")
print("• Series can be created from lists, dictionaries,")
print("  and NumPy arrays.")
print("• Series supports mathematical operations.")

"""
Best Practices
--------------
* Use meaningful index labels.
* Store one type of data in a Series.
* Prefer descriptive variable names.
* Series is ideal for one-dimensional engineering data.
"""
