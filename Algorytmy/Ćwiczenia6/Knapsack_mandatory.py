P1 = [1, 3, 2]
W1 = [2, 1, 2]

P2 = [10, 8, 4, 5, 3, 7]
W2 = [4, 5, 12, 9, 1, 13]

def Knapsack(P, W, maxW):
    n = len(P)
    profits_sum = 0
    for el in P:
        profits_sum += el
    F = [[-1]*(profits_sum+1) for _ in range(n)]

    F[0][P[0]] = W[0]
    for i in range(n):
        F[i][0] = 0

    for i in range(1, n):
        for p in range(profits_sum+1):
            if F[i-1][p] >= 0:
                F[i][p] = F[i-1][p]
                if p + P[i] <= profits_sum and F[i][p] + W[i] <= maxW:
                        F[i][p+P[i]] = F[i][p] + W[i]

    for i in range(profits_sum-1, -1, -1):
        if F[n-1][i] >= 0:
            return i

print(Knapsack(P2, W2, 24))


def Knapsack2(P, W, maxW):
    n = len(P)
    F = [[0] * (maxW+ 1) for _ in range(n)]

    for w in range(W[0], maxW+1):
        F[0][w] = P[0]

    for i in range(1, n):
        for w in range(1, maxW+1):
            F[i][w] = F[i-1][w]
            if w >= W[i]:
                F[i][w] = max(F[i][w], F[i-1][w - W[i]] + P[i])
    return F[-1][-1]

print(Knapsack2(P2, W2, 24))