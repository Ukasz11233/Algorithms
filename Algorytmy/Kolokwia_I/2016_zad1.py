A = [[ 0 for i in range(3)] for i in range(3)]
B = [[2, 19, 32], [43, 24, 12], [54, 29, 17]]

#zlozonosc to: O(n*n + n*n*lgn) = O(n^2*lgn)
#poniewaz: n razy tworze kopiec, czyli n*O(n), nastepnie n^2 razy wywoluje minimum z kopca minimum.
#czy lepszym rozwiazaniem byloby posortowanie tablicy zawierajacej n^2 elementow w czasie "liniowym" O(n^2)?

print(B)
def Parent(i):
    return (i-1)//2

def Left(i):
    return (2*i)+1

def Right(i):
    return (2*i)+2

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


def SumSort(A, B, n):
    for i in range(n):
        Build_Min_Heap(B[i])
    for i in range(n):
        for j in range(n):
            A[i][j] = Heap_Extract_Min(B[j])
    return A

print(SumSort(A, B, len(A)))