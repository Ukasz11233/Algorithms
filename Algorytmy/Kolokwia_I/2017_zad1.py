A = [24, 17, 36, 79, 41, 92, 53, 99]

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

def ListLength(first):
    tmp = first
    length = 0
    while tmp is not None:
        length += 1
        tmp = tmp.next
    return length

def AppendNode(list, node):
    while list.next is not None:
        list = list.next
    list.next = node


def GetMax(sentinel):
    p = max_prev = sentinel
    q = max = sentinel.next

    while q is not None:
        if q.val > max.val:
            max_prev = p
            max = q
        p = q
        q = q.next
    if max is not None:
        max_prev.next = max.next
        return max

def InsertionSort(list):
    if ListLength(list) >1:
        Sortedlist = None
        while list.next is not None:
            node = GetMax(list)
            node.next = Sortedlist
            Sortedlist = node
        return Sortedlist
    return None

def Last(list):
    while list.next is not None:
        list = list.next
    return list

def BucketSortOnLinkedList(list, a, b):
    list_len = ListLength(list)
    buckets = [Node() for _ in range(list_len+1)]
    p = list
    q = p.next
    while q is not None:
        bucket_idx = int((p.val/(b-a))*list_len)
        AppendNode(buckets[bucket_idx], p)
        p.next = None
        p = q
        q = q.next
    bucket_idx = int((p.val / (b - a)) * list_len)   # ostatni element
    AppendNode(buckets[bucket_idx], p)

    for i in range(list_len):
        buckets[i] = InsertionSort(buckets[i])
    Sortedlist = Node()

    for i in range(list_len-1, -1, -1):
        if buckets[i] is not None:
            first = buckets[i]
            last = Last(buckets[i])
            last.next = Sortedlist
            Sortedlist = first
    return Sortedlist

if __name__ == "__main__":
    list = MakeFromArray(A)
    node = BucketSortOnLinkedList(list, 0, 100)
    Print(node)

