# Given a string of words, reverse all the words. For example:
# input: 'This is the best'
# output: 'best the is This'

# O(N)
def rev_word1(string):
    string = string.strip()
    arr = string.split()

    # We could use a linear loop
    # Also complexity of built-in reversed func. is O(N)
    # It's better to use a built-in func.
    return " ".join(reversed(arr))


# O(N)
# Manually removing spaceses from string
def rev_word2(string):
    char_bool = False
    if string[0] != " ":
        char_bool = True

    words = []
    start_index = 0
    ending_index = 0
    for i in range(len(string)):
        if char_bool == False and string[i] != " ":
            char_bool = True
            start_index = i

        elif (char_bool == True and string[i] == " "):
            char_bool = False
            ending_index = i
            words.append(string[start_index: ending_index])

        elif char_bool == True and i == len(string) - 1:
            words.append(string[start_index: i + 1])

    return " ".join(reversed(words))

# More readable than rev_word2
# Manually removing spaceses from string
def rev_word3(string):
    i = 0
    length = len(string)

    words = []
    while i < length:
        if string[i] != " ":
            word = ""
            while i < length and string[i] != " ":
                word += string[i]
                i += 1

            words.append(word)
        i += 1

    return " ".join(reversed(words))

print(rev_word3('Hello     John    how are you'))


print(rev_word3('Hello'))
print(rev_word3('    space before'))
print(rev_word3('   This    is  the   best'))
print(rev_word3('space after        '))
