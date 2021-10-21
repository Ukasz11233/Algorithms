# Rozwiazanie polega na obliczeniu odleglosci pomiedzy wszystkimi wierzcholkami za pomoca algorytmu Floyda-Warshalla O(V^3),
# Nastepnie sprawdzamy pomiedzy ktorymi wierzcholkami istnieje sciezka o sumie nie mniejszej niz D, czy wierzcholki maja rozne kolory, i jesli tak to tworzymy pomiedzy nimi krawedz
# nieskierowana. Tworzymy rowniez pomiedzy wierzcholkami niebieskimi superzrodlo ( o pojemnosci kazdej krawedzi 1), a pomiedzy wierzcholkami zielonymi superujscie ( rwoniez o pojemnosci kazdej krawedzi 1)
# Na koniec odpalamy algorytm edmodsa_karp-a na nowym grafie i otrzymujemy maksymalny przeplyw. Wierzcholki nigdy nam sie nie powtorza, poniewaz kazda krawedz superujscia po pojemnosc 1, wiec akceptuje tylko 1 wierzcholek niebieski
# zlozonosc to O(V^3 + V^2 + V*E^2) = O(V*E^2)


#from zad3testy import runtests
#from zad3EK import edmonds_karp
import copy, collections

def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = collections.deque()
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.popleft()
        for ind, val in enumerate(graph[u]):
            if (visited[ind] == False) and (val > 0):
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
    return visited[t]

def edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow

def Floyd_Warshall(G):
    n = len(G)

    S = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                S[i][j] = 0
            elif G[i][j] == 0:
                S[i][j] = float("inf")
            else:
                S[i][j] = G[i][j]

    for k in range(1, n+1):
        for i in range(n):
            for j in range(n):
                S[i][j] = min(S[i][j], (S[i][k-1] + S[k-1][j]))
    return S


def BlueAndGreen(T, K, D):
    dist = Floyd_Warshall(T)
    n = len(T)
    S = [[0]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            if dist[i][j] >= D:
                if K[i] == "B" and K[j] == "G":
                    S[n][i], S[i][n] = 1, 1

                    S[n+1][j], S[j][n+1] = 1, 1
                    S[i][j], S[j][i] = 1, 1
                elif K[i] == "G" and K[j] == "B":
                    S[n][j], S[j][n] = 1, 1
                    S[n+1][i], S[i][n+1] = 1, 1
                    S[i][j], S[j][i] = 1, 1


    return edmonds_karp(S, n, n+1)

T = [
[0, 1, 1, 0, 1],
[1, 0, 0, 1, 0],
[1, 0, 0, 0, 1],
[0, 1, 0, 0, 1],
[1, 0, 1, 1, 0],
]
K = ["B", "B", "G", "G", "B"]
D = 2
print(BlueAndGreen(T, K, D))