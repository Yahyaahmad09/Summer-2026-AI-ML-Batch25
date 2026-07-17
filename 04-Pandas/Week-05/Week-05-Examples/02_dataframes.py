"""
Week 05 - Pandas Fundamentals
Topic: DataFrames
"""
import pandas as pd

print("\n=== Example 1: Transformer Data ===")
transformers=pd.DataFrame({
"Transformer":["T1","T2","T3"],
"Rating_kVA":[100,200,500],
"Voltage_kV":[11,11,33]
})
print(transformers)

print("\n=== Example 2: Solar Panels ===")
solar=pd.DataFrame({
"Panel":["P1","P2","P3"],
"Power_W":[550,580,600],
"Efficiency":[21.2,22.0,22.4]
})
print(solar)

print("\n=== Example 3: Building Energy ===")
building=pd.DataFrame({
"Building":["A","B","C"],
"Load_kWh":[120,98,145],
"PV_kWh":[35,42,30]
})
print(building)

print("\n=== Example 4: CityLearn Observation ===")
obs=pd.DataFrame({
"Hour":[8,9,10],
"Carbon":[0.42,0.51,0.60],
"Price":[21.5,20.8,19.9]
})
print(obs)

print("\n=== Example 5: DataFrame Attributes ===")
print("Columns:",obs.columns.tolist())
print("Shape:",obs.shape)
print("Data Types:")
print(obs.dtypes)
print("\nSummary: DataFrame is a 2D labeled table.")
