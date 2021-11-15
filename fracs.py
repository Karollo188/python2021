import math

def tearDown(frac):
    if frac[0] == 0 and frac[1] != 0:
        frac[1] = 1
    return [frac[0]/math.gcd(frac[0],frac[1]),frac[1]/math.gcd(frac[0],frac[1])]

def add_frac(frac1, frac2):  # frac1 + frac2
    return tearDown([(frac1[0]*frac2[1] + frac2[0]*frac1[1]),frac1[1]*frac2[1]])

def sub_frac(frac1, frac2):        # frac1 - frac2
    return tearDown([(frac1[0]*frac2[1] - frac2[0]*frac1[1]),frac1[1]*frac2[1]])

def mul_frac(frac1, frac2):        # frac1 * frac2
    return tearDown([frac1[0]*frac2[0],frac1[1]*frac2[1]])

def div_frac(frac1, frac2):        # frac1 / frac2
    return tearDown([frac1[0]*frac2[1],frac1[1]*frac2[0]])

def is_positive(frac):             # bool, czy dodatni
    if frac[0]/frac[1] > 0:
        return True
    else:
        return False

def is_zero(frac): # bool, typu [0, x]
    if frac[0] == 0:
        return True
    return False

def cmp_frac(frac1, frac2): # -1 | 0 | +1
    if frac1[0]/frac1[1] > frac2[0]/frac2[1]:
        return 1
    elif frac1[0]/frac1[1] < frac2[0]/frac2[1]:
        return -1
    return 0

def frac2float(frac): # konwersja do float
    return frac[0] / frac[1]


f1 = [-1, 2]                  # -1/2
f2 = [0, 1]                   # zero
f3 = [3, 1]                   # 3
f4 = [6, 2]                   # 3 (niejednoznaczność)
f5 = [0, 2]                   # zero (niejednoznaczność)

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([1, 2], [1, 2]), [1, 1])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1,2], [1,3]), [1,6])
        self.assertEqual(sub_frac([1,2], [1, 1]), [-1, 2])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1,2], [1,3]), [1,6])
        self.assertEqual(mul_frac([1,3], [1, -3]), [1, -9])

    def test_div_frac(self):
        self.assertEqual(div_frac([1,2], [1,3]), [3,2])
        self.assertEqual(div_frac([1,2], [1,4]), [2,1])
        self.assertEqual(div_frac([1,2], [1,5]), [5,2])


    def test_is_positive(self):
        self.assertEqual(is_positive([1,2]), True)
        self.assertEqual(is_positive([1,-2]), False)

    def test_is_zero(self):
        self.assertEqual(is_zero([0,3]), True)
        self.assertEqual(is_zero([1,3]), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1,2],[2,4]), 0)
        self.assertEqual(cmp_frac([1,2],[1,4]), 1)
        self.assertEqual(cmp_frac([1,4],[1,2]), -1)


    def test_frac2float(self):
        self.assertEqual(frac2float([1,2]), 0.5)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy