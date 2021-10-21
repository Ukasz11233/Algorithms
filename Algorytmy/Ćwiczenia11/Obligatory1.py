from queue import PriorityQueuegra planoszwa statki

G = [[(1, 10), (2, 5)],
     [(0, 10), (2, 5), (3, 8), (4, 9)],
     [(0, 5), (1, 3), (4, 4)],
     [(1, 8), (6, 6)],
     [(2, 4), (1, 9), (5, 2), (7, 3)],
     [(4, 2), (6, 4)],
     [(3, 6), (5, 4), (7, 1), (8, 5)],
     [(4, 3), (6, 1), (8, 2)],
     [(5, 5), (6, 2)]]

G2 = [[(1, 15), (2, 10)],
      [(0, 15), (2, 1), (3, 2)],
      [(0, 10), (1, 1), (3, 5)],
      [(1, 2), (2, 5)]]

G3 = [[(1, 5), (2, 3)],
     [(0, 5), (2, 4), (3, 7)],
     [(0, 3), (1, 4), (3, 3), (4, 6)],
     [(1, 7), (2, 3), (4, 2), (5, 10)],
     [(2, 6), (3, 2), (5, 1)],
     [(3, 10), (4, 1)]]


def Relax(dist, parent, u, v, w, prev_w):
    if dist[v] < dist[u] + w and w < prev_w:
        dist[v] = w
        parent[v] = u


def Print_Path(parent, t):
    if parent[t] < 0:
        print(t, end=" ")
        return
    Print_Path(parent, parent[t])
    print(t, end=" ")


def Shortest_Decreasing_Path(G, s, t):
    n = len(G)
    visited = [False]*n
    dist = [-float("inf")]*n
    parent = [None]*n
    Q = PriorityQueue()

    dist[s] = 0
    parent[s] = -1
    prev_w = float("inf")
    Q.put((0, s, prev_w))

    while not Q.empty():
        tmp = Q.get()
        u = tmp[1]
        prev_w = tmp[2]
        visited[u] = True

        for el in G[u]:
            v = el[0]
            w = el[1]
            if visited[el[0]] == False:
                print(u, v, w, prev_w)
                Relax(dist, parent, u, v, w, prev_w)
                if w < prev_w:
                    Q.put((-dist[v], v, w))
        if u == t:
            break


    Print_Path(parent, t)
    return dist

print(Shortest_Decreasing_Path(G, 0, 8))