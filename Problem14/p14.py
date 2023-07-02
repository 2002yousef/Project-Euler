def longestCollatzSequence(n):
    previousSequence = collatz(n)
    dictionary = {n:len(previousSequence)}
    for i in range(2,n):
        if i in previousSequence: # if the current number already exists in a sequence, no need to compute its sequence
            dictionary[i] = len(previousSequence) - previousSequence.index(i)
        else:
            previousSequence = collatz(i)
            dictionary[i] = len(previousSequence)
    return max(dictionary, key = dictionary.get)
        

def collatz(n):
    sequence = []
    while n != 1:
        if n%2 == 0: 
            n /= 2 # if n is even, n is divided by 2
            sequence.append(n)
        else:
            n = 3 * n + 1 # if n is odd, n is multiplied by 3 and 1 is added
            sequence.append(n)
    return sequence

print(longestCollatzSequence(10)) # Expected 9
print(longestCollatzSequence(50)) # Expected 27
print(longestCollatzSequence(1000000)) # Expected 837799