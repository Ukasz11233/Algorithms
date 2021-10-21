M1 = [[0, 1, 1, 0],
      [1, 0, 1, 0],
      [1, 1, 0, 1],
      [0, 0, 1, 0]]

M3 = [[0, 1, 1],
      [1, 0, 1],
      [1, 1, 0]]

from zad2testy import runtests

def breaking(G):
    n = len(G)
    visited = [False] * n
    deleted = [False] * n

    def DFSVisit(G, u, n):
        visited[u] = True
        for v in range(n):
            if G[u][v] == 1 and visited[v] == False and deleted[v] == False:
                DFSVisit(G, v, n)


    result_counter = -float("inf")
    result = None
    for el in range(n):
        deleted[el] = True
        counter = 0
        for i in range(n):
            if visited[i] == False and deleted[i] == False:
                DFSVisit(G, i, n)
                counter += 1

        if counter > result_counter and counter > 1:
            result_counter = counter
            result = el
        deleted[el] = False
        for j in range(n):
            visited[j] = False

    return result




runtests(breaking)