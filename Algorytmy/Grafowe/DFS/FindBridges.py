E = [[1, 4], [0, 2], [1, 3, 4], [2, 5, 6], [0, 2, 7], [3, 6], [3, 5], [4]]

class Vertex():
    def __init__(self):
        self.low = None
        self.d = None
        self.child = None
        self.visited = False
        self.p = None


def FIndBridges(E):
    n = len(E)
    V = [Vertex() for _ in range(n)]
    time = 0
    Bridges = []


    def Low(V, E, v):
        child_low, back_edge =float("inf"), float("inf")
        if V[v].child is not None:
            child_low = V[V[v].child].low
        for el in E[v]:
            if V[el].visited == True and V[v].p != el:
                if back_edge > V[el].low:
                    back_edge = V[el].low
        return min(V[v].d, child_low, back_edge)


    def DFSVisit(V, E, u):
        V[u].visited = True
        nonlocal time
        time += 1
        V[u].d = time
        V[u].low = V[u].d
        back_edge = float("inf")
        for el in E[u]:
            if V[el].visited == False:
                V[el].p = u
                V[u].child = el
                DFSVisit(V, E, el)

        V[u].low = Low(V, E, u)
        if V[u].low == V[u].d and V[u].p is not None:
            Bridges.append((V[u].p, u))


    for i in range(n):
        if V[i].visited == False:
            DFSVisit(V, E, i)

    for i in range(n):
        print(V[i].low, end=" ")

    return Bridges

print(FIndBridges(E))