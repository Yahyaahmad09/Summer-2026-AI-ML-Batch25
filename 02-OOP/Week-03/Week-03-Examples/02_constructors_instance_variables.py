"""
============================================================
Week 03 - Object-Oriented Programming (OOP)

Topic:
Constructors (__init__) and Instance Variables

Description
-----------
This file explains how constructors initialize objects and
how instance variables store data that belongs to individual
objects.

Topics Covered
--------------
✔ Constructors (__init__)
✔ Instance Variables
✔ Positional Arguments
✔ Keyword Arguments
✔ Accessing Object Attributes

Author: Summer 2026 AI & ML Batch
============================================================
"""

# ============================================================
# Example 1
# Solar Inverter
# ============================================================

print("\n========== Example 1 : Solar Inverter ==========\n")


class SolarInverter:
    """
    Represents a Solar Inverter.

    Each inverter object stores its own information.
    """

    def __init__(self, name, capacity_kw, efficiency):
        """
        Constructor

        Parameters
        ----------
        name : str
        capacity_kw : float
        efficiency : float
        """

        # Instance Variables
        self.name = name
        self.capacity_kw = capacity_kw
        self.efficiency = efficiency


# Positional Arguments
inverter1 = SolarInverter(
    "Huawei SUN2000",
    5,
    98.5
)

# Keyword Arguments
inverter2 = SolarInverter(
    efficiency=97.8,
    capacity_kw=10,
    name="Growatt MOD"
)

print("Inverter 1")
print("Name       :", inverter1.name)
print("Capacity   :", inverter1.capacity_kw, "kW")
print("Efficiency :", inverter1.efficiency, "%")

print()

print("Inverter 2")
print("Name       :", inverter2.name)
print("Capacity   :", inverter2.capacity_kw, "kW")
print("Efficiency :", inverter2.efficiency, "%")


# ============================================================
# Example 2
# Wind Turbine
# ============================================================

print("\n========== Example 2 : Wind Turbine ==========\n")


class WindTurbine:

    def __init__(self, turbine_id, height, rated_power):

        self.turbine_id = turbine_id
        self.height = height
        self.rated_power = rated_power


turbine = WindTurbine(
    "WT-05",
    80,
    2500
)

print("Turbine ID :", turbine.turbine_id)
print("Height     :", turbine.height, "m")
print("Power      :", turbine.rated_power, "kW")


# ============================================================
# Example 3
# Electric Vehicle
# ============================================================

print("\n========== Example 3 : Electric Vehicle ==========\n")


class ElectricVehicle:

    def __init__(
            self,
            model,
            battery_capacity,
            driving_range,
            charging_time):

        self.model = model
        self.battery_capacity = battery_capacity
        self.driving_range = driving_range
        self.charging_time = charging_time


ev = ElectricVehicle(

    model="Tesla Model 3",
    battery_capacity=75,
    driving_range=520,
    charging_time=8

)

print("Model          :", ev.model)
print("Battery        :", ev.battery_capacity, "kWh")
print("Range          :", ev.driving_range, "km")
print("Charging Time  :", ev.charging_time, "hours")


# ============================================================
# Example 4
# Smart Building (CityLearn Inspired)
# ============================================================

print("\n========== Example 4 : Smart Building ==========\n")


class SmartBuilding:
    """
    Simplified Building similar to CityLearn.
    """

    def __init__(

            self,
            building_name,
            solar_generation,
            electricity_price,
            battery_soc

    ):

        self.building_name = building_name
        self.solar_generation = solar_generation
        self.electricity_price = electricity_price
        self.battery_soc = battery_soc


building = SmartBuilding(

    building_name="Residential Building",
    solar_generation=22.4,
    electricity_price=24.5,
    battery_soc=83

)

print("Building          :", building.building_name)
print("Solar Generation  :", building.solar_generation, "kWh")
print("Electricity Price :", building.electricity_price, "PKR/kWh")
print("Battery SoC       :", building.battery_soc, "%")


# ============================================================
# Example 5
# Weather Sensor Node
# ============================================================

print("\n========== Example 5 : Weather Sensor ==========\n")


class WeatherSensor:

    def __init__(

            self,
            sensor_id,
            temperature,
            humidity,
            wind_speed

    ):

        self.sensor_id = sensor_id
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed


sensor = WeatherSensor(

    "WS-101",
    34.5,
    56,
    11.8

)

print("Sensor ID   :", sensor.sensor_id)
print("Temperature :", sensor.temperature, "°C")
print("Humidity    :", sensor.humidity, "%")
print("Wind Speed  :", sensor.wind_speed, "km/h")


# ============================================================
# Key Notes
# ============================================================

print("\n==================================================")
print("Key Notes")
print("--------------------------------------------------")
print("1. __init__() is called automatically.")
print("2. Every object stores its own instance variables.")
print("3. Positional arguments depend on order.")
print("4. Keyword arguments improve readability.")
print("5. Different objects can store different values.")
print("==================================================")


# ============================================================
# Best Practices
# ============================================================

"""
✔ Use meaningful parameter names.

✔ Store only object-specific data as instance variables.

✔ Prefer keyword arguments when many parameters exist.

✔ Keep constructors focused on object initialization.

✔ Avoid putting complex calculations inside __init__().
"""