"""Week 04 - NumPy Fundamentals: Creating NumPy Arrays"""
import numpy as np

print("Example 1")
voltage=np.array([220,222,221,219,223,224]);print(voltage)
print("Example 2")
solar_generation=np.array([0,1.8,3.6,5.4,6.2,5.8,4.0,2.1]);print(solar_generation)
print("Example 3")
battery_soc=np.array([90,88,84,80,77,74,79,85]);print(battery_soc)
print("Example 4")
building_load=np.array([[3.4,2.9,4.1],[5.6,4.8,5.2],[2.1,2.8,3.3]]);print(building_load)
print("Example 5")
print(np.zeros(5));print(np.ones(5));print(np.arange(210,231,5));print(np.linspace(0,10,6))
