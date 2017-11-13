import fracs as fra
import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertFalse(fra.add_frac([1,0],[2,6]))
        self.assertEqual(fra.add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(fra.add_frac([0,1],[5,6]),[5,6])

    def test_sub_frac(self):
        self.assertFalse(fra.sub_frac([1,0],[2,6]))
        self.assertEqual(fra.sub_frac([2,24],[17,12]),[-4,3])

    def test_mul_frac(self):
        self.assertEqual(fra.mul_frac([2,8],[4,8]),[1,8])
        self.assertEqual(fra.mul_frac([-2,5],[1,-6]),[1,15])

    def test_div_frac(self):
        self.assertFalse(fra.div_frac([1,0],[2,2]))
        self.assertEqual(fra.div_frac([1,10],[1,5]),[1,2])
        self.assertEqual(fra.div_frac([-2,5],[1,-6]),[12,5])

    def test_is_positive(self):
        self.assertFalse(fra.is_positive([0,-1]))
        self.assertTrue(fra.is_positive([2,4]))

    def test_is_zero(self):
        self.assertTrue(fra.is_zero([0,4]))
        self.assertFalse(fra.is_zero([7,0]))
        self.assertFalse(fra.is_zero([4,5]))

    def test_cmp_frac(self):
        self.assertEqual(fra.cmp_frac([-12,13],[-14,15]),1)
        self.assertEqual(fra.cmp_frac([12,13],[14,15]),-1)
        self.assertEqual(fra.cmp_frac([2,4],[32,64]),0)

    def test_frac2float(self):
        self.assertEqual(fra.frac2float([1,8]),0.125)
        self.assertEqual(fra.frac2float([-3,12]),-0.25)
        self.assertAlmostEqual(fra.frac2float([2,3]),0.666,places=2)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy