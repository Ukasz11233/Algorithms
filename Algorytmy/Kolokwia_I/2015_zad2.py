class Node:
    def __init__(self, val = 0, next = None):
        self.next = next
        self.value = val

class TwoLists:
    def __init__(self):
        self.even = LinkedList()
        self.odd = LinkedList()


class LinkedList:
    def __init__(self):
        self.first = Node()

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

B = LinkedList()
B.Initialize(A)
Print(B)

# w pythonie nie ma wskanikow, wiec zadanie chyba niewykonalne