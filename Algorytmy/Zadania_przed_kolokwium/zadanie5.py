A = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, None, None, None, None, None]

# zlozonosc to logn

def Find_end(A):
    i = 1
    while A[i] != None:
        i *= 2
    l = i//2
    while l <= i:
        mid = (l+i)//2
        if A[mid] == None:
            i = mid
        elif A[mid] != None and A[mid+1] == None:
            return mid
        else:
            l = mid

print(Find_end(A))