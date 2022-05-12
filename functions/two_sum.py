def twoSum(n, t):
    '''Finds which two numbers in a list of numbers add up to the given target.'''
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if n[j] == t - n[i]:
                return [i, j]
