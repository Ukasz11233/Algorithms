A = [0, 1, 2, 3, 4, 5, 6, 7]

class Lamp:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.on = False
        self.dark = None
        self.interval = None
        self.value = None


    def Creaate_Lamps(self, A):
        n = len(A)
        k = 1
        while k < n:
            k *= 2

        T = [Lamp() for _ in range((2 * k) - 1)]
        for i in range(k - 1, len(T)):
            if i - k + 1 < n:
                T[i].value = A[i - k + 1]
                T[i].dark = (i - k + 1, i - k + 1)
            else:
                T[i].value = 0
                T[i].dark = (i - k + 1, i - k + 1)
            T[i].interval = T[i].dark

        for i in range(k - 2, -1, -1):
            T[i].right = T[2 * i + 2]
            T[i].left = T[2 * i + 1]
            T[i].parent = T[(i - 1) // 2]
            inter = (T[i].left.dark[0], T[i].right.dark[1])
            T[i].dark = inter
            T[i].interval = inter

        return T

class Darkness():
    def __init__(self, A):
        self.L = Lamp().Creaate_Lamps(A)

    def max_darkness(self):
        return self.L[0].dark


    def minimum(self, i):
        dark = L[i].dark
        


    def turn_off(self, i):
        k = 0
        n = len(self.L)

        while k < n:

            if self.L[k].value == i:
                self.L[k].on = False
                self.L[k].dark = (i, i)
                break
            if self.L[k].interval[0] <= i and self.L[k].interval[1] >= i:
                mid = (self.L[k].interval[1] + self.L[k].interval[0]) // 2
                if i <= mid:
                    k = (2 * k) + 1
                else:
                    k = (2 * k) + 2

            else:
                return

        while k >= 0:
            if self.L[k].left != None and self.L[k].right != None:
                l = self.L[k].left.dark
                r = self.L[k].right.dark
                if l != -1 and r != -1:
                    if l[1] + 1 == r[0]:
                        self.L[k].dark = (l[0], r[1])
                    else:
                        if l[1] - l[0] > r[1] - r[0]:
                            self.L[k].dark = (l[0], l[1])
                        else:
                            self.L[k].dark = (r[0], r[1])
                elif l == -1:
                    self.L[k].dark = (r[0], r[1])
                elif r == -1:
                    self.L[k].dark = (l[0], l[1])
            k = (k - 1) // 2

    def turn_on(self, i):
        k = 0
        n = len(self.L)
        while k < n:
            if self.L[k].value == i:
                self.L[k].on = True
                self.L[k].dark = -1
                break
            if self.L[k].interval[0] <= i and self.L[k].interval[1] >= i:
                mid = (self.L[k].interval[1] + self.L[k].interval[0])//2
                if i <= mid:
                    k = 2*k + 1
                else:
                    k = 2*k + 2
            else:
                return

        while k >= 0:
            if self.L[k].left != None and self.L[k].right != None:
                l = self.L[k].left.dark
                r = self.L[k].right.dark
                if l!= -1 and r != -1:
                    if l[1] + 1 == r[0]:
                        self.L[k].dark = (l[0], r[1])
                    else:
                        if l[1] - l[0] > r[1] - r[0]:
                            self.L[k].dark = (l[0], l[1])
                        else:
                            self.L[k].dark = (r[0], r[1])
                elif l == -1:
                    self.L[k].dark = (r[0], r[1])
                elif r == -1:
                    self.L[k].dark = (l[0], l[1])
            k = (k - 1) // 2


Lamps = Darkness(A)
Lamps.turn_on(5)
print(Lamps.max_darkness())
Lamps.turn_off(5)
print(Lamps.max_darkness())