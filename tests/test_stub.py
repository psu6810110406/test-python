import unittest
from unittest.mock import patch

class TestWithStub(unittest.TestCase):
    # Stub ให้ caesarCipher คืนค่าคงที่เสมอ
    @patch('src.caesar_cipher.caesarCipher')
    def test_caesar_logic_isolation(self, mock_caesar):
        mock_caesar.return_value = "FIXED_RESULT"
        # แม้จะใส่ k=999 ผลลัพธ์ต้องออกมาตามที่ Stub ไว้
        from src.caesar_cipher import caesarCipher
        self.assertEqual(caesarCipher("any_text", 999), "FIXED_RESULT")