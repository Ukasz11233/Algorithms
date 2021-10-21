E =[[0, 6, 0, 0, 0, 0, 0],
    [6, 0, 5, 0, 0, 0, 0],
    [0, 5, 0, 4, 2, 3, 0],
    [0, 0, 4, 0, 0, 0, 1],
    [0, 0, 2, 0, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]]


def FindRoute(E, x, y):
    n = len(E)
    visited = [False]*n

    def DFSVisited(E, u, w, y):

        visited[u] = True
        print(u)
        if u == y:
            return True
        result = False

        for i in range(n):
            if visited[i] == False and E[u][i] > 0 and E[u][i] < w:

                result = DFSVisited(E, i, E[u][i], y)
                break

        return result

    return DFSVisited(E, x, float("inf"), y)

print(FindRoute(E, 0, 6))