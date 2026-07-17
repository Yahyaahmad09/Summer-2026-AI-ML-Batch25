"""
Week 04 - NumPy Fundamentals
Topic: Array Indexing and Slicing
"""

import numpy as np

print("\n=== Example 1: Voltage Readings ===")
voltage = np.array([220,221,223,219,225,224])
print("Array:", voltage)
print("First:", voltage[0])
print("Last:", voltage[-1])

print("\n=== Example 2: Solar Generation ===")
solar = np.array([0.0,1.5,3.2,5.1,6.4,4.8,2.3])
print("Morning:", solar[:3])
print("Afternoon:", solar[3:])

print("\n=== Example 3: Battery SoC ===")
soc = np.array([95,92,89,85,82,80])
print("Every second value:", soc[::2])
print("Reverse:", soc[::-1])

print("\n=== Example 4: Building Load Matrix ===")
load = np.array([[3.1,2.8,3.6],
                 [4.2,4.5,4.0],
                 [2.5,2.7,2.9]])
print(load)
print("First Row:", load[0])
print("Second Column:", load[:,1])
print("Bottom Right:", load[2,2])

print("\n=== Example 5: CityLearn Observation Matrix ===")
obs = np.array([[8,0.35,22.1],
                [9,0.40,21.8],
                [10,0.52,20.7],
                [11,0.61,19.9]])
print(obs)
print("Hours:", obs[:,0])
print("Carbon Intensity:", obs[:,1])
print("Prices:", obs[:,2])

print("\nSummary")
print("- Indexing retrieves one element.")
print("- Slicing retrieves multiple elements.")
print("- Use ':' to select rows or columns in 2D arrays.")
