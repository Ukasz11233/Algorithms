W = [2, 2, 4, 8, 1, 8, 16]

def FulfillTrailer(W, k):
    W.sort()
    result = []
    n = len(W)
    for i in range(n-1, -1, -1):
        if k >= W[i]:
            k -= W[i]
            result.append(W[i])
    return result

print(FulfillTrailer(W, 27))