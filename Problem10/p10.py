from eulerlib import primes

def sumPrimes(n):
    return sum(primes(n))

# Test cases
print(sumPrimes(10)) # Expected 17
print(sumPrimes(2000000)) # Expected 142913828922