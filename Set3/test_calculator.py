import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        result1=Calculator(10,2)
        result2=Calculator(-1,1)
        result3=Calculator(-1,-1)
        self.assertEqual(result1.add(),12)
        self.assertEqual(result2.add(), 0)
        self.assertEqual(result3.add(), -2)

    def test_sub(self):
        result1 = Calculator(10, 2)
        result2 = Calculator(-1, 1)
        result3 = Calculator(-1, -1)
        self.assertEqual(result1.sub(), 8)
        self.assertEqual(result2.sub(), -2)
        self.assertEqual(result3.sub(), 0)

    def test_mul(self):
        result1 = Calculator(10, 2)
        result2 = Calculator(-1, 1)
        result3 = Calculator(-1, -1)
        self.assertEqual(result1.mul(), 20)
        self.assertEqual(result2.mul(), -1)
        self.assertEqual(result3.mul(), 1)

    def test_div(self):
        result1 = Calculator(10, 2)
        result2 = Calculator(-1, 1)
        result3 = Calculator(-1, -1)
        result4=Calculator(10,0)
        self.assertEqual(result1.div(), 5)
        self.assertEqual(result2.div(), -1)
        self.assertEqual(result3.div(), 1)

        with self.assertRaises(ValueError):
            result4.div()



if __name__=='__main__':
    unittest.main()