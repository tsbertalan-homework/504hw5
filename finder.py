def isPositive(value):
    if value > 0:
        return True
    else:
        return False

def findroots(x, dx):
    '''
    Search forward from 0, recording places where sign changes.
    '''
    indices = []
    for i in range(1, len(dx)):
        if isPositive(dx[i]) != isPositive(dx[i-1]):
            indices.append(i)
    roots = [x[i] for i in indices]
    return roots
