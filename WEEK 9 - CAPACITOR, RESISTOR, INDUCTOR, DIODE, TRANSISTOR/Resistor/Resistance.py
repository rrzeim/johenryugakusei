
def get_resistance_of_material(resistivity, length, area):
    resistance = resistivity * length / area
    return resistance

resistivity = 2.82e-8   # Aluminum
length = 2
area = 1e-6

result = get_resistance_of_material(resistivity, length, area)
print("Resistance =", result)



def get_resistance_by_ohms_law(voltage, current):
    resistance = voltage / current
    print("Resistance =" , resistance)
    return resistance

