A = [0, 5, 7, 10, 12, 15, 20]

def parent(i):
    return (i-1)//2

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def Build_tree(A):
    n = len(A)
    T = [0]*(2*n)
    for i in range(n):
        T[i+n] = A[i]


    F = [[]*(2*n)]

    return T
print(Build_tree(A))
