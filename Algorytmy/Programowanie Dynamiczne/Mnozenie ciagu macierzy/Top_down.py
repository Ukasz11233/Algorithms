A = [30, 35, 15, 5, 10, 20, 25]

def NaiveMatrixChainOrder(A, i, j):  #naiwne rozwiazanie wykladnicze
    if i == j:
        return 0
    minimum = float("inf")
    for k in range(i, j):
        count = (NaiveMatrixChainOrder(A, i, k) + NaiveMatrixChainOrder(A, k+1, j) + A[i-1]*A[k]*A[j])
        if count < minimum:
            minimum = count
    return minimum

def RMatrixChainOrder(A):
    n = len(A)
    M = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        M[i][i] = 0
    return AuxMatrixChainOrder(A, M, 1, len(A)-1)


def AuxMatrixChainOrder(A, M, i, j):
    if M[i][j] > 0:
        return M[i][j], M
    if i == j:
        q = 0
    else:
        q = float("inf")
        for k in range(i, j):
            q =min(q, AuxMatrixChainOrder(A, M, i, k)[0] + AuxMatrixChainOrder(A, M, k+1, j)[0] + A[i-1]*A[k]*A[j])
    M[i][j] = q
    return q, M

print(RMatrixChainOrder(A))