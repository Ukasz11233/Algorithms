from queue import PriorityQueue

G = [[(1, 10), (2, 5)],
     [(0, 10), (3, 3), (4, 7)],
     [(0, 5), (4, 4)],
     [(1, 3), (4, 1), (5, 7)],
     [(2, 4), (1, 7), (3, 1), (5, 2)],
     [(3, 7), (4, 2)]
     ]


def Relax(dist, parent, u, v, w):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        parent[v] = u

def Dijkstra(G, Q, dist, parent):
    n = len(G)
    visited = [False]*n

    while not Q.empty():
        tmp = Q.get()
        u = tmp[1]
        Alice = tmp[2]

        visited[u] = True
        for el in G[u]:
            if visited[el[0]] == False:
                if Alice == False:
                    Relax(dist, parent, u, el[0], 0)  # prowadzi bob wiec nie dodaje wagi
                    Q.put((dist[el[0]], el[0], True))
                else:
                    Relax(dist, parent, u, el[0], el[1])
                    Q.put((dist[el[0]], el[0], False))


    return dist, parent


def PrintPath(result, s, t):
    if t == s:
        print(s, end=" ")
        return
    PrintPath(result, s, result[t])
    print(t, end=" ")

def ALice_and_Bob(G, s, t):
    n = len(G)
    dist_A = [float("inf")]*n
    parent_A = [None]*n
    dist_B = [float("inf")]*n
    parent_B = [None]*n
    Q = PriorityQueue()


    Q.put((0, s, False))  # False - zaczyna BOB
    dist_B[s] = 0
    parent_B[s] = -1
    dist_B, parent_B = Dijkstra(G, Q, dist_B, parent_B)

    Q.put((0, s, True))  # True - zaczyna Alicja
    dist_A[s] = 0
    parent_A[s] = -1
    dist_A, parent_A = Dijkstra(G, Q, dist_A, parent_A)


    return (PrintPath(parent_A, s, t), "ALice zaczyna") if dist_A[t] < dist_B[t]  else (PrintPath(parent_B, s, t), "Bob zaczyna")

print(ALice_and_Bob(G, 0, 5))
