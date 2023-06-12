def sumEvenFibonacci(n):
    count = 1
    t1 = 1 # First starting term of fibonacci sequence
    t2 = 2 # Second starting term of fibonacci sequence
    t3 = 0
    sum = 0
    if n >=2:
        sum = 2
    while count < n and t3 < 4000000: # Program designed to terms less than 4 million (can be modified)
        t3 = t1+t2 # Next term in a fibonacci sequnce is the sum of the previous two terms
        if t3 % 2 == 0: # Check whether the current term is even or not
            sum += t3
        t1,t2 = t2,t3 # Updating the values of the last two terms
        count +=1 
    return sum

# Test cases
print(sumEvenFibonacci(32)) # Expected 4613732