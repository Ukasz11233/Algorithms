from max_heap_implementation import Max_Heapify, Left, Right
def Min_Heapify(A, i, n):
    l = Left(i)
    r = Right(i)
    if l < n and A[l] < A[i]:
        smallest = l
    else: smallest = i
    if r < n and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        Min_Heapify(A, smallest, n)

def Build_Min_Heap(A):
    for i in range((len(A)//2)-1, -1, -1):
        Min_Heapify(A, i, len(A))


def Heap_Minimum(A):
    return A[0]


def Heap_Extract_Min(A):
    if len(A) < 1:
        print("Kopiec pusty")
    n = len(A)
    min = A[0]
    A[0] = A[n-1]
    n -= 1
    Min_Heapify(A, 0, n)
    return min


def Heap_Increase_Key(A, i, key):
    if key < A[i]:
        print("nowy klucz jest mniejszy niz klucz aktualny")
    A[i] = key
    while i > 0 and A[Parent(i)] > A[i]:
        A[i], A[Parent(i)] = A[Parent(i)], A[i]
        i = Parent(i)


def Min_Heap_Insert(A, key):
    n = len(A)
    n =+ 1
    A[n] = float("INF")
    Heap_Increase_Key(A, n, key)

