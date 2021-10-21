V = [[1, 2], [0, 3], [0, 3, 4], [1, 2, 5], [2, 5], [3, 4, 6], [5, 7], [6]]


def DFS(V):
    n = len(V)
    visited = [0]*n
    parent = [0]*n
    global time
    time = 0

    def DFSVisit(V, u):
        print("krawdz w przod:", parent[u], u)
        global time
        time += 1
        visited[u] = 1
        for v in V[u]:
            if visited[v] == 0:
                parent[v] = u
                DFSVisit(V, v)
            else:
                print("krawedz powrotna:", u, v)
        time += 1
        print("krawedz drzewowa:", u, parent[u])

    for i in range(n):
        if visited[i] == 0:
            DFSVisit(V, i)
    print(parent)
    return time

print(DFS(V))


def DFSWithStack(V):
    n = len(V)
    visited = [0]*n
    stack = []
    parent_stack = []
    time = 0
    for i in range(n):
        if visited[i] == 0:
            stack.append(i)
            while len(stack) > 0:
                v = stack.pop()
                visited[v] = 1

                for el in V[v]:
                    if visited[el] == 0:
                        parent_stack.append(v)
                        stack.append(el)
                        break
                time += 1

            time += 1
            while len(parent_stack) > 0:
                v = parent_stack.pop()
                time += 1
                print(v)

    return time

