A = [11, 2, 3]
B = [6, 4, 5]
C = [17, 23, 54, 11, 4]


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


def BinarySearch(A, x, l, r):
    while l <= r:
        mid = (l + r)//2
        if x == A[mid]:
            return True
        elif x > A[mid]:
            l = mid + 1
        else:
            r = mid -1
    return None

def FindTriangle(A, B, C):
    c = len(C)
    C = QuickSort(C, 0, c-1)
    print(C)
    for i in range(len(A)):
        for j in range(len(B)):
            result = BinarySearch(C, A[i] + A[j], 0, c-1)
            if result is True:
                return True
    return False

print(FindTriangle(A, B, C))