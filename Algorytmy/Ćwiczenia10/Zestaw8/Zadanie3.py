A = [6, 4, 3, 2, 3, 3, 4]


def PrintResult(A, P, i, j):
    if i == 0:
        if P[i][j][2] == 0:
            print("L:", A[i])
        else:
            print("R:", A[i])
    if i > 0 and j >= 0:
        PrintResult(A, P, P[i][j][0], P[i][j][1])
        if P[i][j][2] == 0:
            print("L:", A[i])
        elif P[i][j][2] == 1:
            print("R:", A[i])


def Cars(A, d):
    n = len(A)
    F = [[(-1, -1, d)]*(d+1) for _ in range(n)]
    P = [[(None, None, None)]*(d+1) for _ in range(n)]

    F[0][0] = (0, 1, d-A[0])
    P[0][0] = (0, 0, 1)
    F[0][A[0]] = (1, 0, d)
    P[0][A[0]] = (0, 0, 0)

    for i in range(1, n):
        for j in range(d+1):
            if F[i-1][j][0] >= 0:
                if j + A[i] <= d:
                    F[i][j+A[i]] = (F[i-1][j][0] + 1, F[i-1][j][1], F[i-1][j][2])
                    P[i][j+A[i]] = (i-1, j, 0)
                if F[i-1][j][2] >= A[i]:
                    F[i][j] = (F[i-1][j][0], F[i-1][j][1] + 1, F[i-1][j][2] - A[i])
                    P[i][j] = (i-1, j, 1)

    result = -float("inf")
    idx = None
    print(F)
    for j in range(n-1, -1, -1):
        for i in range(d, -1, -1):
            if F[j][i][0] + F[j][i][1] > result:
                result = F[j][i][0] + F[j][i][1]
                idx = (j, i)
    PrintResult(A, P, idx[0], idx[1])
    return result

print(Cars(A, 9))