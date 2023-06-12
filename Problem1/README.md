# Multiples of 3 and 5
If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.

## Approach
The problem is approached using arithmetic series broken up to 3 steps
Arithmetic series rule: n/2(2a + (n-1)d) where a is the first term, d is the difference and n is the number of terms

## Step 1
1. We find how many multiples of 3 up to term n
2. We find how many multiples of 5 up to term n
3. We find how many multiples of 15 up to term n, since these are common multiples that have been previosly computed

## Step 2
1. We calculate the sum of multiples of 3
2. We calculate the sum of multiples of 5
3. We calculate the sum of multiples of 15

## Step 3
We add the sum of multiples of 3 and 5 then deduct the sum of multiples of 15

## Disclaimer
2 test cases are provided at the end of the code