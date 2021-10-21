class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.parent = None


A = [20, 10, 27, 5, 15, 22, 30]

B =[15, 6, 7, 3, 2, 4, 13, 9, 18, 17, 20]

def Insert(root, key):
    z = Node(key)
    x = root
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == None:
        root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z


def Find(x, k):
    while x != None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x


def Inorder(root):
    if root != None:
        Inorder(root.left)
        print(root.key, end=" ")
        Inorder(root.right)


def Minimum(x):
    while x.left != None:
        x = x.left
    return x


def Maximum(x):
    while x.right != None:
        x = x.right
    return x


def Successor(x):
    if x.right != None:
        return Minimum(x.right)
    y = x.parent
    while y != None and x == y.right:
        x = y
        y = y.parent
    return y


def Predecessor(x):
    if x.left != None:
        return Maximum(x.left)
    y = x.parent
    while y != None and y.left == x:
        x = y
        y = y.parent
    return y


def Build_BST(A):
    n = len(A)

    root = Node(A[0])
    for i in range(1, n):
        Insert(root, A[i])

    #Inorder(root)
    return root


root = Build_BST(B)
tmp = Predecessor(Successor(Find(root, 15)))
print(tmp.key)