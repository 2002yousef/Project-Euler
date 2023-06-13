def isPrime(n):
    for number in range(2,n):
        if n % number == 0:
            return False
    return True
    
    
def largestPrime(n):
    maxPrime = 0
    for number in range(2,n):
        if n % number == 0 and isPrime(number) and number > maxPrime:
            maxPrime = number
    return maxPrime

print(largestPrime(5))
print(largestPrime(35))
print(largestPrime(26))
print(largestPrime(13195))
print(largestPrime(600851475143))