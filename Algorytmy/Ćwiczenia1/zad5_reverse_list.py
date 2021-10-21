class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

def MakeFromArray(A):
    first = None
    for el in A:
        p = Node(el)
        p.next = first
        first = p
    return first

def Write(first):
    tmp = first
    while tmp is not None:
        print(tmp.value, end=" ")
        tmp = tmp.next
    print()

L = MakeFromArray([2, 5, 3, 7, 11])
Write(L)

def ReverseList(first):
    prev = None
    curr = first
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
RL = ReverseList(L)
Write(RL)

