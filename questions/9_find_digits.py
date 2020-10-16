#HackerRank Problem: https://www.hackerrank.com/challenges/find-digits/problem

#O(N)
def find_digits(n):
    divisors = 0

    for digit in str(n):
        if digit == "0":
            continue

        if n % int(digit) == 0:
            divisors += 1
        
    return divisors

print(find_digits(12))
print(find_digits(1012))