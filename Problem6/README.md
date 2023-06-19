# Sum Square Difference
This is a python algorithm, which computes the square of sum of the first n positive integers and subtracts from it the sum of the first n squares

## Explanation and Formulae 
1. Sum of squares: $\displaystyle\sum_{k=1}^n k^2 = 1^2 + 2^2 + 3^2 + ... + n^2 = \frac{n(n+1)(2n+1)}{6}$
2. Sum of numbers from 1 to n: $\displayestyle\sum_{k=1}^n k = 1 + 2 + 3 + ... + n = \frac{n(n+1)}{2}$
3. The function square sums computes the sum in step 2 and returns the sum squared as required
4. The function sumSquareDifference subtracts the sum calculated in step 1 from the sum calculated in step 2

## Disclaimer 
Two test cases are provided at the end of the code