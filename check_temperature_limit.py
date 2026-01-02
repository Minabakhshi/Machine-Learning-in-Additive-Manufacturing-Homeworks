#S4-Q7

def is_temperature_safe(temperature):
    if temperature > 2000:
        return False
    else:
        return True


# example usage
print(is_temperature_safe(1800))  # True
print(is_temperature_safe(2500))  # False
