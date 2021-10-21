A = [2, 6, 32, 11, 76, 3, 45, 94, 37, 83, 22]

class Node:
    def __init__(self):
        self.next = None
        self.val = None


def Quicksortll(l):
    if empty(l):
        return l
    x = l[0].val
    lt = [None, None]
    eq = [None, None]
    gt = [None, None]

    while not empty(l):
        y = get(l)
        if y.val < x:
            app(lt, y)
        elif y.val > x:
            app(gt, y)
        else:
            app(eq, y)
    return concat(concat(Quicksortll(lt), eq), Quicksortll(gt))


def concat(l1, l2):
    if l1[0] == None:
        return l2
    if l2[0] == None:
        return l1
    first = l1[0]
    l1[1].next = l2[0]
    last = l2[1]
    return [first, last]


def get(l):
    tmp = l[0]
    l[0] = l[0].next
    tmp.next = None
    return tmp


def empty(l):
    return l[0] == None


def app(l, el):
    if l[0] == None:
        l[0] = el
    else:
        l[1].next = el
    l[1] = el


def printl(l):
    tmp = l[0]
    while tmp != None:
        print(tmp.val, end = " ")
        tmp = tmp.next
    print()


def create(l):
    if len(l) == 0:
        return [None, None]
    first = Node()
    first.val = l[0]
    first.next = None
    last = first

    for i in range(1, len(l)):
        tmp = Node()
        tmp.val = l[i]
        tmp.next = None
        last.next = tmp
        last = tmp
    return [first, last]

list = create(A)
list = Quicksortll(list)
printl(list)

