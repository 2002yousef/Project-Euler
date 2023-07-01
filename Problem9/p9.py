''' 
A pythagorean triplet has the property {2*m*n, m^2 - n^2, m^2 + n^2}, where the first two terms can be any legs of the triangle and the last term is the hypotenuse and m > n.
The goal is to find a triplet such that the sum of the three legs is equal a target sum which is passed to the function.
By adding the three terms, m^2 + nm - sum = 0 is reached
Then m is made the subject of formula using the quadratic formula
'''

def pythagorasSum(sum):
    m = 0
    n = 0
    for n in range(sum):
        m = (-n + (n**2 +2 * sum)**0.5) / 2
        if m - int(m) == 0:
            break
    
    a = 2 * m *n
    b = m**2 - n**2
    c = m**2 + n**2

    return int(a)*int(b)*int(c)

# Test cases
print(pythagorasSum(1000)) # Expected 31875000