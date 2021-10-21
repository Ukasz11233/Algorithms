def AuxTopDown(A, B, L, i, j):
    if L[i][j] > -1:
        return L[i][j], L
    if i == len(A) or j == len(B):
        return 0, L
    if A[i] == B[j]:
        q = AuxTopDown(A, B, L, i + 1, j + 1)[0] + 1
    else:
        q = max(AuxTopDown(A, B, L, i + 1, j)[0], AuxTopDown(A, B, L, i, j + 1)[0])
    L[i][j] = q
    return q, L

def DiffUtility(A, B, L, i, j):
    if i > 0 and j > 0 and A[i-1] == B[j-1]:
        DiffUtility(A, B, L, i-1, j-1)
        print("", A[i-1], end='')
    elif i > 0 and (j == 0 or L[i][j-1] < L[i-1][j]):
        DiffUtility(A, B, L, i-1, j)
        print(" -" + A[i-1], end='')
    elif j > 0 and (i == 0 or L[i][j-1] >= L[i-1][j]):
        DiffUtility(A, B, L, i, j-1)
        print(" +" + B[j-1], end='')

if __name__ == "__main__":
    A = "XMJYAUZ"
    B = "XMJAATZ"
    L = [[-1 for i in range (len(A)+1)] for i in range(len(A)+1)]
    for i in range(len(A)+1):
        L[i][len(B)] = 0
    for j in range(len(B)+1):
        L[len(A)][j] = 0
    print(AuxTopDown(A, B, L, 0, 0)[0])
    DiffUtility(A, B, L, len(A), len(B))

