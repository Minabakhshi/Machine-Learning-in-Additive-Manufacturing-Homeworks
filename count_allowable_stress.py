#S4-Q5

def count_allowable_stress(forces, distances, allowable_stress):
    count = 0
    for i in range(len(forces)):
        stress = forces[i] / distances[i]
        if stress < allowable_stress:
            count += 1
    return count


# example usage
forces = [100, 200, 300, 60, 70, 400, 450, 600]
distances = [20, 30, 40, 50, 70, 80, 20, 30]

result = count_allowable_stress(forces, distances, 7)
print(result)