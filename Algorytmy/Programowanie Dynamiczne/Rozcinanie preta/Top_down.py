P = [[1, 1], [2, 5], [3, 8], [4, 9], [5, 10], [6, 17], [7, 17], [8, 20], [9, 24], [10, 30]]

def Top_down_aux(P, n, R):
    if R[n] >= 0:
        return R[n]
    if n == 0:
        q = 0
    else:
        q = -float("inf")
        for i in range(1, n+1):
            q = max(q, P[i-1][1] + Top_down_aux(P, n - i, R))
    R[n] = q
    S[n]
    return q


def Top_down(P, n):
    R = []
    for i in range(n+1):
        R.append(-float("inf"))
    return Top_down_aux(P, n, R)



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

print(ExtendedTopDown(P, 10))