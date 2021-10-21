P = [[1, 1], [2, 5], [3, 8], [4, 9], [5, 10], [6, 17], [7, 17], [8, 20], [9, 24], [10, 30]]

def Bottom_up(P, n):
    R = [0]*(n+1)
    R[0] = 0
    for j in range(1, n + 1):
        q = -float("inf")
        for i in range(1, j+1):
            q = max(q, P[i-1][1] + R[j - i])
        R[j] = q
    return R[n]


def ExtendedBottomUp(P, n):
    R = [0] * (n + 1)
    S = [0] * (n + 1)
    R[0] = 0
    for j in range(1, n + 1):
        q = -float("inf")
        for i in range(1, j+1):
            if q < P[i - 1][1] + R[j - i]:
                q = max(q, P[i - 1][1] + R[j - i])
                S[j] = i
        R[j] = q
    return R[n], S

print(ExtendedBottomUp(P, 5))