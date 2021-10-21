A = [3, 5, 2, 4, 6, 1, 7]
W = [0.1, 0.05, 0.1, 0.05, 0.2, 0.35, 0.15]

import math

def Partition(A, p, r):
    if p == r:
        return p
    i = (p - 1)
    pivot = A[r]

    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return (i + 1)

def WeightedMedian(A, W):
    pairs = []

    for i in range(len(A)):
        pairs.append([A[i], W[i]])

    q = Partition(W, 0, len(W)-1)
    l_sum = 0
    p = pairs[q][1]
    for i in range(q):
        l_sum += pairs[i][1]
    r_sum = 1 - l_sum - p

    if r_sum > 0.5:
        return WeightedMedian(A[q:], W[q:])
    elif l_sum > 0.5:
        return WeightedMedian(A[:q], W[:q])
    else:
        if l_sum + p <= 0.5:
            dif = float("inf")
            for i in range(q, len(pairs)):
                if math.fabs(p - pairs[i][1]) < dif:
                    dif = math.fabs(p - pairs[i][1])
                    q = i
            return pairs[q][1]
        elif r_sum + p <= 0.5:
            dif = float("-inf")
            for i in range(q):
                if math.fabs(p - pairs[i][1]) < dif:
                    dif = math.fabs(p - pairs[i][1])
                    q = i
            return pairs[q][1]

print(WeightedMedian(A, W))