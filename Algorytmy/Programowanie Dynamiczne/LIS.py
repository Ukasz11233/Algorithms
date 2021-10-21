# Algorytm wyszukiwania długości najdłuższego rosnącego podciągu był pokazywany na wykładzie i ma złożoność O(n^2)
# Algorytm wypisywania wszystkich LIS ma złożoność O(k^2), gdzie k to ilosc najdluzszych rosnacych podciagow, natomiast ich ilosc moze byc rowna 2^n

class PriorityQueue:  #struktura kolejka priorytetowa

    def __init__(self):
        self.queue = []


    def insert(self, node):
        if self.size() == 0:
            self.queue.append(node)

        else:
            for x in range(0, self.size()):
                if node.priority >= self.queue[x].priority:
                    if x == (self.size()-1):
                        self.queue.insert(x+1, node)
                else:
                    self.queue.insert(x, node)

    def delete(self):
        return self.queue.pop(0)


    def size(self):
        return len(self.queue)


class Queue:  # stuktura kolejki
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Item:   #struktura w ktorej bede przetrzymywal wartosci potrzebne do wypisana LIS

    def __init__(self, length=None, idx=None, val=None, output=[], priority = 0):
        self.length = length
        self.idx = idx
        self.val = val
        self.output = output
        self.priority = priority


def LIS(S, n):
    L = [1]*n
    L[0] = 1
    P = [-1]*n
    for i in range(1, n):
        for j in range(i):
            if S[j] < S[i] and L[j]+1 > L[i]:
                L[i] = L[j] + 1
                P[i] = j


    result = PrintAllLis(S, L, max(L), n)
    return result


def PrintAllLis(S, L, length, n):
    queue = Queue()
    output_queue = PriorityQueue()

    for i in range(n):      # dodaje do kolejki "najwieksze" elementy z tablicy L, czyli ostatnie wartosci kazdego LIS
        if L[i] == length:
            queue.enqueue(Item(length, i, S[i], [S[i]]))

    while queue.isEmpty() == False:
        tmp = queue.dequeue()
        k = 0

        if tmp.length == 1:   # jesli doszlismy do ostatniego elementu, dodajemy element do kolejki priorytetowej
            output_queue.insert(tmp)    #po to aby element z najmniejszym priorytetem (czyli w kolejnosci wystepowania), mogly zostac wypisane najpierw

        for j in range(tmp.idx):
            if L[j] == tmp.length-1 and S[j] <= tmp.val:    # iteruje po tablicy L, szukajac poprzednikow danego elementu podciagu
                queue.enqueue(Item(L[j], j, S[j], [S[j]] + tmp.output, k))   # jesli ich znajde, dodaje do kolejki, za kazdym razem zwiekszajac priorytet danego podciagu
                k += 1

    result = output_queue.size()     # ilosc rosnacych podciagow
    while output_queue.size() > 0:   # wypisuje wszystkie podciagu w kolejnosci ich wystepowania, wyciagajac je kolejno z kolejki priorytetowej
        for el in output_queue.delete().output:
            print(el, end=" ")
        print("")

    return result

def PrintAllLIS(A):
    n = len(A)
    return LIS(A, n)
