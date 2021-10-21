A = "ABCB"
B = "BACB"

def LCS(A, B):
    n = len(A)
    m = len(B)
    L = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    PrintLCS(L, A, n, m)
    print("")
    return L[n][m]

def PrintLCS(L, A, i, j):
    if i <= 0 or j <= 0:
        return

    if L[i-1][j-1] < L[i][j]:
        PrintLCS(L, A, i-1, j-1)
        print(A[i-1], end=" ")
    elif L[i-1][j] > L[i][j]:
        PrintLCS(L, A, i-1, j)
    else:
        PrintLCS(L, A, i, j-1)


print(LCS(A, B))