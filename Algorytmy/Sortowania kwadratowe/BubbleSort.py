A = [4.1, 52, 34, 11, 12, 36, 5, 1, 4.2]

def BubbleSort(A): # stabilny
    for i in range(len(A)):
        for j in range(len(A)-1, i, -1):
            if int(A[j]) < int(A[i]):
                A[j], A[i] = A[i], A[j]
    return A

print(BubbleSort(A))
