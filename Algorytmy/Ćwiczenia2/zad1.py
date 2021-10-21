class Node():
    def __init__(self, value = None):
        self.value = value
        self.next = None

def Create(A):
    for i in range(len(A)//2):
        A[i], A[len(A)-i-1] = A[len(A)-i-1], A[i]
    first = None
    for el in A:
        tmp = Node(el)
        tmp.next = first
        first = tmp
    return first

def Write(first):
    tmp = first
    while tmp is not None:
        print(tmp.value, end=" ")
        tmp = tmp.next
    print()

L1 = Create([1, 3, 5, 6, 7])
L2 = Create([0, 2, 4, 8, 9])
L = Create([4, 6, 8, 1, 5, 2, 3, 7])
#               l1
# 1  3  5  6  7

#         l2
# 0  2  4  8  9

# s                  n
# None 0 1 2 3 4 5 6 7
def Merge(L1, L2):
    newlist = Node()
    start = newlist
    while L1 is not None and L2 is not None:
        if L1.value < L2.value:
            newlist.next = L1
            L1 = L1.next
        else:
            newlist.next = L2
            L2 = L2.next
        newlist = newlist.next

    if L1 is None:
        newlist.next = L2
    elif L2 is None:
        newlist.next = L1
    return start.next

#     p    q
# 4 6 8    1 5 2 3 7

def CutOff(first):
    if first is None:
        return first
    p = first
    q = p.next
    while q is not None:
        if p.value < q.value:
            p = q
            q = q.next
        else:
            p.next = None
            return q
    return None


l = CutOff(L)
Write(l)
#
# None
def NaturalMergesort(L):
    result = last = Node()
    while True:
        list1 = L
        list2 = CutOff(list1)
        if list2 is None:
            last.next = list1
        L = CutOff(list2)
        if L is None:
            break
        last.next = Merge(list1, list2)
        last = result

    return last

Write(NaturalMergesort(L))
