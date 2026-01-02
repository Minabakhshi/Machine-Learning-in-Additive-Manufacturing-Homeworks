#S4-Q4

def check_stress(forces, distances, allowable_stress):
    for i in range(len(forces)):
        stress = forces[i] / distances[i]
        if stress < allowable_stress:
            print(f"Index {i}: stress = {round(stress, 3)}")


# example usage
forces = [100, 200, 300, 60, 70, 400, 450, 600]
distances = [20, 30, 40, 50, 70, 80, 20, 30]

check_stress(forces, distances, 7)