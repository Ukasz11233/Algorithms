T = [4, 3, 5, 2, 3]

def PrintResult(F):

    for i in range(len(F)-1, -1, -1):
        if F[i] > F[i-1]:
            print(F[i] - F[i-1], end=" ")
    print(F[0])

def Logger(T):
    n = len(T)
    F = [0]*n

    F[0] = T[0]
    F[1] = max(T[1], F[0])

    for i in range(2, n):
        F[i] = max(F[i-1], F[i-2] + T[i])

    PrintResult(F)
    return F[-1]

print(Logger(T))

