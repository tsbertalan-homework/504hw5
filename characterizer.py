import numpy as np
from scipy import sqrt  # this will handle complex numbers
from finder import isPositive

def findCharacter(x, y, a, b, g):
    (eig1, eig2) = eigenvalues(x, y, a, b, g)
    characters = []
    if eig1.real < 0 and eig2.real < 0:
        characters.append('stable')
    if isPositive(eig1.real) != isPositive(eig2.real):
        characters.append('saddle')
    if discriminant(x, y, a, b, g) < 0:
        characters.append('oscillatory')
    return ', '.join(characters)

def oldFindCharacter(x, y, a, b, g):
    t = trace(x, y, a, b, g)
    d = det(x, y, a, b, g)
    D = t ** 2 - 4 * d
    # cases from page 123 of math book
    characters = []
    if t < 0 and d > 0:
        characters.append('stable node')
    if D > 0 and d < 0:
        characters.append('saddle point')
    if D == 0:
        characters.append('dependent eigenvectors')
    if D < 0 and d > 0:
        characters.append('complex eigenvalues')
    return ','.join(characters)

def trace(x, y, a, b, g):
    return -2 + a * f(y, g) * (b*g*(1 - x) - 1)

def det(x, y, a, b, g):
    return -a * b * g * (1 - x) * f(y, g) + a * f(y, g)

def f(y, g):
    return np.exp(y / (1 + y/g))

def eigenvalues(x, y, a, b, g):
    A = Af(x, y, a, b, g)
    B = Bf(x, y, a, b, g)
    C = Cf(x, y, a, b, g)
    _a = 1
    _b = -B + -A
    disc = discriminant(x, y, a, b, g)
    eig1 = (-_b + sqrt(disc)) / 2 / _a
    eig2 = (-_b - sqrt(disc)) / 2 / _a
    return (eig1, eig2)

Af = lambda x, y, a, b, g: -1 - a * f(y, g)
Bf = lambda x, y, a, b, g: -1 + a * b * g * (1 - x) * f(y, g)
Cf = lambda x, y, a, b, g: a ** 2 * f(y, g) ** 2 * (1 - x) * b * g

def discriminant(x, y, a, b, g):
    A = Af(x, y, a, b, g)
    B = Bf(x, y, a, b, g)
    C = Cf(x, y, a, b, g)
    _a = 1
    _b = -(B + A)
    _c = A * B + C
    return _b ** 2 - 4 * _a * _c
