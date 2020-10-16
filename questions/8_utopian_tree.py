# HackerRank Problem
# The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height.
#  Each summer, its height increases by 1 meter. A Utopian Tree sapling with a height of 1 meter
# is planted at the onset of spring. How tall will the tree be after n growth cycles? For example,
#  if the number of growth cycles is n = 5, the calculations are as follows:

# Period  Height
# 0          1
# 1          2
# 2          3
# 3          6
# 4          7
# 5          14

def utopian_tree(n):
    height = 1
    is_spring = True

    print(f"Period: {0}   Height: {height}")

    for i in range(1, n + 1):
        if is_spring:
            height *= 2
        else:
            height += 1

        is_spring = not is_spring

        print(f"Period: {i}   Height: {height}")

    return height


utopian_tree(1)
