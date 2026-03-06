import unittest
import sys
import os

# เพิ่ม Path เพื่อให้หาโฟลเดอร์ src เจอ
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.funny_string import funnyString
from src.alternating_characters import alternatingCharacters
from src.caesar_cipher import caesarCipher
from src.two_characters import twoCharacters
from src.grid_challenge import gridChallenge

class TestHackerRank(unittest.TestCase):
    
    # --- Funny String ---
    def test_funnyString_basic(self):
        self.assertEqual(funnyString("acxz"), "Funny")
        self.assertEqual(funnyString("bcxz"), "Not Funny")
        
    def test_funnyString_edge(self):
        self.assertEqual(funnyString("aaaaa"), "Funny") # ทุกตัวเหมือนกัน

    # --- Alternating Characters ---
    def test_alternating_basic(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)
        self.assertEqual(alternatingCharacters("ABABAB"), 0)
        
    def test_alternating_no_deletions(self):
        self.assertEqual(alternatingCharacters("ABCDE"), 0)

    # --- Caesar Cipher ---
    def test_caesar_basic(self):
        self.assertEqual(caesarCipher("middle-Outz", 2), "okffng-Qwvb")
        
    def test_caesar_rotations(self):
        self.assertEqual(caesarCipher("abc", 0), "abc")   # No shift
        self.assertEqual(caesarCipher("abc", 26), "abc")  # Full circle
        self.assertEqual(caesarCipher("abc", 52), "abc")  # Multiple circles
        self.assertEqual(caesarCipher("!@#", 5), "!@#")   # Symbols only

    # --- Two Characters ---
    def test_twoChars_basic(self):
        self.assertEqual(twoCharacters("beabeefeab"), 5)
        
    def test_twoChars_invalid(self):
        self.assertEqual(twoCharacters("aaaaa"), 0) # ตัวเดียวทำคู่ไม่ได้
        self.assertEqual(twoCharacters("abcde"), 2) # สุ่มมาคู่หนึ่งที่สลับกัน

    # --- Grid Challenge ---
    def test_grid_basic(self):
        self.assertEqual(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']), "YES")
        
    def test_grid_fail(self):
        self.assertEqual(gridChallenge(['mpxz', 'abcd', 'wlmf']), "NO")
        
    def test_grid_single(self):
        self.assertEqual(gridChallenge(['a']), "YES") # 1x1 grid

# ใส่ pragma: no cover เพื่อให้เครื่องมือตรวจ Coverage ข้ามบรรทัดนี้ไป
if __name__ == '__main__': # pragma: no cover
    unittest.main()