A = [11, 3, 2, 7, 5, 13]


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.value = None


def CreateBST(l):
    def InsertToBST(p, val):
        t = Node()
        t.value = val
        if p is None: return t

        r = p
        while r is not None:
            q = r
            if val < r.value:
                r = r.left
            else:
                r = r.right

        if val < q.value:
            q.left = t
        else:
            q.right = t

        t.parent = q
        return p

    p = None
    for val in l: p = InsertToBST(p, val)
    return p


def PrintTree(p):
    if p is not None:
        PrintTree(p.left)
        print(p.value, end=' ')
        PrintTree(p.right)



def CountNodes(first):
    tmp = first
    result = 0
    while tmp is not None:
        tmp = tmp.left
        result += 1

    return result


def SortedListToBST(first, n):
    k = 1
    prev = first
    curr = first.left
    nodes_counter = 2
    curr_node = 0
    while k < n:
        while curr_node < nodes_counter:

    k+= 1
    curr.left = curr.next.left


def ConvertTree(p):

    def inOrder(p):
        nonlocal tmp

        if p is not None:
            inOrder(p.left)
            tmp.left = p
            p.parent = tmp
            tmp = p
            inOrder(p.right)

    tmp = Node()
    first = tmp
    inOrder(p)
    n = CountNodes(first.left)
    print(n)
    return first.left

T = CreateBST(A)

def PrintSingleTree(p):

    if p is not None:
        print(p.value, end= " ")
        PrintSingleTree(p.left)


result = ConvertTree(T)
PrintSingleTree(result)