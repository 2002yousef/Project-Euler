def GCF(n1,n2): # GCF: greatest common factor
    maxFactor = 1
    for i in range(1,min(n1,n2)+1): # +1 if either numbers is a factor of the other, since range is exclusive
        if (n1%i == 0) and (n2%i == 0): # Checks if i is divisible by both numbers
            maxFactor = i
    return maxFactor

def LCM(n1,n2):
    return int(n1*n2/GCF(n1,n2)) # LCM * GCF = N1 * N2

# Explained in README
def smallestMultiple(n):
    multiples = list(range(1,n+1))
    multiple = 1
    for i in range(1,n):
        multiple = LCM(multiple,multiples[i])
    return multiple

# Test cases
print(smallestMultiple(10)) # Expected 2520
print(smallestMultiple(20)) # Expected 232792560