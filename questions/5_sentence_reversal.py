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

def rev_word2(string):
    words = []
    last = " "
    word = ""

    #code here

    return " ".join(reversed(arr))

print(rev_word2('This is the best'))


print(rev_word2('Hello     John    how are you   '))
