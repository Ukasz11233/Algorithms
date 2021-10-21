A = [4, 2, 5, 9, 7, 6, 10, 3, 1]

def LBSWrap(A, L):
    incr = LBSIncr(A, L, 0, -float("inf"), 0)
    decr = LBSDecr(A, L, 0, float("inf"), 0)
    return incr + decr - 1

def LBSIncr(A, L, curr, prev, p_idx):
    if curr == len(A):
        return 0
    if L[curr][p_idx] > 0:
        return L[curr][p_idx]
    else:
        excl = LBSIncr(A, L, curr + 1, prev, p_idx)
        incl = 0
        if A[curr] > prev:
            incl = LBSIncr(A, L, curr + 1, A[curr], p_idx + 1) + 1
        L[curr][p_idx] = max(excl, incl)
    return L[curr][p_idx]

def LBSDecr(A, L, curr, prev, p_idx):
    if curr == len(A):
        return 0
    if L[curr][p_idx] > 0:
        return L[curr][p_idx]
    else:
        excl = LBSIncr(A, L, curr + 1, prev, p_idx)
        incl = 0
        if A[curr] < prev:
            incl = LBSIncr(A, L, curr + 1, A[curr], p_idx + 1) + 1
        L[curr][p_idx] = max(excl, incl)
    return L[curr][p_idx]



if __name__ == "__main__":
    L = [[0 for _ in range(len(A))] for _ in range(len(A))]
    print(LBSWrap(A, L))