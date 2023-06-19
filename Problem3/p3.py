def LPF(n): #LPF: largest prime factor
    primeFactors = [] # An empty array that will hold the prime factors
    currentFactor = 2 # The smallest prime number
    while n > 1:
        while n % currentFactor == 0: # Checking whether current factor is a factor of n
            primeFactors.append(currentFactor)
            n /= currentFactor
        currentFactor += 1
    return max(primeFactors) # returning the maximum value in the array

# Test Cases
print(LPF(5)) # Expected 5
print(LPF(35)) # Expected 7
print(LPF(26)) # Expected 13
print(LPF(1892)) # Expected 43
print(LPF(13195)) # Expected 29
print(LPF(600851475143)) # Expected 6857
