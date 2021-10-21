A = [14, 3, 5.2, 12, 11,gra planoszwa statki 9, 1, 2, 5.2]

def InsertionSort(A): # stabilny
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j >= 0 and int(A[j]) > int(key):
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A

print(InsertionSort(A))