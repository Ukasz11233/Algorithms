A = [(0, 1), (3, 2), (5, 4), (3, 5)]



def CheckFormula(A, k):
    n = len(A)
    V = [0]*(2*k)

    def DFSVisit(V, u):
        result = False

        if u == len(A):
            return True

        for el in A[u]:
            if V[el] == 1 or V[el] == 0:
                V[el] = 1
                if el < k:
                    V[el + k] = -1
                else:
                    V[el - k] = -1
                print(u, el, V)
                result = DFSVisit(V, u + 1)
                if result == True:
                    break

        return result

    start = A[0][1]
    V[start] = 1
    if start < k:
        V[start + k] = -1
    else:
        V[start - k] = -1
    print(V)
    result = DFSVisit(V, 1)
    return result

print(CheckFormula(A, 3))