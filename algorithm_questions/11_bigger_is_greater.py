# HackerRank Problem: https://www.hackerrank.com/challenges/bigger-is-greater/problem

letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
           'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
           't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

# T(O^2) and i used sort metdod sort = O(nlogn)
# My solution is really complex.
# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
# In the link above there is a linear solution. Maybe i can optimize my code later.
def bigger_is_greater(word):
    length = len(word)
    rev_word = list(reversed(word))

    ordered = []
    flag = False
    bound = length

    for i in range(1, length):
        ordered.append(rev_word[i - 1])
        ordered.sort()

        for index in range(0, len(ordered)):
            if ordered[index] > rev_word[i]:
                temp = rev_word[i]
                rev_word[i] = ordered[index]
                ordered[index] = temp

                ordered.sort()
                flag = True
                bound = i
                break

        if flag:
            break

    if not flag:
        return "no answer"

    rev_word = "".join(list(reversed(rev_word))[0:length - bound])
    ordered_word = "".join(ordered)
    return rev_word + ordered_word


print(bigger_is_greater('lmno'))
print(bigger_is_greater('dcba'))
print(bigger_is_greater('dcbb'))
print(bigger_is_greater('abdc'))
print(bigger_is_greater('abcd'))
print(bigger_is_greater('fedcbabcd'))
