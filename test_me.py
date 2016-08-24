#!/usr/bin/python
# -*- coding: utf-8 -*-

from caepy import encrypt, decrypt, helper
import unittest


class Encryption(unittest.TestCase):
	test_strings = ( ("test 123", "whvw 123"),
					("with special characters!", "zlwk vshfldo fkdudfwhuv!") )
	
	
	def testStringHelperEncryption(self):
		for first, second in self.test_strings:
			result = helper(first, 3)
			self.assertEqual(second, result)
	
	def testStringFunctionEncryption(self):
		for first, second in self.test_strings:
			result = encrypt(first)
			self.assertEqual(second, result)
			
			
class Decryption(unittest.TestCase):
	test_strings = ( ("test 123", "whvw 123"),
					("with special characters!", "zlwk vshfldo fkdudfwhuv!") )
	
	
	def testStringHelperEncryption(self):
		for first, second in self.test_strings:
			result = helper(second, -3)
			self.assertEqual(first, result)
			
	def testStringFunctionEncryption(self):
		for first, second in self.test_strings:
			result = decrypt(second)
			self.assertEqual(first, result)
	

if __name__ == "__main__":
    unittest.main()
