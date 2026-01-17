def get_inductor_value_of_material(relative_permeability, area, turns, length):
    mu_0 = 4 * 3.141592653589793 * 1e-7  # H/m, permeability of free space
    inductance = (mu_0 * relative_permeability * turns**2 * area) / length
    print(f"Inductor Value: {inductance} H")
    return inductance
