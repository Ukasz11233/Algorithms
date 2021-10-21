A = [(30, 35), (35, 15), (15, 5), (5, 10), (10, 20), (20, 25)]

def MatrixChainOrder(A):
    n = len(A)
    print(n)
    M = [[float("inf") for i in range(n)] for i in range(n)]
    S = [[float("inf") for i in range(n)] for i in range(n)]
    for i in range(n):
        M[i][i] = 0
    for l in range(2, n+1):         #1..5
        for i in range(n - l + 1): #0..5
            j = i + l - 1
            for k in range(i, j): #1...
                q = M[i][k] + M[k+1][j] + A[i][0]*A[k][1]*A[j][1]
                if q < M[i][j]:
                    M[i][j] = q
                    S[i][j] = k
    return M, S[0][n-1]

print(MatrixChainOrder(A))