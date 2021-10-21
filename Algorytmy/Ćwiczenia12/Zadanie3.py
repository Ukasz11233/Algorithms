from Edmonds_Karp2 import Edmonds_Karp, BFS, Increase_Flow

G = [[(1, 1), (2, 1),  (5, 1)],
     [(0, 1), (4, 1), (5, 1)],
     [(0, 1), (5, 1)],
     [(5, 1), (4, 1)],
     [(1, 1), (5, 1), (3, 1)],
     [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)]]


def k_coherence(G):
    n = len(G)

    dist = Edmonds_Karp(G, 0, n-1)

    return dist

print(k_coherence(G))