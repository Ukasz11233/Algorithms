from queue import PriorityQueue


G = [[-1, 6,-1, 5, 2],
[-1,-1, 1, 2,-1],
[-1,-1,-1,-1,-1],
[-1,-1, 4,-1,-1],
[-1,-1, 8,-1,-1]]

P = [0,1,3]


def Relax(dist, parent, fuel_left, P, u, v, w, d):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        parent[v] = u
        for i in range(len(P)):
            if P[i] == v:
                fuel_left[v] = d
                return
        fuel_left[v] = fuel_left[u] - w


def PrintResult(parent, t, result):
    if parent[t] == None:
        return None
    if parent[t] == -1:
        result.append(t)
        return result
    PrintResult(parent, parent[t], result)
    result.append(t)
    return result


def jak_dojade(G, P, d, a, b):
    n = len(G)
    visited = [False]*n
    fuel_left =[0]*n
    dist = [float("inf")]*n
    parent = [None]*n

    Q = PriorityQueue()
    Q.put((0, a))
    dist[a] = 0
    fuel_left[a] = d
    parent[a] = -1

    while not Q.empty():
        u = Q.get()[1]
        visited[u] = True

        for i in range(n):
            if G[u][i] > 0:
                if visited[i] == False and G[u][i] <= fuel_left[u]:
                    Relax(dist, parent, fuel_left, P, u, i, G[u][i], d)
                    Q.put((dist[i], i))
    result = []
    result = PrintResult(parent, b, result)
    return result

print(jak_dojade(G, P, 5, 0, 2))