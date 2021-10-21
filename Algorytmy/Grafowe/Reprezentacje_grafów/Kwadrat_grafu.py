G = [[1, 2], [3], [1], [2]]

def SquareGraph(G):
    n = len(G)
    GS = [[] for _ in range(n)]

    for i in range(n):
        for el in G[i]:
            GS[i].append(el)
            GS[el].append(i)

    return GS

print(SquareGraph(G))

M = [[0, 1, 1, 0], [0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0]]

def SquareMatrix(M):
    n = len(M)
    MS = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if M[i][j] == 1:
                MS[i][j], MS[j][i] = 1, 1
    return MS

print(SquareMatrix(M))