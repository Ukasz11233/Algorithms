E = [[1, 2, 3], [2], [], [0, 2]]

def MotherVertex(E):
    n = len(E)
    visited = [False]*n
    processed = [0]*n
    global time
    time = 0

    def DFSVisit(E, u):
        global time
        time += 1
        visited[u] = True

        for el in E[u]:
            if visited[el]  == False:
                DFSVisit(E, el)

        time += 1
        processed[u] = time



    for i in range(n):
        if visited[i] == False:
            DFSVisit(E, i)

    maxi = -1
    for i in range(n):
        if maxi < processed[i]:
            maxi = processed[i]
            idx = i

    visited = [False]*n
    DFSVisit(E, idx)
    for el in visited:
        if el == False:
            return None

    return idx




print(MotherVertex(E))