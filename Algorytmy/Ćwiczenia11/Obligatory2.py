G = [[1, 0, 0, 0],
     [0, 1, 1, 1],
     [0, 1, 1, 0],
     [1, 0, 1, 1]]

def Transitive_Closure(G):
    n = len(G)
    T = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j or G[i][j] > 0:
                T[i][j] = 1

    for k in range(1, n+1):
        for i in range(n):
            for j in range(n):
                if T[i][j] > 0:
                    T[i][j] = 1
                else:
                    if T[i][k-1] > 0 and T[k-1][j] > 0:
                        T[i][j] = 1
    return T

print(Transitive_Closure(G))