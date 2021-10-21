from queue import Queue

V = [[1, 2], [0, 3], [0, 3, 4], [1, 2, 5], [2, 5], [3, 4, 6], [5, 7], [6]]
V1 = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]

def BFS(V):
    n = len(V)
    visited = [0]*n
    colors = [0]*n
    Q = Queue()
    visited[0] = 1

    Q.put(0)

    while not Q.empty():
        u = Q.get()
        for el in V[u]:
            if visited[el] == False:
                visited[el] = True
                if colors[u] == 0:
                    colors[el] = 1
                else:
                    colors[el] = 0
                Q.put(el)
    for i in range(n):
        for el in V[i]:
            if colors[i] == colors[el]:
                return False

    return True

print(BFS(V1))