from queue import Queue

V = [[1, 2], [0, 3], [0, 3, 4], [1, 2, 5], [2, 5], [3, 4, 6], [5, 7], [6]]
V1 = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]

V2 = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2], [3]]


class Vertex:
    def __init__(self):
        self.d = float("inf")
        self.visited = False
        self.prev = None
        self.adj = []


def BFS(V):
    n = len(V)
    G = [Vertex() for _ in range(n)]
    for i in range(n):
        G[i].adj = V[i]

    Q = Queue()
    G[0].d = 0
    G[0].visited = True

    Q.put(G[0])

    while not Q.empty():
        tmp = Q.get()
        for el in tmp.adj:
            if G[el].visited == False:
                G[el].visited = True
                G[el].prev = tmp
                G[el].d = tmp.d + 1
                Q.put(G[el])

    return G[7].d

print(BFS(V))

