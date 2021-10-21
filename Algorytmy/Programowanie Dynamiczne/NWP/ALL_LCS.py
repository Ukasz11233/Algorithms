A = "ABCBDAB"
B = "BDCABA"

def PrintLCS(A, B, i, j, C):
    if i == 0 or j == 0:
        return [""]
    if A[i-1] == B[j-1]:
        lcs = PrintLCS(A, B, i-1, j-1, C)
        for i in range(len(lcs)):
            lcs[i] = lcs[i] + (A[i-1])
        return lcs
    if C[i-1][j] > C[i][j-1]:
        return PrintLCS(A, B, i-1, j, C)
    if C[i][j-1] > C[i-1][j]:
        return PrintLCS(A, B, i, j-1, C)
    top = PrintLCS(A, B, i-1, j, C)
    left = PrintLCS(A, B, i, j-1, C)

    return top + left

def LCS_Length(A, B):
    C = [[-1 for i in range(len(B)+1)]for j in range(len(A)+1)]
    for i in range(1, len(A)+1):
        C[i][0] = 0
    for j in range(len(B)+1):
        C[0][j] = 0
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                C[i][j] = C[i-1][j-1] + 1
            elif C[i-1][j] >= C[i][j-1]:
                C[i][j] = C[i-1][j]
            else:
                C[i][j] = C[i][j-1]

    return PrintLCS(A, B, len(A), len(B), C)

print(LCS_Length(A, B))