def NOP(A, L, i, j, cost):
    if i == 0 and j == 0 and cost == A[0][0]:
        return 1

    if cost < 0 or i < 0 or j < 0:
        return 0

    if L[i][j][cost] > 0:
        return L[i][j][cost]

    else:
        if i == 0:
            L[i][j][cost] = NOP(A, L, i, j-1, cost - A[i][j])
        if j == 0:
            L[i][j][cost] = NOP(A, L, i-1, j, cost - A[i][j])
        else:
            L[i][j][cost] = NOP(A, L, i-1, j, cost - A[i][j]) + NOP(A, L, i, j-1, cost - A[i][j])

    return L[i][j][cost]


if __name__ == "__main__":
    A = [
        [4, 7, 1, 6],
        [5, 7, 3, 9],
        [3, 2, 1, 2],
        [7, 1, 6, 3]
    ]
    L = [[[0 for _ in range(26)] for _ in range(len(A[0]))] for _ in range(len(A))]
    print(NOP(A, L, len(A)-1, len(A[0])-1, 25))
    print(L)