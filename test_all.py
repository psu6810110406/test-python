import unittest
# Import ฟังก์ชันจากแต่ละไฟล์
from funny_string import funnyString
from alternating_characters import alternatingCharacters
from caesar_cipher import caesarCipher
from two_characters import twoCharacters
from grid_challenge import gridChallenge

class TestHackerRank(unittest.TestCase):
    def test_funnyString(self):
        self.assertEqual(funnyString("acxz"), "Funny")
        self.assertEqual(funnyString("bcxz"), "Not Funny")

    def test_alternatingCharacters(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)
        self.assertEqual(alternatingCharacters("ABABAB"), 0)

    def test_caesarCipher(self):
        self.assertEqual(caesarCipher("middle-Outz", 2), "okffng-Qwvb")
        self.assertEqual(caesarCipher("!@#", 2), "!@#") # Test non-alpha

    def test_twoCharacters(self):
        self.assertEqual(twoCharacters("beabeefeab"), 5)
        self.assertEqual(twoCharacters("abcde"), 2)

    def test_gridChallenge(self):
        self.assertEqual(gridChallenge(['abc', 'ade', 'efg']), "YES")
        self.assertEqual(gridChallenge(['zyx', 'wvu', 'tsr']), "NO")

if __name__ == '__main__':
    unittest.main()