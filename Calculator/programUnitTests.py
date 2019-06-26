import unittest
from Program import add,sub,mult,div

class MyTestCase(unittest.TestCase):
    def test_add(self):
        num1 = 5
        num2 = 7
        result = add(num1,num2)
        self.assertEqual(result, 12)
        self.assertEqual(add(1,2),3)
        self.assertEqual(add(-4,6),2)
        self.assertEqual(add(1,4.5),5.5)
        self.assertEqual(add(-10,10),0)
        self.assertEqual(add(155,200),355)
    def test_sub(self):
        self.assertEqual(sub(4,2),2)
        self.assertEqual(sub(-5,-5),0)
if __name__ == '__main__':
    unittest.main()
