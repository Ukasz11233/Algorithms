A = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21]

from math import floor

def insertionSort(A):
    for i in range(1, len(A)):
        up = A[i]
        j = i - 1
        while j >= 0 and A[j] > up:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = up
    return A


def BucketSort(A):
    B = []
    for i in range(10):
        B.append([])
    for i in range(len(A)):
        idx_b = int(10*A[i])
        B[idx_b].append(A[i])
    for i in range(len(B)):
        B[i] = insertionSort(B[i])

    k = 0
    for i in range(len(B)):
        for j in range(len(B[i])):
                A[k] = B[i][j]
                k += 1
    return A

print(BucketSort(A))