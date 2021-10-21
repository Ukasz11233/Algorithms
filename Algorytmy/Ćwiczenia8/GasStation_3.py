S = [1, 5, 7, 11, 12, 17]
P = [2, 2, 4, 3, 5, 1]


def distance(S, i):
    if i == 1:
        return S[0]
    else:
        return (S[i-1] - S[i-2])


def PrintSolution(Stations, S, P, i, j):
    if Stations[i][j] == 1:
        print(distance(S, i), "litrów za:", P[i-1], "zł na stacji", i-1 )
        PrintSolution(Stations, S, P, i-1, j)
    if Stations[i][j] == 2:
        print("nie tankował na stacji", i-1)
        PrintSolution(Stations, S, P, i-1, j - distance(S, i))



def GasStation(S, P, L):
    n = len(S)
    Stations = [[0]*(L+1) for _ in range(n+1)]
    F = [[-1]*(L+1) for _ in range(n+1)]

    F[0][0] = 0
    for i in range(1, n+1):
        for j in range(L+1):
            if F[i-1][j] >= 0:
                if F[i][j] == -1 or (F[i][j] >=0 and F[i-1][j] + P[i-1]*distance(S, i) < F[i][j]):
                    F[i][j] = F[i-1][j] + P[i-1]*distance(S, i)
                    Stations[i][j] = 1
                if j + distance(S, i) <= L:
                    F[i][j + distance(S, i)] = F[i - 1][j]
                    Stations[i][j+distance(S, i)] = 2

    PrintSolution(Stations, S, P, i, j)
    return F[i][j]

print(GasStation(S, P, 6))


S = [0, 4, 6, 7, 9 ,11, 12]
P = [4, 2, 5, 2, 1, 3, 2]


def Tank3(S, P, l):

    n = len(S)
    F = [[float("inf")]*(l+1) for _ in range(n)]
    F[0][l] = 0

    def Tank_utility(F, S, P, i, j):
        if i < 0 or j < 0 or j > l:
            return float("inf")

        if F[i][j] < float("inf"):
            return F[i][j]

        F[i][j] = min(Tank_utility(F, S, P, i-1, j - (S[i] - S[i-1])), Tank_utility(F, S, P, i-1, l) + P[i]*(l - (j - S[i] + S[i-1])))
        return F[i][j]

    Tank_utility(F, S, P, n-1, l)

    return F

print(Tank3(S, P, 4))

def PrintResult(R, i, j, l):
    if i == 0:
        return

    if j == l:
        PrintResult(R, R[i][j][0], R[i][j][1], l)
        print(i, end=" ")
    else:
        PrintResult(R, R[i][j][0], R[i][j][1], l)


def Tank4(S, P, l):
    n = len(S)
    F = [[float("inf")]*(l+1) for _ in range(n)]
    R = [[(0, 0)]*(l+1) for _ in range(n)]

    for i in range(l+1):
        F[0][i] = 0

    for i in range(n):
        for j in range(l+1):
            if F[i][j] < float("inf"):
                if i + 1 < n and j >= S[i+1] - S[i]:
                    F[i+1][j-(S[i+1] - S[i])] = F[i][j]
                    R[i+1][j-(S[i+1] - S[i])] = (i, j)
                    if F[i+1][l] > F[i][j] + P[i+1]*(l-j):
                        F[i+1][l] = F[i][j] + P[i+1]*(l-(j - (S[i+1] - S[i])))
                        R[i+1][l] = (i, j)


    result = float("inf")
    idx = None
    for i in range(l+1):
        if F[n-1][i] < result:
            result = F[n-1][i]
            idx = i


    PrintResult(R, n-1, idx, l)
    print(" ")
    return F[n-1][idx]

print(Tank4(S, P, 4))