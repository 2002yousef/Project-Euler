def longestCollatzSequence(n):
    previousSequence = collatz(n)
    dictionary = {n:len(previousSequence)}
    for i in range(2,n):
        if i in previousSequence:
            dictionary[i] = len(previousSequence) - previousSequence.index(i)
        else:
            previousSequence = collatz(i)
            dictionary[i] = len(previousSequence)
    return max(dictionary, key = dictionary.get)
        

def collatz(n):
    sequence = []
    while n != 1:
        if n%2 == 0:
            n /= 2
            sequence.append(n)
        else:
            n = 3 * n + 1
            sequence.append(n)
    return sequence

print(longestCollatzSequence(1000000))