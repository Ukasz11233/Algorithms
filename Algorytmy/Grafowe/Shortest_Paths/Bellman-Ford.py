G = [[(1, 6), (2, 7)],
     [(2, 8), (4, -4), (3, 5)],
     [(4, 9), (3, -3)],
     [(1, -2)],
     [(3, 7), (0, 2)]]


def Relax(dist, u, v, w):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w



def Bellman_Ford(G, s):
    n = len(G)
    dist = [float("inf")]*n
    dist[s] = 0

    for i in range(n):   # v razy
        for u in range(n):  # relaksuje wszystkie krawedzie
            for el in G[u]:
                v = el[0]
                w = el[1]
                Relax(dist, u, v, w)

    for u in range(n):   # wykrywanie ujemnych cykli
        for el in G[u]:
            v = el[0]
            w = el[1]
            if dist[v] > dist[u] + w:
                return False
    print(dist)
    return True

print(Bellman_Ford(G, 0))
