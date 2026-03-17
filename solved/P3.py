import math

def find_dev(num):
    primes = []
    for x in range(2, math.floor(math.sqrt(num))+1):
        while num % x == 0:
            primes.append(x)
            num //= x
    if num > 1: primes.append(num) #added
    return primes[-1]

print(find_dev(600851475143))