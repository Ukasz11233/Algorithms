A = [4, 5, 12, 23, 3, 11, 235, 93]

import random

def RandomizedPartition(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return Partition(A, p ,r)

def Partition(A, p, r):
    i = (p - 1)
    pivot = A[r]
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return (i + 1)


def RandomizedSelect(A, p, r, i):
    if p == r:
        return A[p]
    q = Partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return RandomizedSelect(A, p, q - 1, i)
    else:
        return RandomizedSelect(A, q+1, r, i-k)

#worst case O(n^2)
#expected is O(n)

print(RandomizedSelect(A, 0, len(A)-1, 1))