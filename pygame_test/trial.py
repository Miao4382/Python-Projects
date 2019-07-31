import unittest
from student import Solution


class TestStringMethods(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution.exist([["a", "b"],["c", "d"]], "abcd"), False)
        # self.assertEqual(Solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"), True)
        # self.assertEqual(Solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"), True)
        # self.assertEqual(Solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB"), False)
        # self.assertEqual(Solution.exist([["a"]],"ab"), False)
        # self.assertEqual(Solution.exist(["a","a"],"aaa"), False)


# Driver function
if __name__ == "__main__":
    unittest.main()
