from queue import PriorityQueue

G = [[(1, 10), (2, 5)],
     [(2, 2), (3, 1)],
     [(1, 3), (3, 9), (4, 2)],
     [(4, 4)],
     [(3, 6), (0, 7)]]


def Relax(dist, u, v, w):
    if dist[v] > dist[u] * w:
        dist[v] = dist[u] * w



def Dijkstra(G, s):
    n = len(G)
    dist = [-float("inf")]*n
    Q = PriorityQueue()
    visited = [False]*n

    dist[s] = 1
    Q.put((0, s))

    while not Q.empty():
        u = Q.get()[1]
        visited[u] = True

        for el in G[u]:
            if visited[el[0]] == False:
                Relax(dist, u, el[0], el[1])
                Q.put((dist[el[0]], el[0]))

    return dist

print(Dijkstra(G, 0))