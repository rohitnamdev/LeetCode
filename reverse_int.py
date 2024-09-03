# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 
def reverse(x):
    if -2**31 <= x <= 2**31 - 1 or x==0:
        return 0
    if x < 10 and x > 0:
        return x
    strx = str(x)
    if x>0:
        return int(strx[::-1])
    else:
        temp = int(strx[:0:-1])
        return 0-temp
print(reverse(123))

