from caepy import decrypt, encrypt
import unittest
from unittest import TestCase

test_strings = (("test 123", "whvw 123"),
                ("with special characters!", "zlwk vshfldo fkdudfwhuv!"))


class EncryptionTestCase(TestCase):
    def testStringFunctionEncryption(self):
        for first, second in test_strings:
            result = encrypt(first)
            self.assertEqual(second, result)


class DecryptionTestCase(TestCase):
    def testStringFunctionEncryption(self):
        for first, second in test_strings:
            result = decrypt(second)
            self.assertEqual(first, result)


if __name__ == "__main__":
    unittest.main()
