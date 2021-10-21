from queue import Queue

V = [[1, 2], [0, 3], [0, 3, 4], [1, 2, 5], [2, 5], [3, 4, 6], [5, 7], [6]]


def BFS(V):
    n = len(V)
    visited = [False for _ in range(n)]
    distance = [float("inf") for _ in range(n)]
    Q = Queue()
    visited[0] = True
    distance[0] = 0
    Q.put(0)

    while not Q.empty():
        tmp = Q.get()
        for el in V[tmp]:
            if visited[el] == False:
                visited[el] = True
                distance[el] = distance[tmp] + 1
                Q.put(el)

    maxidx, max_dist = 0, -1
    for i in range(n):
        if distance[i] > max_dist:
            maxidx = i
            max_dist = distance[i]


    visited = [False for _ in range(n)]
    distance = [float("inf") for _ in range(n)]
    distance[maxidx] = 0
    visited[maxidx] = True
    Q.put(maxidx)

    while not Q.empty():
        tmp = Q.get()
        for el in V[tmp]:
            if visited[el] == False:
                visited[el] = True
                distance[el] = distance[tmp] + 1
                Q.put(el)

    return max(distance)

print(BFS(V))