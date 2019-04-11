import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        loc = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc),"Location('Paris', 48.9, 2.4)")

    def test_eq(self):
       loc1 = Location("SLO", 35.3, -120.7)
       loc2 = Location("Paris", 48.9, 2.4)
       self.assertEqual(__eq__(loc1,loc2), False)
       loc1 = Location("SLO", 35.3, -120.7)
       loc2 = Location("SLO", 35.3, -120.7)
       self.assertEqual(__eq__(loc1, loc2), True)

if __name__ == "__main__":
        unittest.main()
