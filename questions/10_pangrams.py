# HackerRank Problem: https://www.hackerrank.com/challenges/pangrams/problem

letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

# O(N)
def pangrams(string):
    string = string.replace(" ", "")
    string = string.lower()

    for letter in letters:
        if not letter in string:
            return 'not pangram'

    return 'pangram'

# One line solution
def pangrams2(s):
    return "pangram" if len(set([x.upper() for x in s if x != ' '])) == 26 else "not pangram"


print(pangrams('a'))  # not pangram
print(pangrams('The quick brown fox jumps over the lazy dog'))  # pangram
print(pangrams('We promptly judged antique ivory buckles for the next prize'))  # pangram
print(pangrams('We promptly judged antique ivory buckles for the prize'))  # not pangram
