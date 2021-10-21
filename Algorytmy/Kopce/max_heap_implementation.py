A = [6, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]


def Parent(i):
    return (i-1)//2


def Left(i):
    return (2*i)+1


def Right(i):
    return (2*i)+2


def Max_Heapify(A, i, n):
    l = Left(i)
    r = Right(i)
    if l < n and A[l] > A[i]:
        largest = l
    else: largest = i
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        Max_Heapify(A, largest, n)


def Build_Max_Heap(A):
    for i in range((len(A)//2)-1, -1, -1):
        Max_Heapify(A, i, len(A))
    return A

def Heap_Maximum(A):
    return A[0]


def Heap_Remove_Max(A):
    if len(A) < 1:
        print("Kopiec pusty")
    n = len(A)
    A[0] = A[n-1]
    A = A[:len(A)-1]
    Max_Heapify(A, 0, len(A))
    return A


def Heap_Increase_Key(A, i, key):
    if key < A[i]:
        print("nowy klucz jest mniejszy niz klucz aktualny")
    A[i] = key
    while i > 0 and A[Parent(i)] < A[i]:
        A[i], A[Parent(i)] = A[Parent(i)], A[i]
        i = Parent(i)


def Max_Heap_Insert(A, key):
    n = len(A)
    n += 1
    A[n] = float("-INF")
    Heap_Increase_Key(A, n, key)


B = Build_Max_Heap([6, 17, 3, 16, 13])
print(Heap_Remove_Max(B))