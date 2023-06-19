# Largest Prime Factor
This is a Python algorithm that finds the largest prime factor of a given number. It utilizes the trial division method to determine the prime factors of the number and then returns the largest prime factor found

## Explanation
1. Starting by the smallest prime number,2, the number is divided by 2 and if there is no remainder, the number is kept divided by 2
2. If the number is not divided by 2, the factor is incremented by 1. Only prime numbers will work afterwards since we divided by 2 or 3 in the beginning
3. The prime factors are appended to an array
4. The function LPF, largest prime factor, takes the positive integer, creates the array of prime factors and returns the maximum value in the array