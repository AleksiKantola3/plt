import unittest

import piglatin
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_input_phrase(self):
        phrase = "hello world"
        translator = PigLatin(phrase)
        self.assertEqual(phrase, translator.get_phrase())


    def test_input_empty_phrase(self):
        phrase = ""
        translator = PigLatin(phrase)
        self.assertEqual("nil", translator.get_phrase())
