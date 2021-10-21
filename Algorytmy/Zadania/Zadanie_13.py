A = [4 , 5, 12, 34, 25, 64, 1, 68, 33, 61, 95]

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


def FindPairToSumX(A, x):
    A = QuickSort(A, 0, len(A)-1)
    l, r = 0, len(A)-1
    while l < r:
        sum = A[l] + A[r]
        if sum > x:
            r -= 1
        elif sum < x:
            l += 1
        else:
            return True
        sum = 0
    return False


print(FindPairToSumX(A, 9))