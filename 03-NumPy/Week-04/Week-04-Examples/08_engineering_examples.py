"""
Week 04 - NumPy Fundamentals

Topic:
Engineering Examples with NumPy

Description
-----------
This file combines multiple NumPy concepts using practical
Electrical Engineering and CityLearn-inspired scenarios.

Author: Summer 2026 AI & ML Batch
"""

import numpy as np

# ============================================================
# Example 1 - Smart Grid Energy Analysis
# ============================================================

print("\n========== Example 1 : Smart Grid Energy ==========")

generation = np.array([42, 45, 48, 50, 46])
load = np.array([40, 43, 44, 47, 45])

net_energy = generation - load

print("Generation :", generation)
print("Load       :", load)
print("Net Energy :", net_energy)
print("Average Net:", np.mean(net_energy))

# ============================================================
# Example 2 - Solar Farm Production
# ============================================================

print("\n========== Example 2 : Solar Farm ==========")

solar = np.array([
    [4.2,5.1,5.8],
    [4.8,5.4,6.0],
    [3.9,4.7,5.5]
])

print("Solar Matrix")
print(solar)

print("Daily Production:", np.sum(solar, axis=1))
print("Maximum Output:", np.max(solar))

# ============================================================
# Example 3 - Battery Monitoring
# ============================================================

print("\n========== Example 3 : Battery Monitoring ==========")

soc = np.array([95,92,89,87,84,82])

print("Battery SoC:", soc)

print("Average SoC:", np.mean(soc))
print("Lowest SoC :", np.min(soc))

# ============================================================
# Example 4 - Transformer Loading
# ============================================================

print("\n========== Example 4 : Transformer Loading ==========")

loading = np.array([65,68,72,74,70,69])

print("Loading (%) :", loading)
print("Maximum :", np.max(loading))
print("Standard Deviation :", np.std(loading))

# ============================================================
# Example 5 - CityLearn Observation Processing
# ============================================================

print("\n========== Example 5 : CityLearn ==========")

observations = np.array([
    [8,0.42,21.5],
    [9,0.48,20.8],
    [10,0.55,19.9],
    [11,0.61,18.7]
])

print("Observation Matrix")
print(observations)

hours = observations[:,0]
carbon = observations[:,1]
price = observations[:,2]

print("Hours:", hours)
print("Average Carbon:", np.mean(carbon))
print("Average Price:", np.mean(price))

print("\n================ Summary ================")
print("NumPy allows engineers to efficiently analyze")
print("large numerical datasets using vectorized")
print("operations and statistical functions.")

"""
Best Practices
--------------
* Store engineering data in NumPy arrays.
* Use vectorized operations instead of loops.
* Organize multidimensional datasets using matrices.
* Use aggregation functions for quick analysis.
* NumPy forms the foundation of Pandas, ML, and AI.
"""
