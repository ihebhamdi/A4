import unittest
from src.main import add, generate_password, generate_sha256
import string

class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 4), 6)
        self.assertEqual(add(-1, 3), 2)
        self.assertEqual(add(-1, -2), -3)

class TestPasswordGenerator(unittest.TestCase):

    def test_generate_password_length(self):
        password = generate_password(8)
        self.assertEqual(len(password), 8)
        password = generate_password(12)
        self.assertEqual(len(password), 12)

    def test_generate_password_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(7)
        with self.assertRaises(ValueError):
            generate_password(13)

    def test_generate_password_characters(self):
        password = generate_password(10)
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

class TestSHA256(unittest.TestCase):

    def test_generate_sha256(self):
        self.assertEqual(generate_sha256('test'), '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08')

if __name__ == '__main__':
    unittest.main()
