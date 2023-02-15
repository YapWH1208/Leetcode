import unittest
from Greedy376 import Solution

class TestSolution(unittest.TestCase):
    def test_wiggleMaxLength(self):
        self.assertEqual(Solution().wiggleMaxLength([1,7,4,9,2,5]),6)
        self.assertEqual(Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]),7)
        self.assertEqual(Solution().wiggleMaxLength([1,2,3,4,5,6,7,8,9]),2)