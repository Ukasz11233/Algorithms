A = [(2, 5), (5, 7), (0, 4), (3, 6), (7, 8), (8, 10), (10, 11)]


def PrintSolution(F, A, Prev, i, j):
    if i >= 1:
        PrintSolution(F, A, Prev, i-1, Prev[i][j])
        print(j, end=" ")
    if i == 0:
        print(j, end=" ")
        return

def FindMine(A, K):
    A.sort(key=lambda x:x[0])
    n = len(A)
    F = [[float("inf")]*n for _ in range(K)]
    Prev = [[0]*n for _ in range(K)]
    for i in range(n):
        F[0][i] = A[i][1] - A[i][0]

    for i in range(1, K):
        for j in range(n):
            for k in range(j+1, n, 1):
                if A[k][0] >= A[j][1]:
                    if F[i][k] > F[i-1][j] + (A[k][1] - A[k][0]):
                        F[i][k] = F[i-1][j] + (A[k][1] - A[k][0])
                        Prev[i][k] = j
                    break

    min_ = float("inf")
    for i in range(n):
        if F[K-1][i] < min_:
            min_ = F[K-1][i]
            idx = i

    PrintSolution(F, A, Prev, K-1, idx)
    return F
print(sorted(A, key=lambda x:x[0]))
#print(FindMine(A, 3))