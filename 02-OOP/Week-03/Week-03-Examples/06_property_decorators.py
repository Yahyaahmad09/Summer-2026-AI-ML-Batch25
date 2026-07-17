"""
============================================================
Week 03 - Object-Oriented Programming (OOP)

Topic:
Property Decorators

Description
-----------
Property decorators provide a safe and Pythonic way to
access, update, and delete object attributes.

Topics Covered
--------------
✔ @property (Getter)
✔ @property.setter
✔ @property.deleter

Author: Yahya Ahmad
============================================================
"""

# ============================================================
# Example 1
# Battery State of Charge
# ============================================================

print("\n========== Example 1 : Battery State of Charge ==========\n")


class Battery:
    """
    Represents a rechargeable battery.
    """

    def __init__(self, battery_name, soc):

        self.battery_name = battery_name
        self._soc = soc

    # --------------------------------------------------------
    # Getter
    # --------------------------------------------------------

    @property
    def soc(self):
        """Return the current battery state of charge."""
        return self._soc

    # --------------------------------------------------------
    # Setter
    # --------------------------------------------------------

    @soc.setter
    def soc(self, value):

        if 0 <= value <= 100:
            self._soc = value
        else:
            print("Invalid State of Charge!")

    # --------------------------------------------------------
    # Deleter
    # --------------------------------------------------------

    @soc.deleter
    def soc(self):

        print("Battery State of Charge Deleted.")
        del self._soc


battery = Battery("Battery Pack", 85)

print("Battery :", battery.battery_name)
print("SoC     :", battery.soc, "%")

battery.soc = 95
print("Updated :", battery.soc, "%")

battery.soc = 150

del battery.soc


# ============================================================
# Example 2
# Electric Motor
# ============================================================

print("\n========== Example 2 : Electric Motor ==========\n")


class Motor:

    def __init__(self,
                 motor_name,
                 rated_power):

        self.motor_name = motor_name
        self._rated_power = rated_power

    @property
    def rated_power(self):

        return self._rated_power

    @rated_power.setter
    def rated_power(self, value):

        if value > 0:
            self._rated_power = value
        else:
            print("Power must be greater than zero.")

    @rated_power.deleter
    def rated_power(self):

        print("Rated Power Deleted.")
        del self._rated_power


motor = Motor("Induction Motor", 5.5)

print("Motor :", motor.motor_name)
print("Power :", motor.rated_power, "kW")

motor.rated_power = 7.5

print("Updated Power :", motor.rated_power, "kW")


# ============================================================
# Example 3
# Smart Building (CityLearn Inspired)
# ============================================================

print("\n========== Example 3 : Smart Building ==========\n")


class SmartBuilding:

    def __init__(self,
                 building_name,
                 electricity_price):

        self.building_name = building_name
        self._electricity_price = electricity_price

    @property
    def electricity_price(self):

        return self._electricity_price

    @electricity_price.setter
    def electricity_price(self, value):

        if value >= 0:
            self._electricity_price = value
        else:
            print("Electricity price cannot be negative.")

    @electricity_price.deleter
    def electricity_price(self):

        print("Electricity Price Deleted.")
        del self._electricity_price


building = SmartBuilding(
    "Residential Building",
    23.5
)

print("Building :", building.building_name)
print("Price    :", building.electricity_price)

building.electricity_price = 26.8

print("Updated Price :", building.electricity_price)


# ============================================================
# Example 4
# Solar Panel Efficiency
# ============================================================

print("\n========== Example 4 : Solar Panel ==========\n")


class SolarPanel:

    def __init__(self,
                 panel_name,
                 efficiency):

        self.panel_name = panel_name
        self._efficiency = efficiency

    @property
    def efficiency(self):

        return self._efficiency

    @efficiency.setter
    def efficiency(self, value):

        if 0 <= value <= 100:
            self._efficiency = value
        else:
            print("Efficiency must be between 0 and 100.")


panel = SolarPanel(
    "LONGi LR5",
    22.5
)

print("Efficiency :", panel.efficiency)

panel.efficiency = 23.8

print("Updated Efficiency :", panel.efficiency)


# ============================================================
# Example 5
# Weather Station
# ============================================================

print("\n========== Example 5 : Weather Station ==========\n")


class WeatherStation:

    def __init__(self,
                 station_name,
                 temperature):

        self.station_name = station_name
        self._temperature = temperature

    @property
    def temperature(self):

        return self._temperature

    @temperature.setter
    def temperature(self, value):

        if -50 <= value <= 60:
            self._temperature = value
        else:
            print("Temperature is outside the valid range.")


station = WeatherStation(
    "Station A",
    31
)

print("Temperature :", station.temperature)

station.temperature = 35

print("Updated Temperature :", station.temperature)


# ============================================================
# Summary
# ============================================================

print("\n====================================================")
print("Summary")
print("----------------------------------------------------")
print("✔ @property creates a Getter.")
print("✔ @property.setter updates data safely.")
print("✔ @property.deleter removes data.")
print("✔ Properties provide controlled access.")
print("✔ Validation keeps object data consistent.")
print("====================================================")


"""
============================================================
Best Practices

✔ Use @property instead of direct attribute access.

✔ Validate data inside setters.

✔ Store actual values using private attributes
   (e.g., _soc, _temperature).

✔ Only create deleters when deleting the attribute
   makes sense.

✔ Properties make code cleaner and safer.
============================================================
"""