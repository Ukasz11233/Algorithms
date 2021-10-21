from queue import PriorityQueue

G = [[(1, 10), (2, 5)],
     [(0, 10), (3, 3), (4, 7)],
     [(0, 5), (4, 4)],
     [(1, 3), (4, 1), (5, 7)],
     [(2, 4), (1, 7), (3, 1), (5, 2)],
     [(3, 7), (4, 2)]
     ]

G1 = [[(1, 5), (2, 2)],
      [(0, 5), (2, 4), (3, 2), (4, 6)],
      [(0, 2), (1, 4), (4, 3)],
      [(1, 2), (4, 1), (5, 3)],
      [(2, 3), (1, 6), (3, 1), (5, 5)],
      [(3, 3), (4, 5)]
      ]
V = [3, 6, 5, 4, 2, 9]


def Relax(cost, fuel, parent, u, v, w, tmp_cost):
    if cost[v] > cost[u] + tmp_cost:
        cost[v] = cost[u] + tmp_cost
        parent[v] = u
        fuel[v] = fuel[u] - w


def PrintResult(parent, i):
    if parent[i] == None:
        print(i, end=" ")
        return
    PrintResult(parent, parent[i])
    print(i, end=" ")


def GasStation(G, V, D):
    n = len(G)
    parent = [None] * n
    visited = [False] * n
    cost = [float("inf")] * n
    fuel = [0] * n
    Q = PriorityQueue()

    Q.put((0, 0))
    cost[0] = 0
    fuel[0] = D

    while not Q.empty():
        u = Q.get()[1]
        visited[u] = True

        for el in G[u]:
            v, w = el[0], el[1]
            if visited[v] == False and w <= D:
                if fuel[u] >= w:
                    Relax(cost, fuel, parent, u, v, w, 0)
                else:
                    tmp_fuel = fuel[u]
                    tmp_cost = (w - fuel[u]) * V[u]
                    fuel[u] = w
                    Relax(cost, fuel, parent, u, v, w, tmp_cost)
                    fuel[u] = tmp_fuel

                Q.put((cost[v], v))
    PrintResult(parent, n - 1)
    return cost, fuel, parent


print(GasStation(G, V, 5))


