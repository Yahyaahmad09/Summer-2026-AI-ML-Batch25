"""
============================================================
Week 04 - NumPy Fundamentals

Topic:
Array Attributes

Topics Covered
--------------
- ndim
- shape
- size
- dtype

Author: Summer 2026 AI & ML Batch
============================================================
"""

import numpy as np

print("\n========== Example 1 : Voltage Readings ==========")
voltage = np.array([220, 221, 223, 219, 222])
print("Array:", voltage)
print("Dimensions:", voltage.ndim)
print("Shape:", voltage.shape)
print("Size:", voltage.size)
print("Data Type:", voltage.dtype)

print("\n========== Example 2 : Solar Panel Ratings ==========")
solar = np.array([[550, 560, 580],
                  [540, 570, 590]])
print(solar)
print("Dimensions:", solar.ndim)
print("Shape:", solar.shape)
print("Size:", solar.size)
print("Data Type:", solar.dtype)

print("\n========== Example 3 : Transformer Ratings ==========")
transformers = np.array([100, 200, 500, 1000])
print(transformers)
print("Shape:", transformers.shape)

print("\n========== Example 4 : Building Energy Matrix ==========")
energy = np.array([[12.5, 13.2, 11.8],
                   [10.4, 14.1, 13.7],
                   [11.2, 12.8, 12.1]])
print(energy)
print("Dimensions:", energy.ndim)
print("Shape:", energy.shape)
print("Size:", energy.size)

print("\n========== Example 5 : CityLearn Observation ==========")
obs = np.array([[8, 0.42, 21.5],
                [9, 0.55, 20.9],
                [10, 0.68, 19.8]])
print(obs)
print("Data Type:", obs.dtype)

print("\n================ Summary ================")
print("ndim  -> Number of dimensions")
print("shape -> Rows and columns")
print("size  -> Total number of elements")
print("dtype -> Data type of elements")

"""
Best Practices
--------------
* Inspect array attributes before processing data.
* Use shape to verify dataset dimensions.
* Prefer numeric dtypes for engineering calculations.
"""
