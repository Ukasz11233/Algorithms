A = [1, 5, 8]


def PrintResult(F, A, i, j):
    if i == 0 and j == 0:
        return
    if i == 0:
        if j >= A[i]:
            PrintResult(F, A, i, j - A[i])
            print(A[i], end=" ")

    elif F[i-1][j] == F[i][j]:
        PrintResult(F, A, i-1, j)
    else:
        if j >= A[i]:
            PrintResult(F, A, i, j-A[i])
            print(A[i], end=" ")


def MoneyExchange(A, amount):
    n = len(A)
    F = [[-1]*(amount + 1) for _ in range(n)]

    for i in range(n):
        F[i][0] = 0

    k = 1
    while A[0]*k <= amount:
        F[0][A[0]*k] = k
        k += 1

    for i in range(1, n):
        for j in range(1, amount+1):
            if F[i-1][j] > -1:
                q = F[i-1][j]
            else:
                q = float("inf")

            if j >= A[i] and q > F[i][j - A[i]] + 1:
                q = F[i][j-A[i]] + 1
            F[i][j] = q

    PrintResult(F, A, n-1, amount)
    return F

def PrintSolution(A, F, i):
    if i == 0:
        return
    for j in range(len(A)):
        if i >= A[j]:
            if F[i - A[j]] == F[i] - 1:
                PrintSolution(A, F, i-A[j])
                print(A[j], end=" ")
                return

def MoneyExchange2(A, amount):
    n = len(A)
    F = [float("inf")]*(amount+1)
    F[0] = 0
    for i in range(amount+1):
        for j in range(n):
            if i >= A[j]:
                q = F[i-A[j]] + 1
                if F[i] > q:
                    F[i] = q
    PrintSolution(A, F, amount)
    return F
print(MoneyExchange(A, 7))