A = [5, 4, 2, 11, 9, 6]
#             ij       pivot = 6

def partiton(A, low, high):
    pivot = A[low]
    i = low-1
    j = high+1
    while True:
        i+=1
        while A[i] < pivot:
            i+=1

        j-=1
        while A[j] > pivot:
            j-=1
        if i >= j:
            return A, j
        A[i], A[j] = A[j], A[i]

print(partiton(A, 0, len(A)-1))