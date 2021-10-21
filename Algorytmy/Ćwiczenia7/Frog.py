E = [3, 4, 2, 5, 1, 2, 1, 2, 3]
E2 = [4,5,2,4,1,2,1,0]
E3 = [2,2,1,0,0,0]

def PrintResult(R, i, j):
    if i <= 0:
        print(i, end=" ")
        return
    PrintResult(R, R[i][j][0], R[i][j][1])
    print(i, end=" ")

def JumpingFrog(E):
    n = len(E)
    F = [[-1]*(n) for _ in range(n)]
    R = [[0]*n for _ in range(n)]
    F[0][E[0]] = 0
    R[0][E[0]] = (0, 0)

    for i in range(n):
        for j in range(n):
            if F[i][j] >= 0:
                for k in range(1, j+1):
                    if i + k < n and j + E[i+k] - k < n:
                        if F[i + k][j + E[i + k] - k] < 0:
                            F[i+k][j+E[i+k]-k] = F[i][j] + 1
                            R[i+k][j+E[i+k]-k] = (i, j)

    print(R)
    result = float("inf")
    for i in range(n):
        if F[n-1][i] > -1 and F[n-1][i] < result:
            result = F[n-1][i]
            idx = i

    PrintResult(R, n-1, idx)
    print()
    return result

print(JumpingFrog(E3))