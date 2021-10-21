class Node:
    def __init__(self, value = None):
        self.value = value
        self.Next = None


def MakeFromArray(A):
    for i in range(len(A)//2):
        A[i], A[len(A)-i-1] = A[len(A)-i-1], A[i]
    first = None
    for el in A:
        p = Node(el)
        p.next = first
        first = p
    sentinel = Node()
    sentinel.next = first
    return sentinel


def Write(first):
    while first is not None:
        print(first.value, end=" ")
        first = first.next
    print()


def GetMax(sentinel):
    max_prev = sentinel
    max = sentinel.next
    p = max_prev
    q = max
    while q is not None:
        if q.value > max.value:
            max_prev = p
            max = q
        p = q
        q = q.next
    if max is not None:
        max_prev.next = max.next
        return max

def Insertion_Sort(first):
    SortedList = None
    while first.next is not None:
        node = GetMax(first)
        node.next = SortedList
        SortedList = node
    return SortedList

L = MakeFromArray([2, 5, 3, 7, 11])
Write(L)
SortedList = Insertion_Sort(L)
Write(SortedList)
