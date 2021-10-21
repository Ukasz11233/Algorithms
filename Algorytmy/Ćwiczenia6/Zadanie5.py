A = [[3, -2, 4, 9], [11, -5, -1, 3], [-2, 7, 3, 1], [-1, 4, 2, -5]]

def PrintResult(P, A, i, j):
    if i == 0 and j == 0:
        print(A[i][j], end=" ")
        return
    PrintResult(P, A, P[i][j][0], P[i][j][1])
    print(A[i][j], end=" ")

def Chessboard(A):
    n = len(A)
    F = [[0]*n for _ in range(n)]
    P = [[0]*n for _ in range(n)]

    F[0][0] = A[0][0]
    for i in range(1, n):
        F[0][i] = F[0][i-1] + A[0][i]
        F[i][0] = F[i-1][0] + A[i][0]
        P[i][0] = (i-1, 0)
        P[0][i] = (0, i-1)
    for i in range(1, n):
        for j in range(1, n):
            q = F[i-1][j] + A[i][j]
            P[i][j] = (i-1, j)
            if F[i][j-1] + A[i][j] < q:
                q = F[i][j-1] + A[i][j]
                P[i][j] = (i, j-1)
            F[i][j] = q

    PrintResult(P, A, i, j)
    print("")
    return F[-1][-1]



print(Chessboard(A))