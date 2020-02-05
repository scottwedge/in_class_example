#TestMathematics

#Import Statements
import unittest

import WorkShopTwo.Mathematics as WorkMath


class KnownValues(unittest.TestCase):

    #Test areaSquare() l^2

    def test_square_area_for_5length(self):
        #capture results of MathFunctions
        result = WorkMath.areaSquare(5)
        #Check for expected output
        expected = 25
        self.assertEqual(expected, result)

    #Run test
    if __name__=='__main__':
        unittest.main()        

