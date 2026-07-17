"""
Week 04 - NumPy Fundamentals

Topic:
NumPy Functions

Topics Covered
--------------
- sum()
- mean()
- max()
- min()
- std()
- sqrt()

Author: Summer 2026 AI & ML Batch
"""

import numpy as np

print("\n========== Example 1 : Daily Energy Consumption ==========")
energy = np.array([12.5, 13.8, 11.9, 14.2, 13.1])
print("Energy:", energy)
print("Total Energy:", np.sum(energy), "kWh")

print("\n========== Example 2 : Voltage Analysis ==========")
voltage = np.array([220, 222, 221, 223, 219])
print("Voltage:", voltage)
print("Average Voltage:", np.mean(voltage), "V")

print("\n========== Example 3 : Solar Generation ==========")
solar = np.array([2.5, 4.8, 6.2, 5.7, 3.9])
print("Solar:", solar)
print("Maximum Generation:", np.max(solar), "kWh")
print("Minimum Generation:", np.min(solar), "kWh")

print("\n========== Example 4 : Transformer Loading ==========")
loading = np.array([65, 72, 70, 68, 74])
print("Loading (%):", loading)
print("Standard Deviation:", np.std(loading))

print("\n========== Example 5 : Current Measurements ==========")
current = np.array([4, 9, 16, 25, 36])
print("Current Values:", current)
print("Square Root:", np.sqrt(current))

print("\n================ Summary ================")
print("sum()  -> Total of all elements")
print("mean() -> Average value")
print("max()  -> Largest value")
print("min()  -> Smallest value")
print("std()  -> Standard deviation")
print("sqrt() -> Square root")

"""
Best Practices
--------------
* Use sum() for total energy or power.
* Use mean() to analyze average sensor values.
* Use max() and min() to identify operating limits.
* Use std() to measure variation in data.
* Use sqrt() in engineering calculations when required.
"""
