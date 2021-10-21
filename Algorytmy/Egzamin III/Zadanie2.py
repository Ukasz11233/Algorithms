A = [(1,4),(0,5),(1,5),(2,6),(2,4)]
A2 = [(10,15),(8,14),(1,6),(3,10),(8,11),(6,15)]

from queue import PriorityQueue

def Tower(A):
    n = len(A)
    result = 0
    actual_max = 1
    for i in range(n):
        base = A[i]
        for j in range(i+1, n):
            if base[0] <= A[j][0] and base[1] >= A[j][1]:
                base = A[j]
                actual_max += 1

        if result < actual_max:
            result = actual_max
        actual_max = 1

    return result

print(Tower(A))