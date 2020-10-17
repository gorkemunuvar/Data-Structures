# Problem: Given an integer array, output all the unique 
# pairs that sum up to a specific value k.

# O(N^2)
def first_pair_sum(arr, k):
    if len(arr) < 2:
        return 0

    counter = 0
    for i in range(len(arr) - 1):         # n step
        for j in range(i + 1, len(arr)):  # n-j = n step
            if arr[i] + arr[j] == k:
                counter += 1

    return counter

# O(N) - Better solution
def second_pair_sum(arr, k):
    if len(arr) < 2:
        return 0

    # Sets for tracking
    seen = set()
    counter = 0

    for number in arr:
        target = k - number

        if target in seen:
            counter += 1
        else:
            seen.add(number)

    return counter


print(second_pair_sum([1, 3, 2, 2, 2], 4))  # 2
print(second_pair_sum([1, 2, 3, 1], 3))     # 1
print(second_pair_sum([1, 9, 2, 8, 3, 7, 4,
                       6, 5, 5, 13, 14, 11, 13, -1], 10))  # 6
