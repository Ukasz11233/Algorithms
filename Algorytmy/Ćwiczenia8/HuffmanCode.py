S = ["a", "b", "c", "d", "e", "f"]
F = [10, 11, 7, 13, 1, 20]

from queue import PriorityQueue

class HuffNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val      # czestosc wystepowania
        self.left = left    # lewy syn
        self.right = right  # prawy syn
        self.symbol = None  # symbol jaki reprezentuje
        self.code = ""      # kod Huffmana


def SearchHuffTree(el):
    if el.left is not None:     # sprawdzam czy ma lewego syna, jesli tak przeszukuje dalej i zapisuje w nim kod huffmana
        el.left.code += el.code
        SearchHuffTree(el.left)

    if el.right is not None:    # analogicznie w prawo
        el.right.code +=  el.code
        SearchHuffTree(el.right)


def huffman(S, F):
    n = len(S)
    H = [HuffNode() for _ in range(n)]
    Q = PriorityQueue()
    for i in range(n):   # uzuzpelniam tablice H struktura HuffmanCode i dodaje kazdy element do kelejki priorytetowej
        H[i].val = F[i]
        H[i].symbol = S[i]
        Q.put((H[i].val, H[i]))

    while Q.qsize() > 1:  # buduje drzewo huffmana, wykorzystujac kolejke priorytetowa
        smaller = Q.get()[1]
        smaller.code += "1"
        bigger = Q.get()[1]
        bigger.code += "0"

        parent = HuffNode(smaller.val + bigger.val, smaller, bigger)
        Q.put((parent.val, parent))

    result = 0
    root = Q.get()[1]
    SearchHuffTree(root)  # wywoluje funkcje ktora bedzie spisywala wartosci kodu huffmana przeszukujac zbudowane drzewo

    for i in range(n):
        print(H[i].symbol, ':', H[i].code[::-1])   #odwracam stringa, bo jest zapisany zaczynajac od najmniej waznego bitu
        result += len(H[i].code)*F[i]

    return result

print(huffman(S, F))