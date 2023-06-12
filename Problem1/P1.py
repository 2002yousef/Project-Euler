def multiples_of_3_and_5(n):
    terms3 = int(n / 3) # Find how many multiples of 3 up to n
    terms5 = int(n / 5) # Find how many multiples of 5 up to n
    terms15 = int(n / 15) # Find how many multiples of 15 (common multiples of 3 and 5) up to n

    # The number n is excluded 
    if n % 3 == 0:
        terms3-=1

    if n % 5 == 0:
        terms5-=1
    
    if n % 15 == 0:
        terms15 -=1

    # Using arithmetic series rule to find the sum of multiples
    # n/2(2a + (n-1)d) a= first term, d= difference, n = number of terms
    sum3 = (terms3/2)*(2 * 3 + (terms3 -1)*3)
    sum5 = (terms5/2)*(2 * 5 + (terms5 -1)*5)
    sum15 = (terms15/2)*(2 * 15 + (terms15 -1)*15)

    total = sum3 + sum5 - sum15 # multiples of 15 shall be deducted since they are already found in multiples of 3 and 5
    return int(total)

# Test cases
print(multiples_of_3_and_5(10)) # expected 23
print(multiples_of_3_and_5(1000)) # expected 233168

