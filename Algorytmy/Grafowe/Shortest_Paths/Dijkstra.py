from queue import PriorityQueue

G = [[(1, 10), (2, 5)],
     [(2, 2), (3, 1)],
     [(1, 3), (3, 9), (4, 2)],
     [(4, 4)],
     [(3, 6), (0, 7)]]


G2 = [[(1, 15), (2, 10)],
      [(0, 15), (2, 1), (3, 2)],
      [(0, 10), (1, 1), (3, 5)],
      [(1, 2), (2, 5)]]

G3 = [[(1, 10), (2, 5)],
     [(0, 10), (2, 5), (3, 8), (4, 9)],
     [(0, 5), (1, 3), (4, 4)],
     [(1, 8), (6, 6)],
     [(2, 4), (1, 9), (5, 2), (7, 3)],
     [(4, 2), (6, 4)],
     [(3, 6), (5, 4), (7, 1), (8, 5)],
     [(4, 3), (6, 1), (8, 2)],
     [(5, 5), (6, 2)]]


def PrintResult(parent, t):
    if parent[t] == -1:
        print(t, end=" ")
        return
    PrintResult(parent, parent[t])
    print(t, end=" ")


def Relax(dist, parent, u, v, w):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        parent[v] = u


def Dijkstra(G, s, t):
    n = len(G)
    dist = [float("inf")]*n
    parent = [None]*n
    visited = [False]*n
    dist[0] = 0
    parent[0] = -1


    Q = PriorityQueue()
    Q.put((0, 0))

    while not Q.empty():
        u = Q.get()[1]
        visited[u] = True

        for el in G[u]:
            if visited[el[0]] == False:
                Relax(dist, parent, u, el[0], el[1])
                if dist[el[0]] > el[1] or u == s:
                    Q.put((dist[el[0]], el[0]))
    PrintResult(parent, t)
    return dist

print(Dijkstra(G3, 0, 8))