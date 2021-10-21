
def LPS(A, L, i, j):
    if i > j:
        return 0
    if i == j:
        return 1
    if L[i][j] > 0:
        return L[i][j]
    if i < j:
        if A[i] == A[j]:
            L[i][j] = LPS(A, L, i+1, j-1) + 2
        else:
            q =  max(LPS(A, L, i+1, j), LPS(A, L, i, j-1))
            L[i][j] = q
    return L[i][j]

def PrintLPS(A, B, L, i, j):
    if i == 0 or j == 0:
        return ""
    if A[i] == B[j]:
        return PrintLPS(A, B, L, i-1, j-1) + A[i]
    if L[i-1][j] > L[i][j-1]:
        return PrintLPS(A, B, L, i-1, j)
    else:
        return PrintLPS(A, B, L, i, j-1)

if __name__ == "__main__":
    A = "ABBDCACB"
    B = A[::-1]

    L = [[0 for i in range(len(A))] for i in range(len(A))]
    print("The legnth of the longest palindromic subsequence is", LPS(A, L, 0, len(A)-1))
    print("The longst palindromic subsequence is: ", PrintLPS(A, B, L, len(A)-1, len(A)-1))
