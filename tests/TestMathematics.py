#TestMathematics

#Import Statements
import unittest
import MathFunctions

class KnownValues(unittest.TestCase)

    #Test areaSquare() l^2

    def test_square_area_for_5length(self):
        #capture results of MathFunctions
        result = MathFunctions.areaSquare(5)
        #Check for expected output
        expected = 25
        self.assertEqual(expected, result)

    #Run test
    if__name__=='__main__':
        unnittest.main()        

