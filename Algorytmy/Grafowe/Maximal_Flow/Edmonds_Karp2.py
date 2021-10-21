from queue import PriorityQueue

G = [[(1, 16), (2, 13)],
     [(3, 12)],
     [(1, 4), (4, 14)],
     [(2, 9), (5, 20)],
     [(3, 7), (5, 4)],
     []]


def BFS(G, capacity, parent, s, t, n):
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
        for el in G[u]:
            v = el[0]
            max_capacity = el[1]
            if visited[v] == False and capacity[u][v] < max_capacity:
                visited[v] = True
                parent[v] = u
                flow = min(flow, max_capacity - capacity[u][v])
                dist[v] = d
                if v == t:
                    return flow
                Q.put(v)

    return 0

def Increase_Flow(capacity, parent, flow, s, t):
    if t == s:
        return
    Increase_Flow(capacity, parent, flow, s, parent[t])
    capacity[parent[t]][t] += flow

def Edmonds_Karp(G, s, t):
    n = len(G)
    capacity = [[0]*n for _ in range(n)]
    parent = [None]*n
    flow = 0

    new_flow = BFS(G, capacity, parent, s, t, n)

    while new_flow:
        flow += new_flow
        Increase_Flow(capacity, parent, new_flow, s, t)
        new_flow = BFS(G, capacity, parent, s, t, n)
        

    return capacity

#print(Edmonds_Karp(G, 0, 5))