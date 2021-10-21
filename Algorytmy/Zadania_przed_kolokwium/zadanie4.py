A = [1, 3, 5, 9, 2, 4, 6, 8]

def BukcetSort(A):
    n = len(A)
    k = max(A) + 1
    counting = [0 for _ in range(k)]
    output = [0 for _ in range(n)]
    result = []
    for i in range(n):
        counting[A[i]] += 1
    for i in range(1, k):
        counting[i] += counting[i-1]
    for i in range(n-1, -1, -1):
        counting[A[i]] -= 1
        output[counting[A[i]]] = A[i]
    for i in range(n//2):
        result.append((output[i], output[n-i-1]))
    return result

print(BukcetSort(A))

# n := len(A)-1
# niech klucze beda posortowanie niemalejaca: A[i_1] <= A[i_2] <= A[i_3] .... <= A[i_n]
# wybiram takie 1 <= i_j < i_k < len(A)-1
# zawsze A[i_j] + A[i_k] <= A[i_0] + A[i_n] z zalozenia, poniewaz tablica jest posortowana
# wiec nalezy brac zawsze najbardziej zewnetrzen konce tablicy
