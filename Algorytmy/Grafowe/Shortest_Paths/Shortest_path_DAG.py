G = [[(1, 5), (2, 3)],
     [(2, 2), (3, 6)],
     [(3, 7), (4, 4), (5, 2)],
     [(4, -1), (5, 1)],
     [(5, -2)],
     []]


def TopologicalSort(G, s):
    n = len(G)
    visited = [False]*n
    dist = [0]*n
    time = 0
    result = []

    def DFS_visit(G, u):
        visited[u] = True
        nonlocal time
        time += 1

        for el in G[u]:
            if visited[el[0]] == False:
                time += 1
                DFS_visit(G, el[0])
        time += 1
        dist[u] = time
        result.append(u)

    for i in range(n):
        if visited[i] == False:
            DFS_visit(G, i)

    return result


def Relax(dist, u, v, w):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w


def Dag_Shortest(G, s):
    n = len(G)
    shortest = TopologicalSort(G, s)
    print(shortest)
    dist = [float("inf")]*n

    dist[shortest[n-1-s]] = 0
    for i in range(n-1-s, -1, -1):
        for el in G[shortest[i]]:
            Relax(dist, shortest[i], el[0], el[1])

    return dist

print(Dag_Shortest(G, 2))