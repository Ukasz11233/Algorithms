from Edmonds_Karp2 import Edmonds_Karp, BFS, Increase_Flow

G = [[(5, 10)],
     [(5, 12), (6, 5)],
     [(6, 8), (7, 14)],
     [(7, 7), (8, 11)],
     [(8, 2)],
     [(9, 3)],
     [(9, 15), (10, 6)],
     [(10, 20), (11, 13)],
     [(11, 18)],
     [], [], []]

def Shops_Fabrics(G, s, t):
    n = len(G)
    G.append([])
    for i in range(s):
        G[n].append((i, float("inf")))

    G.append([])
    for i in range(n - t, n, 1):
        G[i].append((n+1, float("inf")))

    n = len(G)

    return Edmonds_Karp(G, n-2, n-1)



print(Shops_Fabrics(G, 5, 3))
