from random import randint, seed


class Node:
    def __init__(self):
        self.next = None
        self.value = None


def cat(l1, l2):  #funkcja łącząca dwie listy w jedną
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    start = l1
    while l1.next is not None:
        l1 = l1.next
    l1.next = l2
    return start


def qsort(L):
    if L is None or L.next is None:
        return L

    tmp = L
    while tmp.next is not None:   # jako pivot wybieram ostatni element, nie psuje to zlozonosci obliczeniowej tego algorytmu w notacji duzego O
        tmp = tmp.next
    pivot = tmp.value

    lt = lt_start = Node()  # trzy nowe listy dla elementow mniejszych, rownyc i wiekszych od pivota
    eq = eq_start = Node()
    gt = gt_start = Node()

    while L is not None: # petla uzupelniajaca powyzsze 3 listy
        if L.value < pivot:
            lt.next = L
            lt = L
        elif L.value == pivot:
            eq.next = L
            eq = L
        else:
            gt.next = L
            gt = L
        tmp = L
        L = L.next
        tmp.next = None  #wypianie elementu z listy wejsciowej

    return cat(cat(qsort(lt_start.next), eq_start.next), qsort(gt_start.next))


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


def printlist(L):
    while L != None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")

seed(42)

n = 10
T = [randint(1, 10) for i in range(10)]
L = tab2list(T)

print("przed sortowaniem: L =", end=" ")
printlist(L)
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
    print("List jest pusta, a nie powinna!")
    exit(0)

P = L
while P.next != None:
    if P.value > P.next.value:
        print("Błąd sortowania")
        exit(0)
    P = P.next

print("OK")
