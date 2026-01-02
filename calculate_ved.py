#S4-Q8

def calculate_ved(power, scan_speed, hatch_distance, layer_thickness):
    ved = power / (scan_speed * hatch_distance * layer_thickness)
    return round(ved, 3)


# example usage
ved_value = calculate_ved(200, 800, 0.1, 0.03)
print(ved_value)
