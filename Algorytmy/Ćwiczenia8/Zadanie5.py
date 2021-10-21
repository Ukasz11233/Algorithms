W = [[1, 2, 3, 4], [1, 2, 2, 1], [1, 4, 2], [1, 1, 1, 1, 1, 1, 1, 1, 3, 3], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2], [5], [4]]

A = [1]
def StealBlock(W, A):
    n = len(W)
    T = [0]*n
    our_tower = 0

    for el in A:
        our_tower += el
    max_block = 0

    for i in range(n):
        for el in W[i]:
            T[i] += el
            if max_block < el:
                max_block = el
    max_tower_idx, max_tower = 0, 0

    while our_tower <= max_tower:
        bool = False
        for i in range(n):
            if T[i] > max_tower:
                max_tower = T[i]
                max_tower_idx = i

        for el in W[max_tower_idx]:
            if el == max_block:
                bool = True

        if bool == True:
            T[max_tower_idx] -= max_block
            our_tower += max_block
        else:
            max_block_in_max_tower = 0
            for el in W[max_tower_idx]:
                if max_block_in_max_tower < el:
                    max_block_in_max_tower = el
            if max_block_in_max_tower
print(StealBlock(W, A))