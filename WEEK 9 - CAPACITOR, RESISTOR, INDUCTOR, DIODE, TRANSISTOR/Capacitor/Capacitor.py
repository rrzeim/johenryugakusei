def get_capacitance_by_material(permeability, area, distance):
    dielectric_constant = 8.854e-12  # Farads per meter (F/m), vacuum permittivity
    capacitance = (permeability * dielectric_constant * area) / distance
    print(f"Capacitance of material is: {capacitance} F")
    return capacitance

def get_capacitance_by_CV(charge, voltage):
    capacitance = charge / voltage
    print(f"Capacitance of material is: {capacitance} F")
    return capacitance

def get_capacitance_current(capacitance, dV_dt):
    ic = capacitance * dV_dt
    print(f"Capacitor current is: {ic} A")
    return ic






