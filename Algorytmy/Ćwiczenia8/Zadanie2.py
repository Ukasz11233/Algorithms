G = [(10, 2), (3, 4), (10, 2), (5, 1), (3, 0), (8, 4)]

def FindMaxPrice(G, t):
    n = len(G)
    T = [0]*(t+1)
    G.sort(key=lambda x:x[0])
    print(G)
    for i in range(n-1, -1, -1):
        k = G[i][1]

        while k >= 0:
            if T[k] == 0:
                T[k] = G[i][0]
                break
            else:
                k -= 1
    return T

print(FindMaxPrice(G, 4))