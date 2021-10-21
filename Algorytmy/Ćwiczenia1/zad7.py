A = [1, 2, 3, 4, 10, 11]

def FindIdx(A, x):
    i = 0
    j = len(A)-1
    while i <= j:
        if A[i] + A[j] < x:
            i += 1
        elif A[i] + A[j] > x:
            j -=1
        else:
            return i, j

print(FindIdx(A, 7))
