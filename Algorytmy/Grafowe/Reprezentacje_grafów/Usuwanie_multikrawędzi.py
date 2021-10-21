E = [[1, 1, 2], [1, 3], [0, 3], [2, 2]]

def DeleteMultiedges(E):
    n = len(E)
    V = [0]*n
    ET = [[] for _ in range(n)]
    for i in range(n):
        for el in E[i]:
            if el != i and V[el] == 0:
                ET[i].append(el)
                V[el] = 1
        V = [0]*n

    return ET

print(DeleteMultiedges(E))