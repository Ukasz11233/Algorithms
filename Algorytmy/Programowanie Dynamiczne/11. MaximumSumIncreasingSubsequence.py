A = [2, 7, 3, 5]

def MSIS(A, L, curr, prev, p_idx, sum):
    if curr == len(A):
        return sum
    if L[curr][p_idx] > 0:
        return L[curr][p_idx]
    excl = MSIS(A, L, curr + 1, prev, p_idx, sum)
    incl = sum
    if A[curr] > prev:
        incl = MSIS(A, L, curr + 1, A[curr], p_idx + 1, sum + A[curr])
    L[curr][p_idx] = max(incl, excl)
    return L[curr][p_idx]

if __name__ == "__main__":
    L = [[0 for _ in range(len(A))] for _ in range(len(A))]
    print(MSIS(A, L, 0, -float("inf"), 0, 0))
    print(L)