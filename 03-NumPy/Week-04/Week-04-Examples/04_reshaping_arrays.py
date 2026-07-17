"""
Week 04 - NumPy Fundamentals

Topic:
Reshaping Arrays

Topics Covered
--------------
- reshape()
- flatten()
- transpose()

Author: Summer 2026 AI & ML Batch
"""

import numpy as np

print("\n========== Example 1 : Daily Voltage Readings ==========")
voltage = np.array([220,221,222,223,224,225])
print("Original:")
print(voltage)

matrix = voltage.reshape(2,3)
print("\nReshaped (2 x 3):")
print(matrix)

print("\n========== Example 2 : Sensor Matrix ==========")
sensor_data = np.arange(1,13)
print("Original:")
print(sensor_data)

sensor_matrix = sensor_data.reshape(3,4)
print("\nSensor Matrix:")
print(sensor_matrix)

print("\n========== Example 3 : Solar Generation Matrix ==========")
solar = np.array([
    2.1,3.4,5.6,
    6.2,5.8,4.9
])

solar_matrix = solar.reshape(2,3)
print(solar_matrix)

print("\nTranspose:")
print(solar_matrix.T)

print("\n========== Example 4 : Building Energy Consumption ==========")
energy = np.arange(100,112)
energy_matrix = energy.reshape(4,3)

print("Energy Matrix:")
print(energy_matrix)

print("\nFlatten Matrix:")
print(energy_matrix.flatten())

print("\n========== Example 5 : CityLearn Observation Matrix ==========")

observations = np.array([
    8,0.42,22.5,
    9,0.48,21.8,
    10,0.53,20.9,
    11,0.60,19.7
])

obs_matrix = observations.reshape(4,3)

print("Observation Matrix:")
print(obs_matrix)

print("\nHours:")
print(obs_matrix[:,0])

print("\nCarbon Intensity:")
print(obs_matrix[:,1])

print("\nElectricity Price:")
print(obs_matrix[:,2])

print("\n================ Summary ================")
print("reshape()  -> Change array dimensions")
print("flatten()  -> Convert multi-dimensional array into 1D")
print("transpose()-> Swap rows and columns")

"""
Best Practices
--------------
* Ensure total number of elements remains the same.
* Use reshape() for organizing engineering datasets.
* Use transpose() when rows and columns need to be exchanged.
* Use flatten() before exporting or processing one-dimensional data.
"""
