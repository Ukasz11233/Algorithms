from math import sqrt
import random

A = []

class Point:
    def __init__(self):
        self.x = None
        self.y = None


def Initializing_list(A):
    A = [0]*10
    for i in range(10):
        x = (round(random.uniform(-0.7, 0.7), 2), round(random.uniform(-0.7, 0.7), 2))
        A[i] = x
    return A



def insertionSort(A):
    for i in range(len(A)):
        up = sqrt(A[i][0]**2 + A[i][1]**2)
        tmp = A[i]
        j = i - 1
        while j >= 0 and sqrt(A[j][0]**2 + A[j][1]**2) > up:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = tmp
    return A

def SortPointsInCircle(A):
    B = []
    for i in range(10):
        B.append([])
    for i in range(len(A)):
        idx_b = int(10*sqrt(A[i][0]**2+A[i][1]**2))
        B[idx_b].append(A[i])
    for i in range(len(B)):
        B[i] = insertionSort(B[i])
    k = 0
    for i in range(len(B)):
        for j in range(len(B[i])):
                A[k] = B[i][j]
                k += 1
    return A
A = Initializing_list(A)
print(SortPointsInCircle(A))