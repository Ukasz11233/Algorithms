A = [[1, 6], [3, 5], [3, 8], [6, 12], [4, 7], [9, 15], [6, 13]]



def Partition(A, low, high):
    i = (low-1)
    pivot = A[high][0]

    for j in range(low, high):
        if A[j][0] < pivot:   #zmodyfikowany quicksort tak aby przedzial zaczynajacy sie z ta sama wartoscia jest najdluzszy
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


def FindBiggest(A):
    n = len(A)
    A = QuickSort(A, 0, n-1)
    print(A)
    longest, counter, k = 0, 0, 0
    result = None
    for i in range(1, n):
        if A[i][1] <= A[k][1] and A[i][0] >= A[k][0]:
            counter += 1
            if counter > longest:
                longest = counter
                result = A[k][0], A[k][1]
        else:
            k = i
            counter = 0

    return result

print(FindBiggest(A))
