A = [14, 2.1, 53, 23, 11, 5, 7, 1, 2.2]

def SelectionSort(A): # niestabilny
    for i in range(len(A)):
        min = i
        for j in range(i, len(A)):
            if int(A[j]) < int(A[min]):
                min = j
        A[i], A[min] = A[min], A[i]
    return A

print(SelectionSort(A))