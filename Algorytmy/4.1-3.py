import math
from timeit import default_timer as timer
A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 13, -4 ,7, -4, -8, 12, 35, 100, 14, -25, 43, -2, -89, 54, 45, -32, -29, 30, 45, -42, -3, 3, 2, -4, 52, -3, 0, 40]
B = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 13, -4 ,7, -4, -8]
C = [13, -3, -25, 100, -3, -16, -23, 18, 20, -7, 12, -5, -22, 13, -4 ,7, -4, -8]
MINUS_INF = float("-inf")

def find_max_subarray_wrap(A, low, high):
    if high > 30:
        find_maximum_subarray(A, low, high)
    else:
        find_max_subarray_force(A)
def find_max_subarray_force(A):
    sum = MINUS_INF
    for i in range(len(A)):
        tmp_sum = A[i]
        for j in range(i+1, len(A)):
            tmp_sum = tmp_sum + A[j]
            if tmp_sum > sum:
                sum = tmp_sum
                left = i
                right = j
    return (left, right, sum)

def find_max_crossing_subarray(A, low, mid, high):
    global max_left, max_right
    max_left, max_right = 0, 0
    left_sum = MINUS_INF
    sum = 0
    for i in range(mid, low, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = MINUS_INF
    sum = 0
    for j in range(mid+1, high):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)


def find_maximum_subarray(A, low, high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = math.floor((low + high)//2)
        (left_low, left_high, left_sum) = find_maximum_subarray(A, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(A, mid+1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)


start_force = timer()
print(find_max_subarray_wrap(A, 0, 17))
end_force = timer()
start_recursive = timer()
print(find_maximum_subarray(C, 0, 17))
end_recursive = timer()

print(f"rozwiazanie silowe: {end_force - start_force}")
print(f"rozwiazanie rekurencyjne: {end_recursive - start_recursive}")
