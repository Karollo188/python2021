import numpy as np
import math
import random

def solve1(a,b,c):
    #prosta, płaszczyzna lub równanie sprzeczne
    if a == 0 and b == 0 and c != 0:
        return "rownanie sprzeczne"
    elif a == 0 and b == 0 and c == 0:
        return "płaszczyzna"
    elif a != 0 and b == 0:
        return  "prosta pionowa"
    elif a == 0 and b != 0 and c != 0:
        return "posta pozioma y = " + str(c)
    elif a == 0 and b != 0 and c == 0:
        return "prosta pozioma y = 0"
    else:
        return "prosta o rownaniu y = " + str(-a/b) + "x + " + str(-c/b)


def calc_pi(n=100):
    #obliczanie pi metoda monte carlo
    sum = 0
    for i in range(n):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        x = x * x
        y = y * y
        if (x + y < 1):
            sum += 1
    r = n / 4
    return sum / r

print("pi = " + str(calc_pi(100)))


def heron(a, b, c):
    # """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    # Herona. Długości boków trójkąta wynoszą a, b, c."""
    if a + b < c or a + c < b or b + c < a:
        raise ValueError
    s = a + b + c
    s = s / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

print(heron(1,1,1))




# P(0, 0) = 0.5,
# P(i, 0) = 0.0 dla i > 0,
# P(0, j) = 1.0 dla j > 0,
# P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0.

a = 10
b = np.zeros((a,a))
for i in range(1, a):
    b[0, i] = 1

for i in range(1,a):
    for j in range(1,a):
        b[i, j] = 0.5 * (b[i -1, j] + b[i, j - 1])

print(b)

