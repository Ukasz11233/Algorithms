E = [[1, 2], [3], [1], [2]]

def TransList(E):
    n = len(E)
    ET = [[] for _ in range(n)]

    for i in range(n):
        for el in E[i]:
            ET[el].append(i)

    return ET

print(TransList(E))

M = [[0, 1, 1, 0], [0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0]]


def TransMatrix(M):
    n = len(M)
    MT = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if M[i][j] == 1:
                MT[j][i] = 1
    return MT
print(TransMatrix(M))