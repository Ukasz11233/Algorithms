import random


def Initializing_list():
    A = [0]*10
    for i in range(10):
        x = (random.randint(-5, 5), random.randint(-5, 5))
        A[i] = x
    return A

def Initializing_weights(n):
    W = [0]*n
    for i in range(n):
        W[i] = random.randint(1, n)
    return W


A = Initializing_list()
W = Initializing_weights(len(A))

def PostOfficeLocation(A, W):
    pairs = []
    for i in range(len(A)):
        pairs.append([A[i], W[i]])

    if

PostOfficeLocation(A, W)