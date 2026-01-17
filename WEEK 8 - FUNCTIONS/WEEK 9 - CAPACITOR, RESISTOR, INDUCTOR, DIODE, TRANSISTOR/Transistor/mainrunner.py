'''
from Capacitor import Capacitor

print("Capacitance Calculator")

charge = float(input("Please enter charge (Coulombs): "))
voltage = float(input("Please enter voltage (Volts): "))

Capacitor.get_caacitance_by_CV(charge, voltage)

from Resistor import Resistance

print("Ohm's Law Calculator")

voltage = float(input("Please enter voltage (Volts): "))
current = float(input("Please enter current (Amps): "))

Resistance.get_resistance_by_ohms_law(voltage, current)

from Inductor.inductor import get_inductor_value_of_material

print("Inductance Calculator")

relative_permeability = float(input("Enter relative permeability (μr): "))
turns = int(input("Enter number of turns (N): "))
area = float(input("Enter cross-sectional area (m²): "))
length = float(input("Enter length of solenoid (m): "))

get_inductor_value_of_material(relative_permeability, area, turns, length)
'''

import NEWRUNNER
