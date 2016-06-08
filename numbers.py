import math

digit = input('Enter a series of single digit numbers with no spaces: ')

def numbers(digit):
    sum = 0
    for i in (digit):
        sum = sum + int(i)
    return sum


sum = numbers(digit)
print ("The sum is: ", sum)
