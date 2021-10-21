from zad1testy import runtests

def ConvertTree(p):
    def inorder(p):
        nonlocal l

        if p is not None:
            inorder(p.left)
            l.append(p)
            inorder(p.right)


    l = []
    inorder(p)
    n = len(l)

    for i in range(0, n):
        l[i].left = l[2*i+1] if 2*i + 1 < n else None
        l[i].right = l[2*i+2] if 2*i + 2 < n else None
        l[i].parent = l[(i-1)//2] if i > 0 else None

    return l[0]

runtests(ConvertTree)