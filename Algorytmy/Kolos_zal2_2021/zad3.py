# Łukasz Chmielewski
# Moje rozwiązanie polega na znalezieniu najkrótszej ścieżki za pomocą algorytmu Dijkstry, z tym, że zapamiętujemy w tablicy parent wszystkie najkótsze ścieżki.
# Następnie DFS-em przechodzę po znalezionych ścieżkach i zliczam krawędzie.
# Złożoność to O(ElogV + V + E)

from zad3testy import runtests

import queue
from collections import deque


def Relax(dist, parent, u, v, w):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        parent[v] = [u]
    elif dist[v] == dist[u] + w:
        for i in range(len(parent[v])):
            if parent[v][i] == u:
                return
        parent[v].append(u)


def DFS(parent, s, t):
    n = len(parent)
    visited = [False] * n
    result = 0

    def DFSVisit(u):
        nonlocal result
        if u == s:
            return result

        visited[u] = True
        print(u, result)
        result += 1

        for el in parent[u]:
            if visited[el] == False:
                DFSVisit(el)

    for el in parent[t]:
        if visited[el] == False:
            result += 1
            DFSVisit(el)

    return result


def paths(G, s, t):
    n = len(G)

    dist = [float("inf")] * n
    visited = [False] * n
    parent = [[] for _ in range(n)]
    Q = queue.PriorityQueue()

    Q.put((0, s))
    dist[s] = 0
    parent[s] = -1

    while not Q.empty():
        u = Q.get()[1]
        visited[u] = True

        for el in G[u]:
            v = el[0]
            w = el[1]
            if visited[v] == False:
                Relax(dist, parent, u, v, w)
                Q.put((dist[v], v))

    return DFS(parent, s, t)


runtests(paths)

