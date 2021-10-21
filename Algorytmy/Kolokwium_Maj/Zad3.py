from queue import PriorityQueue

from zad3testy import runtests

T = [
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]


def DFS(T, n, m):
    visited = [[False]*n for _ in range(m)]
    result = 0
    array = [0]*n

    def DFS_utility(T, row, column):
        visited[row][column] = True
        result = 0

        if column + 1 < n and T[row][column+1] > 0 and visited[row][column+1] == False:
            result += DFS_utility(T, row, column+1)
        if column - 1 >= 0 and T[row][column-1] > 0 and visited[row][column-1] == False:
            result += DFS_utility(T, row, column-1)
        if row + 1 < n and T[row+1][column] > 0 and visited[row+1][column] == False:
            result += DFS_utility(T, row+1, column)
        if row - 1 >= 0 and T[row-1][column] > 0 and visited[row-1][column] == False:
            result += DFS_utility(T, row-1 ,column)

        return result + T[row][column]

    for i in range(n):
        if visited[0][i] == False and T[0][i] > 0:
            array[i] = DFS_utility(T, 0, i)

    return array

def plan(T):
    m = len(T)
    n = len(T[0])
    array = DFS(T, n, m)
    Q = PriorityQueue()

    for i in range(1, n):
        if array[i] > 0:
            Q.put((-array[i], i))

    print(array)
    result = [0]
    dist = array[0]

    while not Q.empty():
        el = Q.get()
        dist -= el[0]
        result.append(el[1])
        if dist >= n-1:
            result.sort()
            return result

    return result

#print(plan(T))
runtests(plan)