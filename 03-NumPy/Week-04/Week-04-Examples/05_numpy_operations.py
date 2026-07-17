"""
Week 04 - NumPy Fundamentals
Topic: NumPy Operations
"""

import numpy as np

print("\n=== Example 1: Voltage + Current Arrays ===")
v=np.array([220,225,230])
i=np.array([5,6,7])
print("Voltage:",v)
print("Current:",i)

print("\n=== Example 2: Power Calculation (P=V*I) ===")
p=v*i
print("Power (W):",p)

print("\n=== Example 3: Efficiency Improvement ===")
eff=np.array([90,91,92])
improved=eff+2
print("Old:",eff)
print("New:",improved)

print("\n=== Example 4: Temperature Conversion ===")
c=np.array([20,25,30,35])
f=(c*9/5)+32
print("C:",c)
print("F:",f)

print("\n=== Example 5: Building Energy Comparison ===")
b1=np.array([12.5,13.1,11.9])
b2=np.array([11.8,12.6,12.2])
print("Difference:",b1-b2)
print("Average:",(b1+b2)/2)

print("\nSummary")
print("+  Addition")
print("-  Subtraction")
print("*  Element-wise multiplication")
print("/  Division")
print("** Power")
