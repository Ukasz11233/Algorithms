E = [[1], [2, 4, 5], [3, 6], [2, 7], [0, 5], [6], [5, 7], [7]]

E2 = [[1, 2, 3], [2], [], [0, 2]]

class Vertex():
    def __init__(self):
        self.d = 0
        self.f = 0
        self.p = None
        self.visited = False

def DFS(E):
    n = len(E)
    V = [Vertex() for _ in range(n)]
    Sorted = []
    time = 0

    def DFSVisit(V, E, u):
        nonlocal time
        time += 1
        V[u].d = time
        V[u].visited = 1
        print(u, time)
        for el in E[u]:
            if V[el].visited == 0:
                V[el].p = u
                DFSVisit(V, E, el)

        time += 1
        V[u].f = time
        Sorted.append(u)


    for i in range(n):
        if V[i].visited == False:
            DFSVisit(V, E, i)

    return V, Sorted


def TransList(E):
    n = len(E)
    ET = [[] for _ in range(n)]

    for i in range(n):
        for el in E[i]:
            ET[el].append(i)

    return ET



def SCC(E):
    n = len(E)
    V, Topological_Sorted = DFS(E)
    ET = TransList(E)
    print(ET)

    VT = [Vertex() for _ in range(n)]
    time = 0

    def DFSVisit(V, E, u, idx):
        nonlocal time
        time += 1
        V[u].d = time
        V[u].visited = 1
        for el in E[u]:
            if V[el].visited == 0:
                V[el].p = u
                DFSVisit(V, E, el, idx)
        SCC_array[idx].append(u)
        time += 1
        V[u].f = time

    idx = 0
    SCC_array = []
    for i in range(n-1, -1, -1):
        if VT[Topological_Sorted[i]].visited == False:
            SCC_array.append([])
            DFSVisit(VT, ET, Topological_Sorted[i], idx)
            idx += 1

    return SCC_array

print(SCC(E2))