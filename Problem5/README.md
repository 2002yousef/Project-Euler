# Smallest Multiple
This is a Python algorithm that finds the smallest multiple of numbers from 1 to n<br/>
For example: $2520$ is the smallest multiple of numbers from 1 to 10.<br/>
The algorithm uses the concept of LCM * GCF = N1 * N2, where LCM is the lowest common multiple, GCF is the greatest common factor and N1 and N2 are two numbers. 

## Steps
1. An array or list of numbers from 1 to n is declared
2. A variable, declared as multiple, is initialized with the value 1
3. The lcm of the first two elements of the array is found
4. The variable multiple holds the value of this lcm
5. The lcm is now calculated from the new value of multiple and the next element in the array
6. Steps 4 and 5 are repeated until the last element in the array

## Disclaimer
Two test cases are provided at the end of the code