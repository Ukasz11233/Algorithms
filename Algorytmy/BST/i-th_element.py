

class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.parent = None
        self.size = 0

def Insert(root, key):
    z = Node(key)
    x = root
    while x != None:
        y = x
        if z.key < x.key:
            x.size += 1
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


def Inorder(root):
    if root != None:
        Inorder(root.left)
        print(root.size)
        Inorder(root.right)


def Build_BST(A):
    n = len(A)

    root = Node(A[0])
    for i in range(1, n):
        Insert(root, A[i])
    return root


def Kth_element(root, k):
    if root != None:
        count = root.size + 1
        if k == count:
            return root
        elif k < count:
             return Kth_element(root.left, k)
        else:
             return Kth_element(root.right, k - count)


def which_element(x):
    if x.parent == None:
        return x.size + 1
    y = x.parent
    tmp = x
    right_size, root_size = 0, 0
    while y.parent != None:
        if y.right == tmp:  # jesli jest prawym poddrzewem to dodaje liczbe elementowe lewego poddrzewa i rodzica
            right_size += y.size + 1
        tmp = y
        y = y.parent

    if y.left == tmp:            # na koniec sprawdzam czy jest lewym czy prawym poddrzewem roota
        root_size = right_size
    elif y.right == tmp:
        root_size = y.size + right_size + 1

    if x.parent.left == x:
        return x.size + root_size + 1
    elif x.parent.right == x:
        return root_size + 2


def Find(x, k):
    while x != None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x


B =[15, 6, 8, 7, 3, 2, 4, 13, 9, 18, 17, 20]
root = Build_BST(B)
print(which_element(Find(root, 7)))