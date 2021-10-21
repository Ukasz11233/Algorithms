def hash_search(arr, key):
    i=0
    while arr[j] == None or i <= len(arr):
       j = (key+i)%len(arr)
       if arr[j] is key:
           return j
       else:
           i+=1
    return None

def hash_insert(arr, key):
    i=0
    while i <= len(arr):
        j = (k+i)%len(arr)
        if arr[j] is None:
            T[j] = key
            return j
        else:
            i+=1
    print("Przepelnienie tablicy z haszowaniem")
    return