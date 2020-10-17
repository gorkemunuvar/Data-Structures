# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become
# 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of
# single or double letters. For instance, it is okay for 'AAB' to return
# 'A2B1' even though this technically takes more space.

# O(n)
# This algorithm known as the Run-Length Compression algorithm
def compress(string):
    length = len(string)

    if len(string) == 0:
        return ""
    
    i = 0
    result = ""
    counter = 0
    last_char = string[0]

    while i < length:
        if string[i] == last_char:
            counter += 1
        else:
            result += last_char + str(counter)
            last_char = string[i]
            counter = 1
        i += 1

    result += last_char + str(counter)
    return result


print(compress(''))
print(compress('A'))
print(compress('AABBC'))
print(compress('AABBCC'))
print(compress('AAABCCDDDDD'))
print(compress('AAAaaa'))
