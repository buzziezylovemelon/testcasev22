import unittest


def funnyString(s):
    n = len(s)
    for i in range(1, n):
        start_diff = abs(ord(s[i]) - ord(s[i - 1]))
        end_diff = abs(ord(s[n - i] ) - ord(s[n - i - 1]))  # ใช้ s[n - i]
        if start_diff != end_diff:
            return 'Not Funny'
    return 'Funny'
class TestFunnyString(unittest.TestCase):
    def test_funnyString(self):
        self.assertEqual(funnyString("hello"), "Not Funny")
        self.assertEqual(funnyString("madam"), "Funny")
        self.assertEqual(funnyString("robot"), "Not Funny")
        self.assertEqual(funnyString("noon"), "Funny")
        self.assertEqual(funnyString("world"), "Not Funny")
        self.assertEqual(funnyString("deified"), "Funny")
        self.assertEqual(funnyString("python"), "Not Funny")
        self.assertEqual(funnyString("level"), "Funny")

TestFunnyString()
print("All passed")
