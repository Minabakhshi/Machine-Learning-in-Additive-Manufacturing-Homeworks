#S4-Q1
# 1) Lists of forces and distances
forces = [100, 200, 300, 60, 70, 450, 400, 600]
distances = [20, 30, 40, 50, 70, 80, 20, 30]
# 2) Maximum allowable stress
max_allowable_stress = 7
# 3) Iterate through the lists and check stress
for i in range(len(forces)):
    stress = forces[i] / distances[i]
    if stress < max_allowable_stress:
        print(f"Index {i}: force = {forces[i]}, distance = {distances[i]}, stress = {stress:.3f}")
