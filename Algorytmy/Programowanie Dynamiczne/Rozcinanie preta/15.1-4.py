P = [[1, 1], [2, 5], [3, 8], [4, 9], [5, 10], [6, 17], [7, 17], [8, 20], [9, 24], [10, 30]]


def ExtendedTopDownAux(P, n, R, S):
    if R[n] >= 0:
        return R[n], S
    if n == 0:
        q = 0
    else:
        q = -float("inf")
        for i in range(1, n+1):
            if q < P[i-1][1] + ExtendedTopDownAux(P, n - i, R, S)[0]:
                q = P[i-1][1] + ExtendedTopDownAux(P, n - i, R, S)[0]
                k = i
        S[n] = k
    R[n] = q
    return q, S


def ExtendedTopDown(P, n):
    R = []
    S = [0] * (n+1)
    for i in range(n+1):
        R.append(-float("inf"))
    return ExtendedTopDownAux(P, n, R, S)


def PrintExtendedTopDown(P, n):
    S = ExtendedTopDown(P, n)[1]
    while n > 0:
        print(S[n])
        n -= S[n]
print(PrintExtendedTopDown(P, 4))