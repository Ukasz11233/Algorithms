from queue import PriorityQueue

E2 = [(0, 2, 7), (0, 1, 1), (1, 2, 8), (2, 3, 2), (3, 4, 5), (1, 4, 4), (2, 5, 3), (1, 5, 12), (5, 4, 6)]

G = [[-1, 2,-1,-1, 1],
    [ 2,-1, 3, 1,-1],
    [-1, 3,-1, 5,-1],
    [-1, 1, 5,-1, 4],
    [ 1,-1,-1, 4,-1]]


def Prim(E):
    n = len(E)
    Q = PriorityQueue()
    visited = [False]*n
    dist = [float("inf")]*n
    parent = [None]*n

    dist[0] = 0
    parent[0] = 0
    Q.put((0, 0))
    while not Q.empty():
        u = Q.get()[1]
        visited[u] = True

        for i in range(n):
            if G[u][i] > 0 and visited[i] == False:
                if dist[i] > G[u][i]:
                    dist[i] = G[u][i]
                    parent[u] = i
                    Q.put((dist[i], i))

    return dist


print(Prim(G))