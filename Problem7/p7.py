# Checks whether the passed number is prime or not
def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

# Generates the next prime number after the prime passed
def generatePrime(last):
    number  = last+1
    while isPrime(number) == False:
        number +=1    
    return number

# Creates an array of n prime numbers and returns the last prime number in the array
def nthPrime(n):
    primes = [2]
    count = 0
    while len(primes) < n:
        primes.append(generatePrime(primes[count]))
        count +=1
    return primes[-1]

# Test cases
print(nthPrime(6)) # Expected 13
print(nthPrime(10001)) # Expected 104743