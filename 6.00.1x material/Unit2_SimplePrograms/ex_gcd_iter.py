def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    compare = 0
    if a > b:
        compare = a
    else:
        compare = b
    for n in range(compare)[::-1]:
        if a % n == 0 and b % n == 0:
            return n

print(gcdIter(9,12))