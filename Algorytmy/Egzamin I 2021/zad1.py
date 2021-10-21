from zad1testy import runtests
from math import fabs
T = [0, 2, 1.1, 2]


def Partition(A, low, high):
    i = (low-1)
    pivot = A[high]

    for j in range(low, high):
        if A[j][0] < pivot[0] or (A[j][0] == pivot[0] and A[j][1] < pivot[1]):
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[high] = A[high], A[i+1]
    return (i+1)


def QuickSort(A,low, high):
    if len(A) == 1:
        return A
    if low < high:
        p = Partition(A, low, high)
        QuickSort(A, low, p-1)
        QuickSort(A, p+1, high)
    return A

def chaos_index(T):
    n = len(T)
    A = [0]*n

    for i in range(n):
        A[i] = (T[i], i)
    A = QuickSort(A, 0, n-1)
    k = 0
    for i in range(n):
        if int(fabs(A[i][1] - i)) > k:
            k = int(fabs(A[i][1] - i))
    print(A)
    return k

#print(chaos_index(T))
runtests(chaos_index)