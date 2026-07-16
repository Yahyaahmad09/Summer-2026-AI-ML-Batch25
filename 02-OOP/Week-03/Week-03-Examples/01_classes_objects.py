"""
============================================================
Week 03 - Object-Oriented Programming (OOP)

Topic:
Classes and Objects

Description
-----------
This file introduces the basic concepts of Object-Oriented
Programming using practical Electrical Engineering examples.

Topics Covered
--------------
✔ Creating Classes
✔ Creating Objects
✔ Accessing Object Attributes
✔ Positional Arguments
✔ Keyword Arguments

Author: Summer 2026 AI & ML Batch
============================================================
"""

# ============================================================
# Example 1
# Smart Energy Meter
# ============================================================

print("\n========== Example 1 : Smart Energy Meter ==========\n")


# ------------------------------------------------------------
# Step 1:
# Create a class.
#
# A class is a blueprint that describes what information
# every Smart Meter object should store.
# ------------------------------------------------------------

class SmartMeter:

    # --------------------------------------------------------
    # Constructor (__init__)
    #
    # The constructor runs automatically whenever a new
    # object is created.
    #
    # The values passed during object creation are received
    # as parameters.
    # --------------------------------------------------------

    def __init__(self, meter_id, location, energy):

        # Instance Variables
        # Every object stores its own copy of these variables.

        self.meter_id = meter_id
        self.location = location
        self.energy = energy


# ------------------------------------------------------------
# Creating Objects using Positional Arguments
#
# Order matters.
#
# meter_id
# location
# energy
# ------------------------------------------------------------

meter1 = SmartMeter(
    "SM-101",
    "Building A",
    245.6
)


# ------------------------------------------------------------
# Creating Objects using Keyword Arguments
#
# Order does NOT matter.
# The parameter names are explicitly written.
# ------------------------------------------------------------

meter2 = SmartMeter(
    location="Building B",
    energy=198.4,
    meter_id="SM-102"
)


# ------------------------------------------------------------
# Accessing Object Attributes
# ------------------------------------------------------------

print("Meter 1")
print("Meter ID :", meter1.meter_id)
print("Location :", meter1.location)
print("Energy   :", meter1.energy, "kWh")

print()

print("Meter 2")
print("Meter ID :", meter2.meter_id)
print("Location :", meter2.location)
print("Energy   :", meter2.energy, "kWh")