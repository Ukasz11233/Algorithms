class Soldier:
    def __init__(self):
        self.type = False
        self.next = None

class Series:
    def __init__(self):
        self.first = None
        self.last = None

    def Creat_Series_Of_Soldiers(self, A):
        self.first = Soldier()
        p = self.first
        self.last = p
        if A[0] == 1:
            p.type = True
        for i in range(1, len(A)):
            new = Soldier()
            p.next = new
            p = new
            self.last = p
            if A[i] == 1:
                p.type = True

    def Print_Series(self):
        p = self.first
        while p is not None:
            print(p.type)
            p = p.next
A = [0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0]

Series = Series()
Series.Creat_Series_Of_Soldiers(A)

def Distance_To_Deal(Series):
    head = Series.first
    sum_to_deal = 0
    distance = 0
    while head is not None:
        if head.type is True:
            distance+=1
        else:
            sum_to_deal += distance*2
        head = head.next
    return sum_to_deal
print(Distance_To_Deal(Series))
