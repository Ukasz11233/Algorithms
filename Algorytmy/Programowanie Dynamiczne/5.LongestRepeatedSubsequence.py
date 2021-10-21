def LRS(A, L, i, j):
    if i == 0 or j == 0:
        return 0
    if L[i-1][j-1] > 0:
        return L[i-1][j-1]
    if i != j and A[i-1] == A[j-1]:
        L[i-1][j-1] = LRS(A, L, i-1, j-1) + 1
    else:
        q = max(LRS(A, L, i - 1, j), LRS(A, L, i, j - 1))
        L[i-1][j-1] = q
    return L[i-1][j-1]

def printLPS(A, L, i, j):
    if i == 0 or j == 0:
        return ""
    if A[i-1] == A[j-1] and i != j:
        return printLPS(A, L, i-1, j-1) + A[i-1]
    else:
        if L[i-1][j] > L[i][j-1]:
            return printLPS(A, L, i-1, j)
        else:
            return printLPS(A, L, i, j-1)

if __name__ == "__main__":
    A = "ATACTCGGA"
    L = [[0 for i in range(len(A)+1)]for i in range(len(A)+1)]
    print(LRS(A, L, len(A), len(A)))
    print(printLPS(A, L, len(A), len(A)))