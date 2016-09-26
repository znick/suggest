#!/usr/bin/env python3

import unittest
import suggest
import tempfile
import os

class TestSuggester(unittest.TestCase):
    def setUp(self):
        self.words_filename = tempfile.mkstemp()[1]
        with open(self.words_filename, "w") as fn:
            fn.write("раз\n")
            fn.write("два\n")

        self.suggester = suggest.Suggester(self.words_filename)

    def tearDown(self):
        os.unlink(self.words_filename)

    def test_basic(self):
        self.assertIn("раз", self.suggester.get("раз"))

    def test_prefix(self):
        self.assertIn("раз", self.suggester.get("р"))

    def test_not_found(self):
        self.assertNotIn("три", self.suggester.get("три"))

    def test_bad_file(self):
        with self.assertRaises(FileNotFoundError):
            suggest.Suggester("no_such_file")

if __name__ == '__main__':
    unittest.main()
