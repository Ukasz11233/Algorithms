# Łukasz Chmielewski


from zad2testy import runtests

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




def length(p):
    res = 0
    while p != None:
        res += 1
        p = p.next
    return res

L2 = [2, 3, 5, 7, 11, 13, 17, 19, 31, 23, 29, 43, 41, 37, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]

def SortH(p,k):
    Q = []
    curr = p
    if k == 0:       # warunek brzegowy
        while curr != None:
            tmp = curr
            Q = AddNode(Q, tmp)
            curr = curr.next
            tmp.next = None
    elif k == 1:
        for i in range(2):
            tmp = curr
            Q = AddNode(Q, tmp)
            curr = curr.next
            tmp.next = None
    else:
        for i in range(k):
            tmp = curr
            Q = AddNode(Q, tmp)
            curr = curr.next
            tmp.next = None

    sorted_list = Node()
    sorted_list.value = float("inf")
    first = sorted_list
    while curr != None:

        tmp = Heap_Minimum(Q)
        Q = Heap_Remove_Min(Q)
        sorted_list.next = tmp
        sorted_list = tmp

        Q = AddNode(Q, curr)
        chwilkowy = curr
        curr = curr.next
        chwilkowy.next = None


    while len(Q) > 0:
        tmp = Heap_Minimum(Q)
        Q = Heap_Remove_Min(Q)
        sorted_list.next = tmp
        sorted_list = tmp

    return first.next

runtests( SortH )