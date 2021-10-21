L = ["k","k","o","o","t","t"]
E = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ]

def letters(G, W):
    L = G[0]
    E = G[1]

    n = len(W)
    l = len(L)
    F = [[float("inf")]*n for _ in range(l)]

    for i in range(l):
        if L[i] == W[0]:
            F[i][0] = 0

    for k in range(1, n):
        for el in E:
            u = el[0]
            v = el[1]
            w = el[2]
            if L[u] == W[k-1] and L[v] == W[k]:
                F[v][k] = min(F[v][k], F[u][k-1] + w)
            elif L[v] == W[k-1] and L[u] == W[k]:
                F[u][k] = min(F[u][k], F[v][k-1] + w)

    result = float("inf")
    for i in range(l):
        if result > F[i][n-1]:
            result = F[i][n-1]
    return result


G = (L, E)

print(letters(G, "ktok"))