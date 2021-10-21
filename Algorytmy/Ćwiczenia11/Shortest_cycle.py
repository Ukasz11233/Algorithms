from copy import deepcopy
from queue import PriorityQueue


# Funkcja wykorzystuje algorytm Dijkstry.
# W glownej petli sprawdzamy kazda krawedz grafu w nastepujacy sposob:
# dla krawedzi (u, v) sprawdzamy za pomoca algorytmu Dijkstry najkrotszej sciezki z u do v, ale "usuwajac" krawedz (u, v) z grafu.
# kazdy wynik zapisujemy w pomocniczej tablicy
# Na koniec wystarczy przeiterowac po pomocniczej tablicy w celu znalezienia najkrotszego cyklu.
# Zlozonosc to O(E*V^2) poniewaz dla kazdej krawedzi wywolujemy algorytm Dijkstry.


def Find_Cycle(parent, t):  # funkcja zwracajaca wierzcholki sciezki tworzacej cykl
    if parent[t] == None:
        return []

    if parent[t] == -1:
        return [t]

    return [t] + Find_Cycle(parent, parent[t])


def Relax(u, v, distance, parent, w):
    if distance[v] > distance[u] + w:
        distance[v] = distance[u] + w
        parent[v] = u


def Dijkstra_on_Matrix(G, s,
                       t):  # zmodyfikowany algorytm Dijkstry, tak aby znalazl najkrotsza sciezke z wierzcholka s do t, pomijajac krawedz (s, t)
    n = len(G)

    Q = PriorityQueue()
    dist = [float("inf")] * n
    parent = [None] * n
    visited = [False] * n

    dist[s] = 0
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

    return Find_Cycle(parent, t), dist[t] + G[s][t]  # zwracam tablice wierzcholkow cyklu oraz jego dlugosc


def min_cycle(G):
    n = len(G)
    E = []
    visited = [[0] * n for _ in range(n)]  # tablica w ktorej bede zaznaczal ktore krawedzie juz zostaly sprawdzone

    for i in range(n):  # iteracja po macierzy w ktorej sprawdzam kazda krawedz zmodyfikowanym algorytmem Dijkstry
        for j in range(n):
            if G[i][j] >= 0 and visited[i][j] == 0:
                visited[i][j] = 1
                visited[j][i] = 1
                E.append(Dijkstra_on_Matrix(G, i, j))

    min_cycle = float("inf")
    min_idx = 0
    for i in range(len(E)):  # szukam najkrotszego cyklu w tablicy E
        if E[i][1] < min_cycle:
            min_idx = i
            min_cycle = E[i][1]

    return E[min_idx][0]


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[-1, 2, -1, -1, 1],
     [2, -1, 4, 1, -1],
     [-1, 4, -1, 5, -1],
     [-1, 1, 5, -1, 3],
     [1, -1, -1, 3, -1]]
LEN = 7

GG = deepcopy(G)
cycle = min_cycle(GG)

print("Cykl :", cycle)

if cycle == []:
    print("Błąd (1): Spodziewano się cyklu!")
    exit(0)

L = 0
u = cycle[0]
for v in cycle[1:] + [u]:
    if G[u][v] == -1:
        print("Błąd (2): To nie cykl! Brak krawędzi ", (u, v))
        exit(0)
    L += G[u][v]
    u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
    print("Błąd (3): Niezgodna długość")
else:
    print("OK")
