class Node:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class LinkedList:
    def __init__(self, first=None, last=None):
        self.first=first
        self.last=last

    def isEmpty(self):
        return self.first is None

    def makeFromArray(self, list):
        if len(list) == 0:
            return
        self.first=Node(list[0])
        p=self.first
        self.last=p
        for i in range(1, len(list)):
            new=Node(list[i])
            p.next=new
            p=new
            self.last=p

    def printlist(self):
        p=self.first
        while p != None:
            print(p.val)
            p=p.next

    def hasOneElement(self):
        return self.first==self.last

    def add(self, val):   #dodawanie na koniec
node=Node(val)
        if self.isEmpty():
            self.first=node
            self.last=node
            return
        self.last.next=node
        self.last=node
def joinLists(tabOfLinkedList):
    wynik=LinkedList()
    findBegin=False
    for i in tabOfLinkedList:
        if not i.isEmpty():
            i.last.next=None
    for i in tabOfLinkedList:
        if not findBegin and not i.isEmpty():
            findBegin=True
            wynik.first=i.first
            wynik.last=i.last
        elif not i.isEmpty():
            wynik.last.next=i.first
            wynik.last=i.last
    return wynik

def quicksortOnLinkedList(lista):
    if lista.isEmpty() or lista.hasOneElement():
        return lista
    smaller=LinkedList()
    grater=LinkedList()
    equal=LinkedList()

    wsk=lista.first

    while wsk != None:
        if wsk.val<lista.last.val:
            smaller.add(wsk.val)
        elif wsk.val==lista.last.val:
            equal.add(wsk.val)
        elif wsk.val>lista.last.val:
            grater.add(wsk.val)
        wsk=wsk.next

    return joinLists([quicksortOnLinkedList(smaller), equal, quicksortOnLinkedList(grater)])


if __name__ == '__main__':
    lista=LinkedList()
    tab=[2,5,8,3,2,7,8,5,4,9,4]
    lista.makeFromArray(tab)
    lista.printlist()
    wynik=quicksortOnLinkedList(lista)
    print("wynik: ")
    wynik.printlist()