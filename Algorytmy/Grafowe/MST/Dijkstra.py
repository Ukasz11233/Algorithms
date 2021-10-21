from queue import PriorityQueue

G = [[(1,3), (2,1)],
    [(3,1), (2,1), (0, 3)],
    [(3,4), (1, 1), (0, 1)],
    [(1, 1), (2, 4)]]


G2 = [[(1, 6), (2, 7)],
     [(2, 8), (4, -4), (3, 5)],
     [(4, 9), (3, -3)],
     [(1, -2)],
     [(3, 7), (0, 2)]]



G3 = [[-1, 2,-1,-1, 1],
    [ 2,-1, 3, 1,-1],
    [-1, 3,-1, 5,-1],
    [-1, 1, 5,-1, 4],
    [ 1,-1,-1, 4,-1]]


def Find_Cycle(parent, t):
    if parent[t] == -1:
        return [t]

    return [t] + Find_Cycle(parent, parent[t])


def Relax(u, v, distance, parent, w):
    if distance[v] > distance[u] + w:
        distance[v] = distance[u] + w
        parent[v] = u


def Dijkstra(G, s):
    n = len(G)
    Q = PriorityQueue()
    dist = [float("inf")]*n
    parent = [None]*n
    visited = [False]*n

    dist[s] = 0
    parent[s] = -1

    Q.put((0, s))

    while not Q.empty():
        u = Q.get()[1]
        visited[u] = True

        for el in G[u]:
            if visited[el[0]] == False:
                parent[el[0]] = u
                Relax(u, el[0], dist, parent, el[1])
                Q.put((dist[el[0]], el[0]))

    return dist


def Dijkstra_on_Matrix(G, s, t):
    n = len(G)
    Q = PriorityQueue()
    dist = [float("inf")]*n
    parent = [None]*n
    visited = [False]*n

    dist[s] = 0
    visited[s] = True
    parent[s] = -1

    Q.put((0, s))

    while not Q.empty():
        u = Q.get()[1]
        visited[u] = True

        for i in range(n):
            if u != s or i != t:
                if G[u][i] > -1 and visited[i] == False:
                    parent[i] = u
                    Relax(u, i, dist, parent, G[u][i])
                    Q.put((dist[i], i))

    A = Find_Cycle(parent, t)

    return A

#print(Dijkstra(G, 0))

#print(Dijkstra_on_Matrix(G2, 0, 4))
