A = [4, 2, 6, 3, 10, 32, 64, 34, 23, 11, 65, 8]

def Partition(A, low, high):
    i = (low-1)
    pivot = A[high]

    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[high] = A[high], A[i+1]
    return (i+1)

def QuickSort(A,low, high):
    if len(A) == 1:
        return A
    if low < high:
        p = Partition(A, low, high)
        QuickSort(A, low, p-1)
        QuickSort(A, p+1, high)
    return A

def QuickSort2(A, low, high):   #quickosrt z pamiecia O(logn)
    if len(A) == 1:
        return A
    while low < high:
        p = Partition(A, low, high)
        if p - low < high - p:
            QuickSort2(A, low, p-1)
            low = p+1
        else:
            QuickSort2(A, p+1, high)
            high = p-1
    return A

print(QuickSort2(A, 0, 11))