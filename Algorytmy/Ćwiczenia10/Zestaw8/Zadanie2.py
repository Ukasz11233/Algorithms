from collections import deque

E = [[1, 3], [0, 2], [1, 3], [0, 4], [3, 5], [4, 6, 8], [5, 7], [6, 8], [5, 7]]


class Vertex():
    def __init__(self, n):
        self.p = None
        self.v = False
        self.shortest = [0 for _ in range(n)]
        self.d = 0
        self.path = [[] for _ in range(n)]

def ShortestPath(E):
    Q = deque()
    n = len(E)
    G = [Vertex(n) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            G[j].v = False
            G[j].d = 0
        G[i].v = True
        G[i].path[i].append(i)
        Q.append(i)

        while len(Q):
            u = Q.pop()
            for el in E[u]:
                if G[el].v == False:
                    G[el].v = True
                    G[el].d = G[u].d + 1
                    G[el].p = u
                    Q.append(el)
                    G[i].shortest[el] = G[u].d + 1
                    G[i].path[el].append(el)
                    G[i].path[el] += G[i].path[u]
                    print(el)

    return G[2].path[7]

print(ShortestPath(E))