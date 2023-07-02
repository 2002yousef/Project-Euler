def power(base, exp):
    return base ** exp # returns base ^ exp

# takes a number and converts it to an array made of its digits, 123 -> [1,2,3]
def stringToArr(num):
    numStr = str(num)
    numArr = [] 
    for val in numStr:
        numArr.append(int(val))

    return numArr

def powerDigitSum(base,exp):
    result = power(base,exp)
    resultArr = stringToArr(result)
    return sum(resultArr) # Calculates the sum of values in an array

# Test cases
print(powerDigitSum(2,15)) # Expected 26
print(powerDigitSum(2,1000)) # Expected 1366