import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        tlist = None
        with self.assertRaises(ValueError):                 # used to check for exception
            max_list_iter(tlist)
    def test_max_list_iter_all_positions(self):             #works if max is in any part of list
        tlist = [1,2,3]
        self.assertEqual(max_list_iter(tlist),3)
        tlist = [1,3,2]
        self.assertEqual(max_list_iter(tlist), 3)
        tlist = [3,1,2]
        self.assertEqual(max_list_iter(tlist), 3)
    def test_max_list_iter_two_small_same(self):            #works if multiples of smaller number
        tlist = [2,2,4]
        self.assertEqual(max_list_iter(tlist), 4)
        tlist = [2,4,2]
        self.assertEqual(max_list_iter(tlist), 4)
        tlist = [4,2,2]
        self.assertEqual(max_list_iter(tlist), 4)
    def test_max_list_iter_two_large_same(self):            #works if multiples of max number
        tlist = [4,4,2]
        self.assertEqual(max_list_iter(tlist), 4)
        tlist = [4,2,4]
        self.assertEqual(max_list_iter(tlist), 4)
        tlist = [2,4,4]
        self.assertEqual(max_list_iter(tlist), 4)
    def test_max_list_iter_all_same(self):                  #if all max
        tlist = [4,4,4]
        self.assertEqual(max_list_iter(tlist), 4)
    def test_max_list_iter_floats(self):                    #if used floats instead
        tlist = [1.1,1.2,1.3]
        self.assertEqual(max_list_iter(tlist), 1.3)
        tlist = [1.1,1.3,1.2]
        self.assertEqual(max_list_iter(tlist), 1.3)
        tlist = [1.3,1.1,1.2]
        self.assertEqual(max_list_iter(tlist), 1.3)




    def test_reverse_rec(self):
        #self.assertEqual(reverse_rec([]), ?)
        self.assertEqual(reverse_rec([1]), [1])
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])





    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

if __name__ == "__main__":
        unittest.main()


