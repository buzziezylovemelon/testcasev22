import unittest


def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i] = sorted(list(grid[i]))
    for x in list(zip(*grid)):
        if list(x) != sorted(x):
            return "NO"
    return "YES"

class Test_gridChallenge(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(gridChallenge(["def", "abc", "xyz"]), "YES")
        self.assertEqual(gridChallenge(["ghi", "jkl", "mno"]), "YES")
        self.assertEqual(gridChallenge(["xyz"]), "YES")
        self.assertEqual(gridChallenge(["q", "r", "s"]), "YES")
        self.assertEqual(gridChallenge(["zzz", "zzz", "zzz"]), "YES")
        self.assertEqual(gridChallenge(["cab", "acb", "bca"]), "YES")
        self.assertEqual(gridChallenge([]), "YES")
        self.assertEqual(gridChallenge(["z"]), "YES")
        self.assertEqual(gridChallenge(["abc", "def", "ghi"]), "NO")
        self.assertEqual(gridChallenge(["zyx", "wvu", "tsr"]), "NO")


Test_gridChallenge()
print("All passed")