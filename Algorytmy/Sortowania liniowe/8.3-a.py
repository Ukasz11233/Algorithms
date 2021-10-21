A = [4, 23, 6546, 523, 145] # n = 13
B = ["aaa", "aab", "bab", "b", "ac", "ab"]
from RadixSort import RadixSort, CountingSort

def SortingArray(A, n):
    B = []
    for i in range(n):
        B.append([])
    for i in range(len(A)):
        tmp = A[i]
        idx_b = 0
        while tmp > 0:
            tmp //= 10
            idx_b +=1
        B[idx_b].append(A[i])
    for i in range(len(B)):
        if len(B[i]) > 0:
            B[i] = RadixSort(B[i])

    k = 0
    for i in range(len(B)):
        for j in range(len(B[i])):
            A[k] = B[i][j]
            k += 1
    return A

print(SortingArray(A, 13))