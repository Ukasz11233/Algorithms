def TLD(A, B, L, i, j):
    if i == 0:
        return j
    if j == 0:
        return i
    if L[i-1][j-1] < float("inf"):
        return L[i-1][j-1]
    else:
        if A[i - 1] == B[j - 1]:
            L[i-1][j-1] = TLD(A, B, L, i - 1, j - 1)
        else:
            L[i-1][j-1] = min(TLD(A, B, L, i - 1, j) + 1, TLD(A, B, L, i, j - 1) + 1, TLD(A, B, L, i-1, j-1) + 1)
    return L[i-1][j-1]
if __name__ == "__main__":
    A = "kitten"
    B = "sitting"
    L = [[float("inf") for _ in range(len(A)+1)] for _ in range(len(B)+1)]
    print(TLD(A, B, L, len(A), len(B)))