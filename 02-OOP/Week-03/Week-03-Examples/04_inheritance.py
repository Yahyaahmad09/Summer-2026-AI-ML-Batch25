"""
============================================================
Week 03 - Object-Oriented Programming (OOP)

Topic:
Inheritance

Description
-----------
Inheritance allows a child class to inherit attributes
and methods from a parent class.

Topics Covered
--------------
✔ Parent Class
✔ Child Class
✔ Inheritance
✔ Method Inheritance
✔ isinstance()

Author: Summer 2026 AI & ML Batch
============================================================
"""

# ============================================================
# Example 1
# Sensor Monitoring System
# ============================================================

print("\n========== Example 1 : Sensor Monitoring System ==========\n")


# ------------------------------------------------------------
# Parent Class
# ------------------------------------------------------------

class Sensor:
    """
    Parent class for all sensors.
    """

    def __init__(self, sensor_id, location):

        self.sensor_id = sensor_id
        self.location = location

    def display_information(self):

        print("Sensor ID :", self.sensor_id)
        print("Location  :", self.location)


# ------------------------------------------------------------
# Child Class
# ------------------------------------------------------------

class TemperatureSensor(Sensor):

    def __init__(self,
                 sensor_id,
                 location,
                 temperature):

        # Call Parent Constructor
        super().__init__(sensor_id, location)

        # Child-specific variable
        self.temperature = temperature

    def display_temperature(self):

        print("Temperature :", self.temperature, "°C")


# ------------------------------------------------------------
# Creating Object
# ------------------------------------------------------------

sensor = TemperatureSensor(

    sensor_id="TS-101",
    location="Control Room",
    temperature=29.5

)

print("Parent Class Information")
sensor.display_information()

print()

print("Child Class Information")
sensor.display_temperature()

print()

print("Is sensor an object of Sensor?",
      isinstance(sensor, Sensor))


# ============================================================
# Example 2
# CityLearn Inspired Energy Devices
# ============================================================

print("\n========== Example 2 : CityLearn Energy Devices ==========\n")


# ------------------------------------------------------------
# Parent Class
# ------------------------------------------------------------

class EnergyDevice:

    def __init__(self,
                 device_name,
                 building):

        self.device_name = device_name
        self.building = building

    def show_device(self):

        print("Device   :", self.device_name)
        print("Building :", self.building)


# ------------------------------------------------------------
# Child Class
# ------------------------------------------------------------

class Battery(EnergyDevice):

    def __init__(self,
                 device_name,
                 building,
                 soc):

        # Reuse parent constructor
        super().__init__(device_name, building)

        self.state_of_charge = soc

    def battery_status(self):

        print("Battery SoC :", self.state_of_charge, "%")


# ------------------------------------------------------------
# Child Class
# ------------------------------------------------------------

class SolarPanel(EnergyDevice):

    def __init__(self,
                 device_name,
                 building,
                 generation):

        super().__init__(device_name, building)

        self.generation = generation

    def solar_status(self):

        print("Solar Generation :", self.generation, "kWh")


# ------------------------------------------------------------
# Creating Objects
# ------------------------------------------------------------

battery = Battery(

    device_name="Battery Storage",
    building="Building A",
    soc=82

)

panel = SolarPanel(

    device_name="PV Array",
    building="Building A",
    generation=24.6

)

print("Battery Object")
battery.show_device()
battery.battery_status()

print()

print("Solar Panel Object")
panel.show_device()
panel.solar_status()


# ============================================================
# Summary
# ============================================================

print("\n====================================================")
print("Summary")
print("----------------------------------------------------")
print("✔ A Parent Class contains common features.")
print("✔ A Child Class inherits from the Parent.")
print("✔ super() calls the Parent Constructor.")
print("✔ Child classes can have additional attributes.")
print("✔ Inheritance reduces duplicate code.")
print("====================================================")


"""
============================================================
Best Practices

✔ Put common attributes in the Parent Class.

✔ Put unique attributes in Child Classes.

✔ Use super() to initialize the Parent.

✔ Avoid duplicating code.

✔ Use inheritance only when an "is-a"
relationship exists.

Examples:
Battery IS-A EnergyDevice.
SolarPanel IS-A EnergyDevice.
============================================================
"""