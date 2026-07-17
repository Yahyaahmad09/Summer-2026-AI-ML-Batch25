"""
============================================================
Week 03 - Object-Oriented Programming (OOP)

Topic:
Magic Methods

Description
-----------
Magic methods are special methods in Python that allow
objects to behave like built-in data types.

Topics Covered
--------------
✔ __str__()
✔ __repr__()

Author: Yahya Ahmad
============================================================
"""

# ============================================================
# Example 1
# Smart Energy Meter
# ============================================================

print("\n========== Example 1 : Smart Energy Meter ==========\n")


class SmartMeter:
    """
    Represents a Smart Energy Meter.
    """

    def __init__(self,
                 meter_id,
                 location,
                 energy):

        self.meter_id = meter_id
        self.location = location
        self.energy = energy

    # --------------------------------------------------------
    # __str__()
    #
    # Called automatically when print(object) is used.
    # It should return a user-friendly string.
    # --------------------------------------------------------

    def __str__(self):

        return (
            f"SmartMeter("
            f"ID={self.meter_id}, "
            f"Location={self.location}, "
            f"Energy={self.energy} kWh)"
        )


meter = SmartMeter(
    "SM-101",
    "Building A",
    256.8
)

print(meter)


# ============================================================
# Example 2
# Electric Vehicle
# ============================================================

print("\n========== Example 2 : Electric Vehicle ==========\n")


class ElectricVehicle:

    def __init__(self,
                 model,
                 battery,
                 range_km):

        self.model = model
        self.battery = battery
        self.range_km = range_km

    def __str__(self):

        return (
            f"EV(Model={self.model}, "
            f"Battery={self.battery} kWh, "
            f"Range={self.range_km} km)"
        )


vehicle = ElectricVehicle(
    "Tesla Model 3",
    75,
    520
)

print(vehicle)


# ============================================================
# Example 3
# Weather Station
# ============================================================

print("\n========== Example 3 : Weather Station ==========\n")


class WeatherStation:

    def __init__(self,
                 station_name,
                 temperature,
                 humidity):

        self.station_name = station_name
        self.temperature = temperature
        self.humidity = humidity

    def __str__(self):

        return (
            f"{self.station_name}"
            f"\nTemperature : {self.temperature} °C"
            f"\nHumidity    : {self.humidity}%"
        )


station = WeatherStation(
    "Station A",
    32.5,
    61
)

print(station)


# ============================================================
# Example 4
# CityLearn Building
# ============================================================

print("\n========== Example 4 : CityLearn Building ==========\n")


class Building:

    def __init__(self,
                 name,
                 solar_generation,
                 battery_soc):

        self.name = name
        self.solar_generation = solar_generation
        self.battery_soc = battery_soc

    def __str__(self):

        return (
            f"Building : {self.name}"
            f"\nSolar Generation : {self.solar_generation} kWh"
            f"\nBattery SoC      : {self.battery_soc}%"
        )


building = Building(
    "Residential Building",
    21.4,
    82
)

print(building)


# ============================================================
# Example 5
# Difference Between __str__() and __repr__()
# ============================================================

print("\n========== Example 5 : __repr__() ==========\n")


class SolarPanel:

    def __init__(self,
                 panel_name,
                 power):

        self.panel_name = panel_name
        self.power = power

    def __str__(self):

        return (
            f"{self.panel_name} ({self.power} W)"
        )

    # --------------------------------------------------------
    # __repr__()
    #
    # Mainly used by developers.
    # It should return an unambiguous representation.
    # --------------------------------------------------------

    def __repr__(self):

        return (
            f"SolarPanel("
            f"panel_name='{self.panel_name}', "
            f"power={self.power})"
        )


panel = SolarPanel(
    "LONGi LR5",
    580
)

print("Using print(object)")
print(panel)

print()

print("Using repr(object)")
print(repr(panel))


# ============================================================
# Summary
# ============================================================

print("\n====================================================")
print("Summary")
print("----------------------------------------------------")
print("✔ __str__() creates a readable object description.")
print("✔ print(object) automatically calls __str__().")
print("✔ __repr__() is mainly for developers.")
print("✔ Magic methods improve object readability.")
print("✔ They make custom objects behave like Python objects.")
print("====================================================")


"""
============================================================
Best Practices

✔ Always implement __str__() for user-friendly output.

✔ Keep __repr__() unambiguous.

✔ Do not print inside __str__().
   Always RETURN a string.

✔ __str__() should describe the object clearly.

✔ Magic methods make debugging much easier.
============================================================
"""