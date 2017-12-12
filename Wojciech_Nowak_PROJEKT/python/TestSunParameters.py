import unittest
import SunParameters as  sp

class TestSunParameters(unittest.TestCase):
    def setUp(self):
        self.zero = sp.SunParameters()

    def testGetSunrise(self):
        sun = sp.SunParameters()
        sunrise = sun.getSunrise()
        time = sunrise.split(':', 1)
        self.assertGreaterEqual(int(time[0])*100+int(time[1]), 353)
        self.assertLessEqual(int(time[0])*100+int(time[1]), 740)

    def testGetSunset(self):
        sun = sp.SunParameters()
        sunset = sun.getSunset()
        time = sunset.split(':', 1)
        self.assertGreaterEqual(int(time[0])*100+int(time[1]), 1505)
        self.assertLessEqual(int(time[0])*100+int(time[1]), 2133)

if __name__ == '__main__':
    unittest.main()