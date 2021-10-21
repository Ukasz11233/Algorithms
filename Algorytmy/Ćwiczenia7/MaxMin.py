T = [4, 10, 11, 3, 8, 14, 6]

A = [1, 2, 8, 4, 3, 7, 1, 9, 2, 1, 3]

A2 = [4, 3, 5, 6, 9, 11, 2]
def MaxMin(T, k):
    n = len(T)
    F = [[0]*n for _ in range(k)]

    F[0][0] = T[0]
    for i in range(1, n):
        F[0][i] += F[0][i-1] + T[i]


    for i in range(1, k):
        for j in range(i, n):
            if i == j:
                F[i][j] = min(F[i-1][j-1], T[i])
                continue
            max_ = -1
            for k in range(i-1, j):
                min_ = float("inf")
                if F[i-1][k] < min_:
                    min_ = F[i-1][k]
                if F[0][j] - F[0][k] < min_:
                    min_ = F[0][j] - F[0][k]
                if max_ < min_:
                    max_ = min_
            F[i][j] = max_

    print(F)

def Fence(A, k):
    n = len(A)
    F = [[-1]*n for _ in range(k)]
    P = [[0]*n for _ in range(k)]


    F[0][0] = A[0]
    for i in range(1, n):
        F[0][i] = F[0][i-1] + A[i]

    def FenceUtility(A, P, F, i, j):
        if i < 0 or j < 0:
            return 0, 0

        if F[i][j] >= 0:
            return F[i][j], P[i][j]

        result = -float("inf")
        idx = 1
        for l in range(i, j):
            q = min(FenceUtility(A, P, F, i-1, l)[0], F[0][j] - F[0][l])
            if result < q:
                idx = l
                result = q

        F[i][j] = result
        P[i][j] = idx

        return F[i][j], P[i][j]

    FenceUtility(A, P, F, k-1, n-1)

    end = n-1
    for i in range(k-1, -1, -1):
        if i == 0:
            print("worker", 0, ":", end=" ")
            for j in range(end+1):
                print(A[j], end=" ")
        else:
            print("worker", i ,":", end=" ")
            for j in range(P[i][end]+1, end+1):
                print(A[j], end=" ")
        end = P[i][end]
        print("")


    return F[k-1][n-1]


print(MaxMin(A2, 3))
