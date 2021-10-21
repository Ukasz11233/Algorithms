A = [1, 3, 5, 4, 2, 8, 9, 10]


def LIS(A):
    L = [0]*len(A)
    L[0] = 1

    for i in range(1, len(A)):
        for j in range(i):
            if A[j] < A[i] and L[j] > L[i]:
                L[i] = L[j]
        L[i] += 1
    return L

print(LIS(A))
