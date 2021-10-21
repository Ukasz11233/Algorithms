A = [4, 6, 8, 1, 5, 2, 3, 7]

class Node():

    def __init__(self, value=None):
        self.value = value
        self.next = None


def Create(A):
    first = None
    for i in range(len(A)//2):
        A[i], A[len(A)-i-1] = A[len(A)-i-1], A[i]
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

def GetMiddle(first): #zwraca heady list przecietych w polowie
    if first is None:
        return None
    slow_ptr = fast_ptr = first
    while fast_ptr is not None and fast_ptr is not None:
        tmp = slow_ptr
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    tmp.next = None
    return first, slow_ptr



def Merge(list1, list2):
    newlist = start = Node()
    while list1 is not None and list2 is not None:
        if list1.value < list2.value:
            newlist.next = list1
            list1 = list1.next
        else:
            newlist.next = list2
            list2 = list2.next
        newlist = newlist.next

    if list1 is None:
        newlist.next = list2
    if list2 is None:
        newlist.next = list1

    return start.next

def Mergesort(first):
    if first is None or first.next is None:
        return first
    left, right = GetMiddle(first)
    result = Merge(Mergesort(left), Mergesort(right))
    return result

def cat(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    tmp = l1
    while l1.next is not None:
        l1 = l1.next
    l1.next = l2
    return tmp

l1 = Create([])
l2 = Create([])
Write(cat(l1, l2))
