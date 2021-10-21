pattern = 'you_should_not'
text = 'thou_shall_not'

A = "ABCBD"
B = "BACBF"

def match(char1, char2):
    if char1 == char2:
        return 0
    else:
        return 1


def BottomUp(pattern, text):
    pattern_len = len(pattern) + 1
    text_len = len(text) + 1
    D = [[0]*(pattern_len) for _ in range(text_len)]
    T = [[0]*(pattern_len) for _ in range(text_len)]
    for j in range(pattern_len):
        D[0][j] = j
    for i in range(text_len):
        D[i][0] = i

    for i in range(1, text_len):
        for j in range(1, pattern_len):
            opt4 = opt1 = D[i-1][j-1] + match(pattern[j-1], text[i-1])
            opt2 = D[i-1][j] + 1
            opt3 = D[i][j-1] + 1

            if i > 1 and j > 1 and match(pattern[j-2], text[i-1]) == 0 and match(pattern[j-1], text[i-2]) == 0:
                opt4 = D[i-2][j-2] + 1

            D[i][j] = opt1
            T[i][j] = 1
            if D[i][j] > opt2:
                D[i][j] = opt2
                T[i][j] = 2
            if D[i][j] > opt3:
                D[i][j] = opt3
                T[i][j] = 3
            if D[i][j] > opt4:
                D[i][j] = opt4
                T[i][j] = 4

    reconstruct_path(T, pattern, text, i, j)
    print("")
    return D[-1][-1]


def reconstruct_path(T, pattern, text, i, j):
    if T[i][j] == 0:
        return

    if T[i][j] == 1:
        reconstruct_path(T, pattern, text, i-1, j-1)
        if pattern[j-1] == text[i-1]:
            print("M", end=" ")
        else:
            print("S", end=" ")
    if T[i][j] == 2:
        reconstruct_path(T, pattern, text, i-1, j)
        print("D", end=" ")
    if T[i][j] == 3:
        reconstruct_path(T, pattern, text, i, j-1)
        print("I", end=" ")
    if T[i][j] == 4:
        reconstruct_path(T, pattern, text, i-2, j-2)
        print("SW", end=" ")


print(BottomUp(A, B))