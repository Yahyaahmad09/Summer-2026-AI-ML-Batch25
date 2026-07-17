"""
Week 04 - NumPy Fundamentals

Topic:
NumPy Random Module

Topics Covered
--------------
- random.seed()
- random.rand()
- random.randint()
- random.normal()
- random.choice()

Author: Summer 2026 AI & ML Batch
"""

import numpy as np

print("\n========== Example 1 : Random Solar Generation ==========")
np.random.seed(42)
solar = np.random.rand(5) * 6
print("Solar Generation (kWh):")
print(np.round(solar, 2))

print("\n========== Example 2 : Random Battery SoC ==========")
battery_soc = np.random.randint(20, 101, size=8)
print("Battery State of Charge (%):")
print(battery_soc)

print("\n========== Example 3 : Voltage Measurements with Noise ==========")
voltage = np.random.normal(loc=220, scale=2, size=10)
print("Voltage Samples:")
print(np.round(voltage, 2))

print("\n========== Example 4 : Weather Conditions ==========")
weather = np.array(["Sunny", "Cloudy", "Rainy"])
forecast = np.random.choice(weather, size=7)
print("Weekly Weather:")
print(forecast)

print("\n========== Example 5 : CityLearn Electricity Prices ==========")
prices = np.random.uniform(18, 30, size=6)
print("Electricity Prices (PKR/kWh):")
print(np.round(prices, 2))

print("\n================ Summary ================")
print("seed()    -> Reproducible random numbers")
print("rand()    -> Random decimal values")
print("randint() -> Random integers")
print("normal()  -> Normally distributed values")
print("choice()  -> Random selection from a list")

"""
Best Practices
--------------
* Use random.seed() for reproducible experiments.
* Use rand() for simulation data.
* Use randint() for discrete engineering values.
* Use normal() to model sensor noise.
* Use choice() for selecting random categories.
"""
