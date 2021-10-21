from queue import PriorityQueue

G = [[(1, 10), (2, 5)],
     [(0, 10), (2, 2), (3, 1)],
     [(0, 5), (1, 2), (3, 9), (4, 4)],
     [(1, 1), (2, 9), (4, 6), (5, 5)],
     [(2, 4), (3, 6), (5, 3)],
     [(3, 5), (4, 3)]]


G2 = [[(1,4), (2,3)], # 0
[(3,2)], # 1
[(3,5)], # 2
[]] # 3


def PrintPath(parent, t):
    if parent[t] == -1:
        print(t, end=" ")
        return
    PrintPath(parent, parent[t])
    print(t, end=" ")


def Tourist_Guide_P(G, s, t):
    n = len(G)
    visted = [False]*n
    dist = [-float("inf")]*n
    parent = [None]*n
    Q = PriorityQueue()

    Q.put((0, s))

    dist[s] = 0
    parent[s] = -1
    while not Q.empty():
        u = Q.get()[1]
        visted[u] = True
        for el in G[u]:
            v = el[0]
            w = el[1]
            if visted[v] == False:
                if dist[v] < w:
                    parent[v] = u
                    dist[v] = w
                    Q.put((-dist[v], v))

    PrintPath(parent, n-1)
    return parent, dist

print(Tourist_Guide_P(G, 0, 5))


class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.rank = 0


def Find(x):
    if x != x.parent:
        x.parent = Find(x.parent)
    return x.parent


def Union(x, y):
    x = Find(x)
    y = Find(y)
    if x == y:
        return

    if x.rank > y.rank:
        y.parent = x

    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def Kruskal(G):
    n = len(G)
    E = []
    for i in range(n):
        for el in G[i]:
            E.append((i, el[0], el[1]))

    E = sorted(E, key=lambda x: x[2])

    A = []
    for i in range(n):
        A.append(Node(i))

    n = len(E)
    result = [E[n-1]]
    Union(A[E[n-1][0]], A[E[n-1][1]])

    for i in range(n-1, -1, -1):
        u = E[i][0]
        v = E[i][1]
        if Find(A[u]) != Find(A[v]):
            Union(A[u], A[v])
            result.append(E[i])

    return result

#print(Kruskal(G))