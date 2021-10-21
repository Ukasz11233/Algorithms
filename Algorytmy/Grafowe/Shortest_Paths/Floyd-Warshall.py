G = [[0, 3, 8, 0, -4],
     [0, 0, 0, 1, 7],
     [0, 4, 0, 0, 0],
     [2, 0, -5, 0, 0],
     [0, 0, 0, 6, 0]]





def Floyd_Warshall(G):
    n = len(G)

    S = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                S[i][j] = 0
            elif G[i][j] == 0:
                S[i][j] = float("inf")
            else:
                S[i][j] = G[i][j]

    for k in range(1, n+1):
        for i in range(n):
            for j in range(n):
                S[i][j] = min(S[i][j], (S[i][k-1] + S[k-1][j]))
    return S

print(Floyd_Warshall(G))