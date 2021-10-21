import random
import math
from RandomizedSelect import RandomizedSelect, Partition
A = []

def FillRandom(A):
    A = [0]*10
    for i in range(10):
        x = (random.randint(-10, 10), random.randint(-10, 10))
        A[i] = x
    return A


def BestPlaceForPipe(A):
    A = FillRandom(A)
    B = [0]*len(A)
    for i in range(len(A)):
        x = math.sqrt(A[i][0]**2 + A[i][1]**2)
        B[i] = x
    for j in range(len(A)):
        if A[j][1] < 0:
            B[j] *= -1
    return RandomizedSelect(B, 0, len(B)-1, len(B) / 2)

print(BestPlaceForPipe(A))
