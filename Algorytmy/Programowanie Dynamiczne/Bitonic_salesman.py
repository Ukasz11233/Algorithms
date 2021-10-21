A = [[0, 6], [1, 0], [2, 3], [5, 4], [6, 1], [7, 5], [8, 2]]
B = [[0, 6], [1, 0], [2, 3], [4, 5]]
D = [[0, 2], [2, 4], [3, 1], [4, 3]]  # wroclaw, gdansk, krakow, warszawa
C = [["Wrocław", 0, 2], ["Warszawa",4,3], ["Gdańsk", 2,4], ["Kraków",3,1]]

class Paths():                # struktura przechowująca sciezke idaca w "lewo" i sciezke idaca w "prawo"
    def __init__(self, start = ""):
        self.left = [start]
        self.right = [start]


def Count_Distance(A):   # funkcja wypelniajaca tablice D odleglosciami wszystkich punktow
    D = [[0]*len(A) for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(A)):
                    D[i][j] = ((A[i][1]-A[j][1])**2 + (A[i][2] - A[j][2])**2)**(1/2)
    return D


def PrintTour(L, R):   # funkcja wypisujaca miasta najkrotszej sciezki
    for el in R:
        print(el, end=", ")

    for i in range(len(L) - 1, -1, -1):
        print(L[i], end=", ")



def BitonicSalesman(C):
    n = len(C)
    C.sort(key=lambda x:x[1])   # sortuje miasta po wspolrzedniej x
    D = Count_Distance(C)       # tablica D przechowuje odleglosci miedzy wszystkimi miastami

    F = [[float("inf")]*n for _ in range(n)]   #tablica do zapamietywania odlegosci funkcji F z wykladu
    Res = [[Paths(C[0][0]) for _ in range(n)] for _ in range(n)]  # tablica "sciezek"

    F[0][0] = 0
    for i in range(1, n):
        F[0][i] = F[0][i-1] + D[i-1][i]
        Res[0][i].right = Res[0][i-1].right + [C[i][0]]


    for i in range(1, n):   # ponizsze dwie petle realizuja funkcje F z wykladu i jednoczesnie zapamietywana jest
        for j in range(1, n):   # sciezka w "lewo" i w "prawo" dla polowy elementow tablicy F
            if j > i:
                if i == j-1:
                    q = float("inf")
                    for k in range(j-1):
                        if q > F[k][j-1] + D[k][j]:
                            q = F[k][j-1] + D[k][j]
                            mk = k

                    Res[i][j].left = Res[mk][j-1].right
                    Res[i][j].right = Res[mk][j-1].left + [C[j][0]]
                    F[i][j] = q

                else:
                    F[i][j] = F[i][j-1] + D[j-1][j]
                    Res[i][j].left = Res[i][j-1].left
                    Res[i][j].right = Res[i][j-1].right + [C[j][0]]


    result = float("inf")
    for i in range(n):      # na koniec wybieram najkrotsza sciezke z tablicy F
        if result > F[i][n-1] + D[i][n-1]:
            result = F[i][n-1] + D[i][n-1]
            idx = i
    print("Dlugosc trasy:", result)
    PrintTour(Res[idx][n-1].left, Res[idx][n-1].right)
    print("")

    return None



def TSP(D, F, i, j):
    if j > i:
        if F[i][j] != float("inf"):
            return F[i][j]

        if i == j-1:
            best = float("inf")
            for k in range(j-1):
                best = min(best, TSP(D, F, k, j-1) + D[k][j])
            F[j-1][j] = best
        else:
            F[i][j] = TSP(D, F, i, j-1) + D[j-1][j]

        return F[i][j]
    return float("inf")

def TSPWrap(A):
    n = len(A)
    D = Count_Distance(A)

    F = [[float("inf")]*n for _ in range(n)]
    F[0][1] = D[0][1]
    result = float("inf")
    for i in range(n):
        q = TSP(D, F, i, n-1) + D[i][n-1]
        if q < result:
            result = q

    return result

#print(TSPWrap(B))
print(BitonicSalesman(C))

