E = [[3], [0, 2], [1, 3], [2]]

def DFSCycle(E):
    n = len(E)
    visited = [0] * n
    parent = [0] * n

    def DFSVisit(E, u):
        visited[u] = 1
        for v in E[u]:
            if visited[v] == 0:
                parent[v] = u
                DFSVisit(E, v)
            elif visited[v] == 1 and parent[u] != v:
                
                return True

    for i in range(n):
        if visited[i] == 0:
            result = DFSVisit(E, i)
            if result == True:
                return True

    return False
print(DFSCycle(E))