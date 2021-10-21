A = [13, -3, -25, 100, -3, -16, -23, 18, 20, -7, 12, -5, -22, 13, -4 ,7, -4, -8]

def find_max_subarray(A):
    sum = float("-inf")
    sum_min = float("inf")
    tmp_sum = 0
    for i in range(len(A)):
        tmp_sum = tmp_sum + A[i]
        if tmp_sum > sum:
            sum = tmp_sum
            max_right = i
    tmp_sum = 0
    for j in range(max_right+1):
        tmp_sum = tmp_sum + A[j]
        if tmp_sum < sum_min:
            sum_min = tmp_sum
            max_left = j
    return max_left+1, max_right , sum - sum_min

print(find_max_subarray(A))