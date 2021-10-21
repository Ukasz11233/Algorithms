M1 = [[0, 1, 1, 0],
      [1, 0, 1, 0],
      [1, 1, 0, 1],
      [0, 0, 1, 0]]



def DFS(G):
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    articulation = [0]*n

    def DFSVisit(G, u, n):
        visited[u] = True

        for i in range(n):
            if visited[i] == False and G[u][i] == 1:
                articulation[u] += 1
                parent[i] = u
                DFSVisit(G, i, n)

    for i in range(n):
        if visited[i] == False:
            DFSVisit(G, i, n)
    for i in range(n):
        if parent[i] != None:
            articulation[i] += 1

    return articulation

print(DFS(M1))