W = [4, 5, 12, 9, 1, 13]
P = [10, 8, 4, 5, 3, 7]
H = [4, 3, 5, 2, 1, 3]

def Knapsack_2D(W, P, maxW, maxH):
    n = len(W)
    F = [[[-1]*(maxH+1) for _ in range(maxW+1)] for _ in range(n)]
    for i in range(maxW+1):
        for j in range(maxH+1):
            if i > W[0] and i > H[0]:
                F[0][i][j] = P[0]
            else:
                F[0][i][j] = 0

    def Knapsack_2D_utility(W, P, F, i, w, h):
        if i < 0 or w < 0 or h < 0:
            return 0
        if F[i][w][h] >= 0:
            return F[i][w][h]

        F[i][w][h] = max(Knapsack_2D_utility(W, P, F, i-1, w, h), Knapsack_2D_utility(W, P, F, i-1, w - W[i], h - H[i]) + P[i])

        return F[i][w][h]

    Knapsack_2D_utility(W, P, F, n-1, maxW, maxH)
    print(F[-1][-1][-1])
print(Knapsack_2D(W, P, 24, 5))