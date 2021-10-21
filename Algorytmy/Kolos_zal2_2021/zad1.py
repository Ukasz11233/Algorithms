from zad1testy import runtests
D = [(2,3,10,6),(3,1,8,8),(5,4,9,7)]
D1 = [(6, 4, 7, 5), (2, 3, 10, 6), (3, 1, 8, 8), (5, 4, 9, 7)]
def CountDiff(D, i, j):
    xa1, ya1, xa2, ya2 = D[i]
    xb1, yb1, xb2, yb2 = D[j]
    P1 = (xa2 - xa1)*(ya2 - ya1)
    P2 = (xb2 - xb1)*(yb2 - yb1)

    if xa1 < xb1:
        if xa2 < xb2:
            l = xa2 - xb1
        else:
            l = xb2 - xb1
    else:
        if xa2 < xb2:
            l = xa2 - xa1
        else:
            l = xb2 - xa1

    if ya1 < yb1:
        if ya2 < yb2:
            r = ya2 - yb1
        else:
            r = yb2 - yb1
    else:
        if ya2 < yb2:
            r = ya2 - ya1
        else:
            r = ya2 - ya1


    return min(P1 - l*r, P2 - l*r)



def react(D):
    n = len(D)
    maximum = CountDiff(D, 0, 1)
    result = 0
    #print(maximum)
    for i in range(n-1):

        tmp = CountDiff(D, i, i+1)
        #print(tmp)
        if tmp < maximum:
            maximum = tmp
            result = i

    return result

#print(react(D1))
runtests(react)