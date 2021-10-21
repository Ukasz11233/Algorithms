A = 'aabc'
B = 'bcaa'

def AnagramCheck(A, B, k):
    if len(A) != len(B):
        return False
    n = len(A)
    K = [0 for _ in range(k)]
    for i in range(n):
        K[ord(A[i])%97] += 1
        K[ord(B[i])%97] -= 1
    for i in range(n):
        if K[ord(A[i])%97] != 0:
            return False
    return True

print(AnagramCheck(A, B, 3))
