from queue import PriorityQueue

G = [[(1, 16), (2, 13)],
     [(3, 12)],
     [(1, 4), (4, 14)],
     [(2, 9), (5, 20)],
     [(3, 7), (5, 4)],
     []]

class Node:
    def __init__(self, v = None):
        self.v = v
        self.f = []



def Increase_Flow(V, parent, min_cost, t):
    if parent[t] == -1:
        return
    Increase_Flow(V, parent, min_cost, parent[t])
    for i in range(len(V[parent[t]].f)):
        if V[parent[t]].f[i][0] == t:
            V[parent[t]].f[i][1] += min_cost



def BFS(V, G, parent, s, t, n):
    visited = [False]*n
    dist = [float("inf")]*n
    Q = PriorityQueue()
    d = 0
    flow = float("inf")
    Q.put(s)

    dist[s] = 0
    visited[s] = True
    parent[s] = -1

    while not Q.empty():
        u = Q.get()
        d += 1
        for i in range(len(V[u].f)):
            v = V[u].f[i][0]
            w = V[u].f[i][1]

            if visited[v] == False and w < G[u][i][1]:
                visited[v] = True
                parent[v] = u
                flow = min(flow, G[u][i][1] - w)
                dist[v] = d
                if v == t:
                    return flow
                Q.put(v)

    return 0



def Edmonds_Karp(G, s, t):
    n = len(G)
    parent = [None]*n
    V = []
    for i in range(n):
        V.append(Node(i))
        for el in G[i]:
            V[i].f.append([el[0], 0])
    flow = 0
    new_flow = BFS(V, G, parent, s, t, n)

    while new_flow:
        flow += new_flow
        Increase_Flow(V, parent, new_flow, t)
        new_flow = BFS(V, G, parent, s, t, n)

    print(V[0].f)
    return flow



print(Edmonds_Karp(G, 0, 5))
