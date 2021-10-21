class Node:
    def __init__(self, val = 0, next = None):
        self.next = next
        self.value = val


class LinkedList:
    def __init__(self):
        self.first = None

    def Initialize(self, A):
        if len(A) == 0:
            return
        self.first = Node(A[0])
        x = self.first
        for i in range(1, len(A)):
            new = Node(A[i])
            x.next = new
            x = new
        x.next = None

def Print(B):
    tmp = B.first
    while tmp != None:
        print(tmp.value, end=" ")
        tmp = tmp.next
    print()


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10, 12]

def FixSortedList(B):
    element = B.first
    tmp = None
    while element.next.next != None:
        prev = element
        element = element.next
        if element.value > element.next.value:
            tmp = element
            prev.next = element.next

    element = B.first
    if tmp is not None:
        print(tmp.value)
        while element.next != None:
            if tmp.value > element.value and tmp.value < element.next.value:
                x = element.next
                element.next = tmp
                tmp.next = x
            element = element.next

    return B

B = LinkedList()
B.Initialize(A)
Print(B)
B = FixSortedList(B)
Print(B)