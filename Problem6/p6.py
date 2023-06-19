def sumSquares(n): 
    return (n/6)*(n+1)*(2*n+1)
# 1^2 + 2^2 + 3^2 + 4^2 + .... + n^2
# Formula can be found in the README.md file

def squareSums(n):
    sum = (n/2)*(n+1)
    return sum ** 2
# (1 + 2 + 3 + 4 + .... + n)^2
# Formula can be found in the README.md file

def sumSquareDifference(n):
    return int(squareSums(n) - sumSquares(n))
# Square of sums - sum of squares

# Test cases
print(sumSquareDifference(10)) # Expected 2640
print(sumSquareDifference(100)) # Expected 25164150

