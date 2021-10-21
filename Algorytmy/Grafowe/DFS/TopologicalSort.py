E = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2], [3]]

G = [[2, 3], [0], [1], [4], [0]]

class Vertex():
    def __init__(self):
        self.d = 0
        self.f = 0
        self.p = None
        self.visited = False

def DFS(E):
    n = len(E)
    V = [Vertex() for _ in range(n)]
    SortedVertices = []
    global time
    time = 0

    def DFSVisit(V, E, u):
        global time
        time += 1
        V[u].d = time
        V[u].visited = 1
        for el in E[u]:
            if V[el].visited == 0:
                V[el].p = u
                DFSVisit(V, E, el)

        time += 1
        V[u].f = time
        SortedVertices.append(u)

    for i in range(n):
        if V[i].visited == False:
            DFSVisit(V, E, i)

    return SortedVertices

print(DFS(G))