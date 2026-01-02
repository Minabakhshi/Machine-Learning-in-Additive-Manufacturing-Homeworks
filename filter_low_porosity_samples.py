#S4-Q10

def low_porosity_samples(masses, volumes):
    low_porosity_list = []

    for i in range(len(masses)):
        density = masses[i] / volumes[i]
        porosity = (1 - density) * 100

        if porosity < 5:
            low_porosity_list.append(round(porosity, 3))

    return low_porosity_list


# example usage
masses = [9.7, 9.9, 8.5, 9.95]
volumes = [10, 10, 10, 10]

result = low_porosity_samples(masses, volumes)
print(result)
