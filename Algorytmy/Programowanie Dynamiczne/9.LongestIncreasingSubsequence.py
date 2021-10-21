A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
B = [0, 8, 4, 5]

def LIS(A, L, curr, prev, p_idx):
    if curr == len(A):
        return 0
    if L[curr][p_idx] > 0:
        return L[curr][p_idx]
    else:
        excl = LIS(A, L, curr + 1, prev, p_idx)
        incl = 0
        if A[curr] > prev:
            incl = LIS(A, L, curr + 1, A[curr], curr) + 1
        L[curr][p_idx] = max(incl, excl)
    return L[curr][p_idx]

def PrintLis(A, L, i, j):
    if i == len(A) or j == len(A):
        return
    else:
        print(A[i])
        q1 = PrintLis(A, L, i+1, j+1)
        q2 = PrintLis(A, L, i+1, j)
        q3 = PrintLis(A, L, i, j+1)
        return max(q1, q2, q3)

if __name__ == "__main__":
    L = [[0 for i in range(len(B))] for i in range(len(B))]
    print(LIS(B, L, 0, -float("inf"), 0))
    print(L)