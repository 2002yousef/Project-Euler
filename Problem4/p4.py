def largestPalindrome(n): # n is the number of digits of the two numbers
    palindrome = [] # 
    for num1 in range(10**(n), 10**(n-1),-1): # ex: if n = 2, then it computes numbers between 100 and 10 since these are only 2 digits
        for num2 in range(10**(n), 10**(n-1),-1): # -1 in both for loops is to create a decrementing loops since we are looking for the largest value
            result = num1 * num2
            if isPalindrome(result):
                palindrome.append(result)
    return max(palindrome)


def isPalindrome(n):
    if(str(n) == str(n)[::-1]): # palindrome check
        return True
    else:
        return False
    
# Test cases
print(largestPalindrome(1)) # Expected 9
print(largestPalindrome(2)) # Expected 9009
print(largestPalindrome(3)) # Expected 906609