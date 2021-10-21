    arr = [11, 10 ,9 ,0 ,2 ,1 ,8 ,6 ,7 ,3 ,4 ,5, 12, 14, 13]   # n = 4 ,  m = 3

def insertionSort(arr, stop):
    for i in range(1, stop):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

def sortUnsorted(arr, n):
    m=len(arr)//n
    for i in range(0, len(arr), m):
        insertionSort(arr, i+m)
    for j in range(0, len(arr)-m, m):
        for k in range(j, len(arr)-m, m):
            if arr[k] > arr[k+m]:
                arr[:k+m], arr[k+m:k+2*m] = arr[k+m:k+2*m], arr[:k+m]
    return arr

print(sortUnsorted(arr, 4))
