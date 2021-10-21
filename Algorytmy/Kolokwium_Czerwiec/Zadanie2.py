class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

def dodaj(T, key):
    W = BNode(key)
    if key < T.value:
        if T.left == None:
            T.left = W
            W.parent = T
        else:
            dodaj(T.left, key)
    else:
        if T.right == None:
            T.right = W
            W.parent = T
        else:
            dodaj(T.right, key)


def createtree(keys):
    T = BNode(keys[0])
    for i in range(1, len(keys)):
        dodaj(T, keys[i])
    return T
A = [1, -1, -2, 4, 5, 6, 7]
A2 = [-1000, -1002, -1003, -1001, 10, -200, 100, -201, -199, 99, 101]
A3 = [-1000, -1002, -1003, -1001, 10, -100, 200, -101, -99, 199, 201]
def find_min(T, result):
    if T == None or (T.left == None and T.right == None):
         return result

    else:
        if T.value < result:
            result_left = find_min(T.left, T.value)
            result_right = find_min(T.right, T.value)

        else:
            result_left = find_min(T.left, result)
            result_right = find_min(T.right, result)

        

    return result

def cutthetree(T):
    result = 0
    result += find_min(T.left, float("inf"))
    result += find_min(T.right, float("inf"))
    return result



print(cutthetree(createtree(A3)))
