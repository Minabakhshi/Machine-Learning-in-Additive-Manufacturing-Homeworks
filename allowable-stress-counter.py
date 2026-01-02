#S4-Q3

forces = [100, 200, 300, 60, 70, 400, 450, 600]
distances = [20, 30, 40, 50, 70, 80, 20, 30]

max_allowable_stress = 7

count = 0

for i in range(len(forces)):
    stress = forces[i] / distances[i]
    if stress < max_allowable_stress:
        count += 1

print(count)