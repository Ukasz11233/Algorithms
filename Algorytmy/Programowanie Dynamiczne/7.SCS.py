A = "ABCBDAB"
B = "BDCABA"
L = [[float("inf") for i in range(len(B)+1)]for i in range(len(A)+1)]
S = [[0 for i in range(len(B))] for i in range(len(A))]

def SCS(A, B, L,  idxA, idxB):
    if idxA == 0 or idxB == 0:
        return idxA + idxB

    if L[idxA-1][idxB-1] < float("inf"):
        S[idxA - 1][idxB - 1] = B[idxB]
        return L[idxA-1][idxB-1]

    if A[idxA-1] == B[idxB-1]:
        q =  SCS(A, B, L, idxA - 1, idxB -1) + 1
        S[idxA - 1][idxB - 1] = A[idxA - 1]
    else:
        q1 = SCS(A, B, L, idxA - 1, idxB) + 1
        q2 = SCS(A, B, L, idxA, idxB - 1) + 1
        if q1 > q2:
            S[idxA - 1][idxB - 1] = B[idxB - 1]
            q = q2
        else:
            S[idxA - 1][idxB - 1] = A[idxA - 1]
            q = q1
    L[idxA - 1][idxB - 1] = q
    return L[idxA-1][idxB-1]


print(SCS(A, B, L, len(A), len(B)))

def SCS_Display(A, B, L, idxA, idxB):
    if idxA == 0:
        return B[:idxB]
    if idxB == 0:
        return A[:idxA]
    if A[idxA - 1] == B[idxB - 1]:
        return SCS_Display(A, B, L, idxA -1, idxB - 1) + A[idxA - 1]
    else:
        if L[idxA - 1][idxB] < L[idxA][idxB - 1]:
            return SCS_Display(A, B, L, idxA - 1, idxB) + A[idxA - 1]
        else:
            return SCS_Display(A, B, L, idxA, idxB - 1) + B[idxB - 1]


print(SCS_Display(A, B, L, len(A), len(B)))