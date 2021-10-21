A = [42, 12, 11, 54, 32, 11, 45, 12]
B = [5, 13]

C = [1, 2, 3, 4, 5, 6]
def BinarySearch(A, low, high, x):
    while low <= high:
        mid = (high+low)//2
        if A[mid] == x:
            return True
        if A[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

def Partition(A, low, high):
    i = (low-1)
    pivot = A[high]

    for j in range(low, high):
        if A[j] <= pivot:   #zmodyfikowany quicksort tak aby przedzial zaczynajacy sie z ta sama wartoscia jest najdluzszy
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



def CheckIfDiffrent(A, B):
    m = len(B)
    B = QuickSort(B, 0, m-1)

    for el in A:
        flag = BinarySearch(B, 0, m-1, el)
        if flag == True:
            return False
    return True

print(CheckIfDiffrent(A, B))