A = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
B = ['B', 'D', 'C', 'A', 'B', 'A']

def PrintLCS(D, A, i, j):
    if i == -1 or j == -1:
        return
    if D[i][j] == 2:
        PrintLCS(D, A, i-1, j-1)
        print(A[i])
    elif D[i][j] == 1:
        PrintLCS(D, A, i-1, j)
    else:
        PrintLCS(D, A, i, j-1)

def LCS_Length(A, B):
    C = [[-1 for i in range(len(B)+1)]for j in range(len(A)+1)]
    D = [[-1 for i in range(len(B))]for j in range(len(A))]
    for i in range(1, len(A)+1):
        C[i][0] = 0
    for j in range(len(B)+1):
        C[0][j] = 0
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                C[i][j] = C[i-1][j-1] + 1
                D[i-1][j-1] = 2  #strzalka na ukos
            elif C[i-1][j] >= C[i][j-1]:
                C[i][j] = C[i-1][j]
                D[i-1][j-1] = 1  #strzalka do gory
            else:
                C[i][j] = C[i][j-1]
                D[i-1][j-1] = 3  #strzalka w lewo

    return PrintLCS(D, A, len(A)-1, len(B)-1)



print(LCS_Length(A, B))
