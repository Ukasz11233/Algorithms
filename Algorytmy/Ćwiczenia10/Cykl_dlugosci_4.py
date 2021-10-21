E = [[1, 3, 4, 5], [0, 2],[1, 3, 6], [2, 4, 5], [0, 3], [0, 3], [2]]

E2 = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]

def FindCycle4(E):
    n = len(E)
    A = [[0]*n for _ in range(n)]
    for i in range(n):
        first, second = None, None
        for j in range(n):
            if E[i][j] == 1 and first == None:
                first = j
            elif E[i][j] == 1 and first != None and second == None:
                second = j
            if first != None and second != None:
                if A[first][second] > 0:
                    print(i, first, second, A)
                    return True
                else:
                    A[first][second] = 1
                    first = None
                    second = None
    return False


print(FindCycle4(E2))