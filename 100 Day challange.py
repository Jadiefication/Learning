import unittest
from math import factorial

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
class TestFactorial(unittest.TestCase):

    def test_zero(self): 
        self.assertEqual(factorial(0), 1)

    def test_positive(self): 
        self.assertEqual(factorial(5), 120)

    def test_negative(self): 
        with self.assertRaises(ValueError): factorial(-5)

    def test_float(self): 
        with self.assertRaises(TypeError): factorial(5.5)

    def test_string(self): 
        with self.assertRaises(TypeError): factorial("five") [1]

    def test_large_number(self): 
        self.assertEqual(factorial(15), 1307674368000)

if __name__ == '__main__':
  unittest.main()