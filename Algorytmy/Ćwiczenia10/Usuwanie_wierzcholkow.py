from queue import Queue

E = [[1, 4], [0, 2], [1, 3, 4], [2, 5, 6], [0, 2, 7], [3, 6], [3, 5], [4]]


class Vertex():
    def __init__(self):
        self.d = None
        self.visited = False
        self.p = None


def DFS(E):
    n = len(E)
    V = [Vertex() for _ in range(n)]
    global time
    time = 0
    to_delete = Queue()

    def DFSVisit(V, E, u):

        V[u].visited = True
        global time
        time +=1
        V[u].d = time

        for el in E[u]:
            if V[el].visited == False:
                V[el].p = u
                DFSVisit(V, E, el)
        E[u] = []
        to_delete.put(u)

    for i in range(n):
        if V[i].visited == False:
            DFSVisit(V, E, i)
    while not to_delete.empty():
        v = to_delete.get()
        V[v] = None

    return E, V

print(DFS(E))

