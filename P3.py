import math

def find_dev(num):
    for x in range(2, math.floor(math.sqrt(num)), 1):
        if num % x == 0:
            return x
    return 0

print(find_dev(13195))