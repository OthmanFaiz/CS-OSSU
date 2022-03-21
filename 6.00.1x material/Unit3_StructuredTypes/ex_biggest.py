animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

aDict = {'u': []}


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    bkey = None
    for key in aDict:
        if bkey is None:
            bkey = key
        elif len(aDict[key]) > len(aDict[bkey]):
            bkey = key
    return bkey


print(biggest(aDict))