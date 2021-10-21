A = [4, 3, 9, 5, 1]

def FindSum(A, x):
    n = len(A)
    L = [[0]*n for _ in range(n)]
    for i in range(n):
        L[i][i] = x - A[i]
    for i in range(1, n):
        for j in range(i):
            if L[i-1][j] >= A[i]:
                L[i][j] = L[i-1][j] - A[i]
            else:
                L[i][j] = L[i-1][j]


    for i in range(n):
        if L[n-1][i] == 0:
            return True

    return False


def PrintSolution(P, i, j):
    if i == 0 or j == 0:
        print(j, end=" ")
        return
    if j - P[i][j] > 0 and P[i-1][j - P[i][j]] > 0:
        PrintSolution(P, i-1, j-P[i][j])
        if P[i][j] > 0:
            print(P[i][j], end=" ")
    else:
        PrintSolution(P, i-1, j)


def FindSumBoolean(A, x):
    n = len(A)
    F =[[0]*(x+1) for _ in range(n)]
    P = [[0]*(x+1) for _ in range(n)]

    for i in range(n):
        if A[i] <= x:
            F[i][A[i]] = A[i]
    F[0][0] = 1

    for i in range(1, n):
        for j in range(0, x+1):
                if F[i-1][j] > 0:
                    F[i][j] = F[i-1][j]
                    if j+A[i] <= x:
                        P[i][j+A[i]] = A[i]
                        F[i][j+A[i]] = j + A[i]
    PrintSolution(P, i, j)
    print(P)
    return F[-1][-1]

print(FindSumBoolean(A, 15))