A = [1, 2, 11, 4, 5, 7, 9]

class Node():
    def __init__(self, value = None):
        self.val = value
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
        print(tmp.val, end=" ")
        tmp = tmp.next
    print()

list = MakeFromArray(A)
Print(list)

def MergeLists(list1, list2):
    p = list1
    q = list2
    newlist = None
    while p is not None and q is not None:
        if p.val <= q.val:
            tmp = p
            p = p.next
        else:
            tmp = q
            q = q.next

        tmp.next = newlist
        newlist = tmp

    if p is None:
        q.next = newlist
        newlist = q
    if q is None:
        p.next = newlist
        newlist = p

    return newlist


def Reverse(first):
    prev = None
    curr = first
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def fixSortedList(list):
    p = list
    q = p.next
    wrong = None
    while q is not None:
        if q.val < p.val:
            wrong = q
            p.next = None
            break
        p = q
        q = q.next
    fixed = MergeLists(list, wrong)
    result = Reverse(fixed)
    return result

Print(fixSortedList(list))