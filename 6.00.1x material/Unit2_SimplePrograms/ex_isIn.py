def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) //2 == 0:
        return False
    if char == aStr[len(aStr) // 2]:
        return True
    if char > aStr[len(aStr) // 2]:
        return isIn(char,aStr[len(aStr) //2:])
    else:
        return isIn(char,aStr[:len(aStr) //2])

print(isIn('w', 'bcdghopuvw'))