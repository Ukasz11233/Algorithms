A = [5, 3, 4, 2, 3, 2, 1, 1, 5, 3]

class numbers():

    def __init__(self, A):
        self.array = A

    def count_num_in_range(self, a, b):
        k = max(self.array)
        counting = [0] * (k+1)
        for i in range(len(self.array)):
            counting[self.array[i]] += 1
        print(counting)
        for i in range(1, len(counting)):
            counting[i] += counting[i-1]
        print(counting)
        return counting[b] - counting[a]
test = numbers(A)

print(test.count_num_in_range(0, 2))