# Problem. Given a string, determine if it is comprised of all unique characters.
# For example, the string 'abcde' has all unique characters and should return
# True. The string 'aabcde' contains duplicate characters and should return false.

# O(N)
def test(string):
    length = len(string)

    if length == 0 or length == 1:
        return True

    last_char = string[0]

    for i in range(1, length):
        if string[i] == last_char:
            return False

        last_char = string[i]

    return True

# O(N)
# Another solution
def unique_char(string):
    seen = set()

    for char in string:
        if char in seen:
            return False
        
        seen.add(char)

    return True

print(unique_char(''))
print(unique_char('goo'))
print(unique_char('abcdefg'))
print(unique_char('ABCDEFG'))
print(unique_char('ABCCDEFG'))
