from zad3testy import runtests

T = [0, 1, 2]
V = [2, 1, 5]
q = 1
l = 4



T1 = [0, 5, 10]
V1 = [10, 5, 20]
q1 = 100
l1 =  35
ans1 =  3


T2 = [
            0, 35, 40, 112, 117, 124, 125, 132, 141, 169, 172, 186, 199, 225, 248, 249, 255, 266, 273, 282, 310, 333,
            360, 371, 373, 374, 402, 418, 429, 432,
            466,
            490,
            493, 500, 502, 512, 514, 542, 544, 583, 586, 602, 613, 653, 656, 663, 664, 694, 721, 723, 739, 740, 753,
            758, 773, 823, 847, 863, 877, 879, 880,
            902,
            906,
            916, 932, 934, 957, 959, 983, 993, 995
        ]
V2 = [
            84, 75, 42, 25, 51, 40, 78, 30, 47, 58, 90, 50, 28, 75, 61, 25, 90, 98, 81, 90, 31, 72, 89, 68, 47, 10, 43,
            61, 91, 96, 47, 86, 26, 80, 54, 1, 71,
            39,
            82,
            66, 0, 49, 86, 24, 32, 87, 19, 56, 23, 96, 80, 44, 8, 32, 50, 93, 10, 55, 70, 54, 81, 54, 96, 60, 58, 44,
            59, 38, 57, 29, 18]

q2 = 80
l2 = 1000
ans2 = 17


def Find_Result(PREV, i, j):
    if i <= 0:
        return [0]
    return Find_Result(PREV, PREV[i][j][0], PREV[i][j][1]) + [i] if PREV[i][j][2] == True else Find_Result(PREV, PREV[i][j][0], PREV[i][j][1]) + []


def iamlate(T, V, q, l):
    n = len(T)
    F = [[float("inf")]*(q+1) for _ in range(n)]
    PREV = [[0] * (q + 1) for _ in range(n)]

    if V[0] >= q:
        F[0][q] = 1
        PREV[0][q] = None
    else:
        F[0][V[0]] = 1
        PREV[0][V[0]] = None

    for i in range(n):
        for j in range(q+1):
            if i + 1 < n:
                fuel = j - T[i + 1] + T[i]
                if fuel < 0:
                    continue
                else:
                    if F[i+1][fuel] > F[i][j]:
                        F[i+1][fuel] = F[i][j]
                        PREV[i+1][fuel] = (i, j, False)
                    if fuel + V[i+1] >= q and F[i+1][q] > F[i][j]+1:
                        F[i+1][q] = F[i][j] + 1
                        PREV[i + 1][q] = (i, j, True)
                    elif fuel + V[i+1] < q and F[i+1][fuel+ V[i+1]] > F[i][j] + 1:
                        F[i+1][fuel + V[i+1]] = F[i][j]+ 1
                        PREV[i + 1][fuel + V[i + 1]] = (i, j, True)


    result = float("inf")
    result_idx = 0
    for i in range(q+1):
        if i + T[n - 1] >= l and F[n - 1][i] < result:
            result = F[n-1][i]
            result_idx = i

    if result_idx + T[n-1] >= l:
        result_array = Find_Result(PREV, n-1, result_idx)
        return result_array
    else:
        return []


print(iamlate(T, V, q, l))
runtests(iamlate)