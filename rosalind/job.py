from copy import deepcopy


def job_maximum(inter, weights):
    original = deepcopy(weights)
    for i in range(len(inter[1:])):
        start = inter[i + 1][0]
        end = inter[i + 1][1]
        for j in range(len(inter[:i + 1])):
            j0 = inter[j][0]
            j1 = inter[j][1]
            if j1 <= start and j1 < end:
                weights[i + 1] = max(original[i + 1], original[i + 1] + weights[j])

    return max(weights)


intervals = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (7, 9)]
weights = [5, 6, 5, 4, 11, 2]
print(job_maximum(intervals, weights))
