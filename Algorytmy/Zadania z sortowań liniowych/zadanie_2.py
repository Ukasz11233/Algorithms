A = ["aaa", "aaab", "aba", "aabba", "abbaa", "bbb"]

#aabba, abbaa


def CSS(B, exp):
    output = [0]*len(B)
    counting = [0]*26     #bo tyle jest liczb w alfabecie
    for i in range(len(B)):
        counting[ord(B[i][exp])%26] +=1
    for i in range(1, len(counting)):
        counting[i] += counting[i-1]
    for i in range(len(B)-1, -1, -1):
        idx = ord(B[i][exp])%26
        output[counting[idx] - 1] = B[i]
        counting[idx] -= 1
    for i in range(len(B)):
        B[i] = output[i]


def RadixStrings(B):
    max1 = len(B[0]) # wszyystkie stringi w danym buckecie maja taka sama dlugosc
    exp = max1 - 1
    while exp >= 0:
        CSS(B, exp)
        exp -=1
    return B

def SortStrings(A):
    buckets = [ [] for _ in range(len(A))]
    for str in A:
        bucket_idx = len(str)
        buckets[bucket_idx].append(str)

    for i in range(len(A)):
        if len(buckets[i]) > 0:
            print(buckets[i])
            buckets[i] = RadixStrings(buckets[i])
    k = 0
    for i in range(len(A)):
        for j in range(len(buckets[i])):
            A[k] = buckets[i][j]
            k+=1
    return A

print(SortStrings(A))