"""
============================================================
Week 03 - Object-Oriented Programming (OOP)

Topic:
Class Variables
Class Methods
Static Methods

Description
-----------
This file explains the difference between:

✔ Class Variables
✔ Class Methods
✔ Static Methods

using practical Electrical Engineering examples.

Author: Yahya Ahmad
============================================================
"""

# ============================================================
# Example 1
# Battery Bank
# ============================================================

print("\n========== Example 1 : Battery Bank ==========\n")


class BatteryBank:
    """
    Demonstrates Class Variables.
    """

    # --------------------------------------------------------
    # Class Variable
    # Shared by every BatteryBank object.
    # --------------------------------------------------------

    battery_type = "Lithium-Ion"

    def __init__(self, battery_id, voltage, capacity):

        self.battery_id = battery_id
        self.voltage = voltage
        self.capacity = capacity


battery1 = BatteryBank(
    "BAT-101",
    48,
    200
)

battery2 = BatteryBank(
    "BAT-102",
    24,
    150
)

print("Battery Type :", BatteryBank.battery_type)

print()

print("Battery 1")
print("ID       :", battery1.battery_id)
print("Voltage  :", battery1.voltage)
print("Capacity :", battery1.capacity)

print()

print("Battery 2")
print("ID       :", battery2.battery_id)
print("Voltage  :", battery2.voltage)
print("Capacity :", battery2.capacity)

# Change class variable

BatteryBank.battery_type = "Lead Acid"

print("\nUpdated Battery Type :", BatteryBank.battery_type)

print("Battery 1 Type :", battery1.battery_type)
print("Battery 2 Type :", battery2.battery_type)


# ============================================================
# Example 2
# Solar Company
# ============================================================

print("\n========== Example 2 : Solar Company ==========\n")


class SolarPanel:

    manufacturer = "Canadian Solar"

    def __init__(self, panel_name, power):

        self.panel_name = panel_name
        self.power = power

    # --------------------------------------------------------
    # Class Method
    #
    # Used for modifying class variables.
    # --------------------------------------------------------

    @classmethod
    def change_manufacturer(cls, new_name):

        cls.manufacturer = new_name


panel1 = SolarPanel(
    "Panel A",
    550
)

panel2 = SolarPanel(
    "Panel B",
    600
)

print("Manufacturer :", SolarPanel.manufacturer)

SolarPanel.change_manufacturer("LONGi Solar")

print("\nManufacturer Updated\n")

print(panel1.panel_name, "-", panel1.manufacturer)
print(panel2.panel_name, "-", panel2.manufacturer)


# ============================================================
# Example 3
# Distribution Transformer
# ============================================================

print("\n========== Example 3 : Distribution Transformer ==========\n")


class Transformer:

    frequency = 50

    def __init__(self, rating):

        self.rating = rating

    @classmethod
    def update_frequency(cls, value):

        cls.frequency = value


transformer1 = Transformer("100 kVA")
transformer2 = Transformer("200 kVA")

print("Initial Frequency :", Transformer.frequency, "Hz")

Transformer.update_frequency(60)

print("Updated Frequency :", Transformer.frequency, "Hz")

print(transformer1.rating)
print(transformer2.rating)


# ============================================================
# Example 4
# Smart Grid Safety
# ============================================================

print("\n========== Example 4 : Static Method ==========\n")


class SafetyGuide:

    @staticmethod
    def electrical_safety():

        print("Disconnect the power supply before maintenance.")

    @staticmethod
    def ppe():

        print("Always wear insulated gloves and safety shoes.")


SafetyGuide.electrical_safety()
SafetyGuide.ppe()


# ============================================================
# Example 5
# CityLearn Inspired Building
# ============================================================

print("\n========== Example 5 : CityLearn Building ==========\n")


class SmartBuilding:

    city = "Islamabad"

    def __init__(self,
                 building_name,
                 battery_soc):

        self.building_name = building_name
        self.battery_soc = battery_soc

    @classmethod
    def change_city(cls, new_city):

        cls.city = new_city

    @staticmethod
    def operating_hours():

        print("Building operates 24 hours a day.")


building1 = SmartBuilding(
    "Building A",
    85
)

building2 = SmartBuilding(
    "Building B",
    63
)

print("Current City :", SmartBuilding.city)

SmartBuilding.change_city("Peshawar")

print("\nAfter Updating City\n")

print(building1.building_name, "-", building1.city)
print(building2.building_name, "-", building2.city)

print()

SmartBuilding.operating_hours()


# ============================================================
# Summary
# ============================================================

print("\n====================================================")
print("Summary")
print("----------------------------------------------------")
print("✔ Class Variables belong to the class.")
print("✔ Every object shares the same Class Variable.")
print("✔ Class Methods modify Class Variables.")
print("✔ Static Methods don't access object or class data.")
print("✔ Static Methods are utility/helper functions.")
print("====================================================")


"""
============================================================
Best Practices

✔ Store common information as Class Variables.

✔ Use Class Methods to modify Class Variables.

✔ Use Static Methods for utility functions.

✔ Do not use Static Methods when object data is required.

✔ Prefer meaningful names for Class Variables.
============================================================
"""