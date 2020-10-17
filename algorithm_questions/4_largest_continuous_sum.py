# Problem: Given an array of integers (positive and negative) find the largest continuous sum.

# O(N^3)
# We find all contiguous subarrays in the arr
def find1(arr):
    max_sum = arr[0]
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            s = 0
            for k in range(i, j + 1):
                s += arr[k]

            max_sum = max(max_sum, s)

    return max_sum

# O(N^2)
# We find all contiguous subarrs. in arr but we don't
# duplicate sum operation from scratch


def find2(arr):
    max_sum = arr[0]

    for i in range(len(arr)):
        s = 0
        for j in range(i, len(arr)):
            s += arr[j]

            max_sum = max(max_sum, s)

    return max_sum


# O(N)
# The best solution cause it's linear time complexity solution
def find3(arr):
    max_sum = arr[0]
    max_sum_so_far = arr[0]

    for i in range(1, len(arr)):
        max_sum = max(max_sum + arr[i], arr[i])

        # When for loop ends, adding the last num to max_sum can be
        # less than max_sum_so_far. So that we use;
        max_sum_so_far = max(max_sum, max_sum_so_far)

    return max_sum_so_far


print(find3([1, 2, -1, 3, 4, -1]))
print(find3([1, 2, -1, 3, 4, 10, 10, -10, -1]))
print(find3([-1, 1]))
print(find3([1, 2, 3, 4, 5, 6]))
