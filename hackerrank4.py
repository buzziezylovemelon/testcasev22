import unittest

def alternate(s):
    lens = [0]
    letters = list(set(list(s)))
    for letter1 in range(len(letters)):
        for letter2 in range(letter1 + 1, len(letters)):
            two = []
            for letter in s:
                if letter == letters[letter1]:
                    if two:
                        if two[-1] == letters[letter2]:
                            two.append(letter)
                        else:
                            two = []
                            break
                    else:
                        two.append(letter)
                elif letter == letters[letter2]:
                    if two:
                        if two[-1] == letters[letter1]:
                            two.append(letter)
                        else:
                            two = []
                            break
                    else:
                        two.append(letter)
            lens.append(len(two))
    return max(lens)

class Test_alternate(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(alternate("ababababa"), 5)  # "babab" or "ababa"
        self.assertEqual(alternate("cccc"), 0)
        self.assertEqual(alternate("xyzxyz"), 2)  # "xy" or "yz" or "zx"
        self.assertEqual(alternate("abcdabcd"), 8)
        self.assertEqual(alternate("z"), 0)
        self.assertEqual(alternate(""), 0)
        self.assertEqual(alternate("xyxyxyxyxyxyxyxy"), 16)
        self.assertEqual(alternate("dddddddddddddddddddd"), 0)
        self.assertEqual(alternate("ab"), 2)

Test_alternate()
print("All passed")