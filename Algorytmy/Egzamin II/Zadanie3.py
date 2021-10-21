T = [ [0,2,1,1], [1,0,1,1], [2,2,0,1], [2,2,2,0] ]


class Vertex():
    def __init__(self):
        self.visited = False
        self.p = None
        self.f = 0


def tasks(T):
    n = len(T)
    G = [Vertex() for _ in range(n)]
    global time
    time = 0
    result = []

    def DFSVisit(G, u):
        global time
        G[u].visited = True
        time += 1

        for i in range(n):
            if T[u][i] == 1 and G[i].visited == False:
                DFSVisit(G, i)

        time += 1
        G[u].f = time
        result.append(u)

    for i in range(n):
        if G[i].visited == False:
            DFSVisit(G, i)


    for i in range(n//2):
        result[i], result[n-i-1] = result[n-i-1], result[i]

    return result

print(tasks(T))