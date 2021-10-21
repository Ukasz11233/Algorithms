A = [14, 23, 52, 11, 2, 65, 19, 56, 98, 15, 23]

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


def SumBetween(A, p, q, n):
    left = RandomizedSelect(A, 0, n - 1, p)
    right = RandomizedSelect(A, 0, n - 1, q)

    sum = left + right
    for el in A:
        if el > left and el < right:
           sum += el
    return sum


print(SumBetween(A, 2, 5, len(A)))
print(sorted(A))