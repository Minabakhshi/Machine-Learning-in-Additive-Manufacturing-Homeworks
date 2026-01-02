#S4-Q9

def count_high_density_samples(masses, volumes):
    count = 0
    for i in range(len(masses)):
        density = masses[i] / volumes[i]
        if density > 0.9:
            count += 1
    return count


# example usage
masses = [9, 8, 10, 7]
volumes = [10, 10, 9, 10]

result = count_high_density_samples(masses, volumes)
print(result)
