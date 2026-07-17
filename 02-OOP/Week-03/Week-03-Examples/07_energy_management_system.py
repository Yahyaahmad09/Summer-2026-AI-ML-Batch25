"""
============================================================
Week 03 - OOP Mini Example

Topic:
Energy Management System

Description
-----------
This example combines all Week 03 concepts into one
small application.

Topics Used
-----------
✔ Classes
✔ Objects
✔ Constructors
✔ Instance Variables
✔ Class Variables
✔ Class Methods
✔ Static Methods
✔ Inheritance
✔ __str__()
✔ @property
============================================================
"""

print("\n========== Energy Management System ==========\n")


# ============================================================
# Parent Class
# ============================================================

class EnergyDevice:

    manufacturer = "Open Energy"

    def __init__(self, device_name):

        self.device_name = device_name

    @classmethod
    def change_manufacturer(cls, name):

        cls.manufacturer = name

    @staticmethod
    def safety_message():

        print("Always disconnect power before maintenance.")

    def __str__(self):

        return f"{self.device_name}"


# ============================================================
# Battery
# ============================================================

class Battery(EnergyDevice):

    def __init__(self,
                 device_name,
                 soc):

        super().__init__(device_name)

        self._soc = soc

    @property
    def soc(self):

        return self._soc

    @soc.setter
    def soc(self, value):

        if 0 <= value <= 100:
            self._soc = value
        else:
            print("Invalid SoC")


# ============================================================
# Solar Panel
# ============================================================

class SolarPanel(EnergyDevice):

    def __init__(self,
                 device_name,
                 generation):

        super().__init__(device_name)

        self.generation = generation


# ============================================================
# Create Objects
# ============================================================

battery = Battery(
    "Battery Storage",
    82
)

panel = SolarPanel(
    "Solar PV",
    25.4
)

print(battery)
print(panel)

print()

print("Battery SoC :", battery.soc, "%")

battery.soc = 91

print("Updated SoC :", battery.soc, "%")

print()

print("Manufacturer :", EnergyDevice.manufacturer)

EnergyDevice.change_manufacturer(
    "GreenTech Energy"
)

print("Updated Manufacturer :", EnergyDevice.manufacturer)

print()

EnergyDevice.safety_message()

print()

print("Solar Generation :", panel.generation, "kWh")