# Nth Prime
A prime number has no other factors than 1 and itself. <br/>
If we list the first 6 prime numbers, 2,3,5,7,11,13, 13 is the 6th prime number.<br/>
This python algorithm takes a value n and returns the nth prime number.

## Steps
1. The function isPrime takes a number and checks whether it is prime or not by dividing it with all numbers from 2 to itself - 1.
2. If the function returns false, then the passed number is not prime, else it will return true.
3. The function generatePrime takes a number and generates the next prime number after it.
4. The function nth prime creates an array with the first prime number 2.
5. It calls the function generatePrime and appends the generated prime number to the array
6. It returns the last number in the array

## Disclaimer
Two test cases are provided at the end of the code.