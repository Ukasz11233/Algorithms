A = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
B = ['B', 'D', 'C', 'A', 'B', 'A']

def AuxTopDown(A, B, C, i, j):
    if C[i][j] > -1:
        return C[i][j], C
    if i == len(A) or j == len(B):
        return 0, C
    if A[i] == B[j]:
        q =  AuxTopDown(A, B, C, i+1, j+1)[0] + 1
    else:
        q = max(AuxTopDown(A, B, C, i+1, j)[0], AuxTopDown(A, B, C, i, j+1)[0])
    C[i][j] = q
    return q, C


def TopDown(A, B):
    C = [[-1 for i in range(len(B)+1)] for i in range(len(A)+1)]
    for i in range(len(A)+1):
        C[i][len(B)] = 0
    for j in range(len(B)+1):
        C[len(A)][j] = 0
    print(C)
    return AuxTopDown(A, B, C, 0, 0)[1]

print(TopDown(A, B))