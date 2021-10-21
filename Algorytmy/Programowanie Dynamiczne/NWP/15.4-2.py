A = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
B = ['B', 'D', 'C', 'A', 'B', 'A']

def PrintLCS(C, A, i, j):
    if i == 0 or j == 0:
        return
    if C[i-1][j] < C[i][j] and C[i][j-1] < C[i][j]:  #strzalka na ukos
        PrintLCS(C, A, i-1, j-1)
        print(A[i-1])
    elif C[i-1][j] < C[i][j] and C[i][j-1] == C[i][j]:  #stzalka w lewo
        PrintLCS(C, A, i, j-1)
    else:                                                #strzalka w gore
        PrintLCS(C, A, i-1, j)

def LCS_Length(A, B):
    C = [[-1 for i in range(len(B)+1)]for j in range(len(A)+1)]
    for i in range(1, len(A)+1):
        C[i][0] = 0
    for j in range(len(B)+1):
        C[0][j] = 0
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                C[i][j] = C[i-1][j-1] + 1
            elif C[i-1][j] >= C[i][j-1]:
                C[i][j] = C[i-1][j]
            else:
                C[i][j] = C[i][j-1]

    return PrintLCS(C, A, len(A), len(B))



print(LCS_Length(A, B))
