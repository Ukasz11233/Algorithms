E = [[1, 2], [0, 2], [0, 1]]

def CheckUndirected(E):
    n = len(E)
    A = [[0]*n for _ in range(n)]
    for i in range(n):
        for el in E[i]:
            A[i][el] = 1

    for i in range(n):
        for el in E[i]:
            if A[el][i] == 0:
                return False
    return True

print(CheckUndirected(E))
