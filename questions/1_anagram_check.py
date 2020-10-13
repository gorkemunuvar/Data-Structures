# Problem: Given two strings, check to see if they are anagrams. An anagram is
# when the two strings can be written using the exact same letters (so you can
# just rearrange the letters to get a different phrase or word).

def anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    letters = {}
    for char in s1:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    for char in s2:
        if not char in letters:
            return False
        else:
            if not s2.count(char) == letters[char]:
                return False

    return True


print(anagram('dog', 'god'))                            # True
print(anagram('clint eastwood', 'old west action'))     # True
print(anagram('aa', 'bb'))                              # False
print(anagram('stressed ', 'desserts'))                 # True
print(anagram('dormitory', 'dirty room'))               # True
print(anagram('yo yo ye', "yosufdu"))                   # False
