def isPrime(num, primes):
    i = 0
    while primes[i]**2 <= num:
        if num % primes[i] == 0: return False
        i += 1
    return True

x, primes = 6, [2,3,5]
while len(primes) < 10001:
    if isPrime(x, primes): primes.append(x)
    x += 1
print(primes[-1])