T = [123, 890, 688, 587, 257, 246]
T2 = [587,990,257,246,668,132]

def IsPossible(first, second):
    s_first = str(first)
    s_second = str(second)

    for i in range(len(s_first)):
        for j in range(len(s_second)):
            if s_first[i] == s_second[j]:
                return True

    return False



def MinCost(T):
    T.sort()
    print(T)
    n = len(T)
    F = [[float("inf")]*n for _ in range(n)]

    for i in range(n-1):
        if IsPossible(T[i], T[i+1]):
            F[i][i+1] = T[i+1] - T[i]

    for i in range(2, n):
        for j in range(n - i):
            l = j + i
            if IsPossible(T[j], T[l]):
                F[j][l] = T[l] - T[j]
            else:
                F[j][l] = F[j][l-1] + F[l-1][l]

    print(F)
    return F[0][n-1] if F[0][n-1] != float("inf") else -1



print(MinCost(T))