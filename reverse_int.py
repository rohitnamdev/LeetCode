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

