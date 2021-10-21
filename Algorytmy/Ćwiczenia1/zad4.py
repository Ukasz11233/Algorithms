A = [1, 5, 3, 11, 4, 12, 6]

def FindMinMAx(A):
    max = A[0]
    min = A[0]
    i = len(A) % 2
    while i < len(A):
        if A[i] < A[i+1]:
            if A[i] < min:
                min = A[i]
            if A[i+1] > max:
                max = A[i+1]
        else:
            if A[i] > max:
                max = A[i]
            if A[i+1] < min:
                min = A[i+1]
        i += 2
    return max, min

print(FindMinMAx(A))