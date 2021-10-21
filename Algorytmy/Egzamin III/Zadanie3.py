A = [ [0,1,2,4,5], [0,10,20], [5,15,25] ]

class Node:
  def __init__(self, value = None):
    self.value = value
    self.next = None


def MakeFromArray(A):
    start = None
    for i in range(len(A)-1, -1, -1):
        tmp = Node(A[i])
        tmp.next = start
        start = tmp
    return start


def CreateArrays(A):
    n = len(A)
    result = []
    for i in range(n):
        result.append(MakeFromArray(A[i]))
    return result


def Print(first):
    tmp = first
    while tmp is not None:
        print(tmp.value, end=" ")
        tmp = tmp.next
    print()


def Parent(i):
    return (i-1)//2


def Left(i):
    return (2*i)+1


def Right(i):
    return (2*i)+2


def Min_Heapify(A, i, n):
    l = Left(i)
    r = Right(i)
    if l < n and A[l].value < A[i].value:
        smallest = l
    else: smallest = i
    if r < n and A[r].value < A[smallest].value:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        Min_Heapify(A, smallest, n)



def Build_Min_Heap(A):
    for i in range((len(A)//2)-1, -1, -1):
        Min_Heapify(A, i, len(A))
    return A

def Heap_Minimum(A):
    return A[0]


def Heap_Remove_Min(A):
    if len(A) == 1:
        return []
    n = len(A)
    A[0] = A[n-1]
    A = A[:len(A)-1]
    Min_Heapify(A, 0, len(A))
    return A


def Heap_Increase_Key(A, i, key):
    if key.value < A[i].value:
        print("nowy klucz jest mniejszy niz klucz aktualny")
    A[i] = key
    while i > 0 and A[Parent(i)].value > A[i].value:
        A[i], A[Parent(i)] = A[Parent(i)], A[i]
        i = Parent(i)


def Min_Heap_Insert(A, key):
    n = len(A)
    tmp = Node()
    tmp.value = -float("inf")
    A.append(tmp)
    Heap_Increase_Key(A, n, key)
    return A




def AddNode(Q, tmp):
    if len(Q) == 0:
        Q = Build_Min_Heap([tmp])
    else:
        Q = Min_Heap_Insert(Q, tmp)
    return Q



def Merge_arrays(A):
    n = len(A)
    Arrays = CreateArrays(A)





Merge_arrays(A)