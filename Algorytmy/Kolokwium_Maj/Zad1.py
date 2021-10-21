import copy
from zad1testy import runtests
T = [ (2, 1, 5, 3),
(3, 7, 9, 2),
(2, 8, 11, 1) ]
p = 5



def Students(A, i):
    return (A[i][2]-A[i][1])*A[i][0]


def Prev(A, i):
    if i == 0:
        return 0
    else:
        for j in range(i, -1, -1):
            if A[j][2] < A[i][1]:
                return j
        return i


def PrintResult(A, R, i, j, result):
    if i == 0:
        result.append(A[i][4])
        return result
    PrintResult(A, R, R[i][j][0], R[i][j][1], result)
    result.append(A[i][4])
    return result


def select_buildings(T, p):
    n = len(T)
    F = [[0]*(p+1) for _ in range(n)]
    R = [[(0, 0)]*(p+1) for _ in range(n)]


    A = [[] for _ in range(n)]
    for i in range(n):
        A[i].append(T[i][0])
        A[i].append(T[i][1])
        A[i].append(T[i][2])
        A[i].append(T[i][3])
        A[i].append(i)

    A = sorted(A, key=lambda x: x[2])
    for i in range(p+1):
        if i >= T[0][3]:
            F[0][i] = Students(A, 0)


    for i in range(1, n):
        for j in range(p+1):
            q = F[i-1][j]

            if j >= A[i][3]  and Prev(A, i) != i and  q < F[Prev(A, i)][j - A[i][3]] + Students(A, i):
                F[i][j]= F[Prev(A, i)][j - A[i][3]] + Students(A, i)
                R[i][j] = (Prev(A, i), j - A[i][3])
            else:
                F[i][j] = q
                R[i][j] = R[i-1][j]

    max_ = -1
    idx = 0
    result = []
    for i in range(n):
        for j in range(p+1):
            if F[i][j] >= max_:
                idx = (i, j)
                max_ = F[i][j]
    print(idx, max_)
    result = PrintResult(A, R, idx[0], idx[1], result)
    result.sort()
    print(F)
    print(R)
    return result

P2 = ([(8,2,6,2),(9,4,8,5),(9,8,9,2),(3,10,15,1),],7)
R2 = [0,2,3]

P3=([(7,23,24,1),(2,10,14,3),(7,17,22,1),(9,20,22,2),(4,19,22,8),(2,2,6,1)],10)
R3=[0,1,2,5]

P4=([(1,8,12,5),(4,7,8,2),(3,2,3,6),(9,7,8,5),(8,21,22,8),(5,4,7,10),(1,21,24,10),(7,14,16,1)],32)
R4=[0,2,4,5,7]


print(select_buildings(P3[0], 10))
#runtests(select_buildings)
K = sorted(P2[0], key = lambda x: x[2])
print(K)