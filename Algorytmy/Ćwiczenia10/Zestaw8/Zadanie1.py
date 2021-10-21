from collections import deque


E =[[1, 2, 3], [0, 2, 6, 7], [0, 1, 3, 5, 8], [0, 2, 5, 4], [3, 5, 9], [4, 2, 3, 8], [1, 7], [1, 9], [2, 5, 9], [4, 7, 8]]


class Vertex():
    def __init__(self):
        self.visited = False
        self.color = None




def ColorVertices(E):
    n = len(E)
    G = [Vertex() for _ in range(n+1)]

    Q = deque()
    G[0].visited = 0
    G[0].color = 0
    Q.append(0)
    max_c = 0

    while len(Q):
        u = Q.pop()
        if max_c < len(E[u]) + 1:
            max_c = len(E[u]) + 1

        C = [0]*max_c
        C[G[u].color] = 1

        for el in E[u]:
            if G[el].visited == False:
                G[el].visited = True
                Q.append(el)
            if G[el].color == None:
                color = 0
                while color < len(E[u]) + 1:
                    if C[color] == 0:
                        G[el].color = color
                        C[color] = 1
                        break
                    color += 1

            else:
                C[G[el].color] = 1

    return G[7].color

print(ColorVertices(E))