A = [10, 20, 30, 40, 50, 60, 70, 80, 90]


def PrintSolution(A, P, n, K):
    if K == 0:
        for i in range(n+1):
            print(A[i], end=" ")
        print("")
        return
    PrintSolution(A, P, P[n][K], K-1)
    for i in range(P[n][K]+1, n+1):
        print(A[i], end=" ")
    print("")


def PartitionDP(A, K):
    n = len(A)
    F = [[float("inf")]*(K+1) for _ in range(n)]
    P = [[None]*(K+1) for _ in range(n)]

    for i in range(K+1):
        F[0][i] = A[0]

    for i in range(1, n):
        F[i][0] = F[i-1][0] + A[i]

    for i in range(1, n):
        for k in range(1, K+1):
            for j in range(i):
                q = max(F[j][k-1], F[i][0] - F[j][0])
                if F[i][k] > q:
                    F[i][k] = q
                    P[i][k] = j

    print(P)
    PrintSolution(A, P, n-1, K)
    return F

print(PartitionDP(A, 2))