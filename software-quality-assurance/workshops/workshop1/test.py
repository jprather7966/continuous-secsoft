import unittest
import source 


class TestCalc(unittest.TestCase):
    def testSub1(self):
        self.assertEqual(1, source.performSub(2, 1), "Results should be 1.")    

    def testSub2(self):
        self.assertEqual(31, source.performSub(53, 22), "Results should be 31.")  

    def testMult1(self):
        self.assertEqual(286, source.performMult(22, 13), "Results should be 286.")
    
    def testMult2(self):
        self.assertEqual(50, source.performMult(5, 10), "Results should be 50.")

    def testDiv1(self):
        self.assertEqual(2, source.performDiv(20, 10), "Results should be 2.")

    def testDiv2(self):
        self.assertEqual(ZeroDivisionError, source.performDiv(20, 0), "Divide by Zero test case. Results should throw a ZeroDivisonError.")
    
    def testDiv3(self):
        self.assertEqual(0, source.performDiv(0, 20), "Results should be 0.")

    def testDivZero(self):
        self.assertEqual("Put in correct divisor", source.performSub(20, 0), "Bug in implementation.")    

if __name__ == '__main__': 
    unittest.main() 