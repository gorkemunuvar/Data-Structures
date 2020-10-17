# Problem: Consider an array of non-negative integers. A second array is formed by shuffling
# the elements of the first array and deleting a random element. Given these two arrays,
# find which element is missing in the second array.

import collections

# O(N)
# But this way is not work correctly cause
# arrays can have duplicate numbers.
def finder1(arr1, arr2):
    for num in arr1:
        if num not in arr2:
            print(f"{num} is missing")
            return

    print("No missing element.")

# O(N)
def finder2(arr1, arr2):
    # Using defaultdict to avoid missing key errors
    dict_nums = collections.defaultdict(int)

    for num in arr2:
        dict_nums[num] += 1

    for num in arr1:
        if dict_nums[num] == 0:
            print(f"{num} is missing.")
            return
        else:
            dict_nums[num] -= 1

# O(N)
# Using XOR to find missing element.
# A XOR A = 0. So when we iterate all the numbers
# of arr1 and arr2 we'll find the missing el.
def finder3(arr1, arr2):
    result = 0

    for num in arr1 + arr2:
        result ^= num

    print(result)


# Another solution: Also we could sort arr1 and arr2 and then we
# could iterate and compare all the numbers. When a comparing is
# false, it is the missing element. But time complexity of sort()
# func. is O(nlogn). That's why it's not a good solution.

finder3([5, 5, 7, 7], [5, 7, 7])                    # 5 is missing
finder3([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])  # 5 is missing
finder3([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1])  # 6 is missing
