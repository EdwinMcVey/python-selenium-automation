"""
When a user enters a number n, find the sum of digits in all numbers from 1 to n.
Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
"""
n = int(input('Input your number: '))

def sumOfDigits(sum):

    sum = (n*(n+1)/2)

    return sum

print("Sum of digits in numbers from 1 to", n, "is", sumOfDigits(sum))

