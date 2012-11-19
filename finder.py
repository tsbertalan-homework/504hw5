def findroots(x, dx):
    '''
    Search forward from 0, recording places where sign changes.
    '''
    def ispositive(value):
        if value > 0:
            return True
        else:
            return False
    indices = []
    for i in range(1, len(dx)):
        if ispositive(dx[i]) != ispositive(dx[i-1]):
            indices.append(i)
    roots = [x[i] for i in indices]
    return roots
