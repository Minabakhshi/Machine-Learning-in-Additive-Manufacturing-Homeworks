#S4-Q2

forces = [100, 200, 300, 60, 70, 400, 450, 600]
distances = [20, 30, 40, 50, 70, 80, 20, 30]

max_allowable_stress = 7

good_stresses = []

for i in range(len(forces)):
    stress = forces[i] / distances[i]
    if stress < max_allowable_stress:
        stress_rounded = round(stress, 3)
        good_stresses.append(stress_rounded)

print(good_stresses)
