X = [0.25, 0.5, 1.6]

def UnitIntervsls(X):
    result = 1
    n = len(X)
    interval = X[0]
    for i in range(1, n):
        if X[i] > interval + 1:
            interval = X[i]
            result += 1

    return result

print(UnitIntervsls(X))