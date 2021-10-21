class Member():
    def __init__(self, party = 0, idx = -1):
        self.sub = []
        self.f = -1
        self.g = -1
        self.party = party
        self.idx = idx

A = [Member() for _ in range(13)]
P = [7, 30, 9, 8, 4, 11, 5, 2, 1, 4, 15, 13, 20]
for i in range(len(P)):
    A[i].party = P[i]
    A[i].idx = i

A[0].sub = [A[1], A[2], A[3]]
A[1].sub = [A[4], A[5], A[6]]
A[2].sub = [A[7], A[8], A[9]]
A[3].sub = [A[10], A[11], A[12]]


def F(v):
    if v.f > -1:
        return v.f
    sum = 0
    for el in v.sub:
        sum += G(el)

    v.f = max(v.party + sum, G(v))

    return v.f

def G(v):
    if v.g > -1:
        return v.g
    sum = 0
    for el in v.sub:
        sum += F(el)
    v.g = sum
    return v.g

def PrintTour(A, i, n):
    if i < n:
        if A[i].g == 0:
            print(i, end=" ")
            return

        if A[i].f == A[i].g:
            for el in A[i].sub:
                PrintTour(A, el.idx, n)


        else:
            for el in A[i].sub:
                for elem in el.sub:
                    PrintTour(A, elem.idx, n)
            print(i, end=" ")


def FirmParty(A):
    q = max(F(A[0]), G(A[0]))
    PrintTour(A, 0, len(A))
    print("")
    return q
print(FirmParty(A))