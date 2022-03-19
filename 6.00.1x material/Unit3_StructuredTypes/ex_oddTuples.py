# Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, where every other element of the input tuple is copied, starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    temp = ()
    oddOnly = 1
    for i in aTup:
        if oddOnly % 2 != 0:
            temp = temp + (i,)
        oddOnly += 1
    return temp


print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))