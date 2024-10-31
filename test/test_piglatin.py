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


    def test_translate_phrase_starts_with_vowel_ends_in_y(self):
        phrase = "any"
        translator = PigLatin(phrase)
        translator.translate()
        self.assertEqual("anynay", translator.get_phrase())


    def test_translate_phrase_starts_with_vowel_ends_in_vowel_not_y(self):
        phrase = "apple"
        translator = PigLatin(phrase)
        translator.translate()
        self.assertEqual("appleyay", translator.get_phrase())

    def test_translate_phrase_starts_with_vowel_ends_in_consonant(self):
        phrase = "ask"
        translator = PigLatin(phrase)
        translator.translate()
        self.assertEqual("askay", translator.get_phrase())

    def test_translate_phrase_starts_with_consonant(self):
        phrase = "hello"
        translator = PigLatin(phrase)
        translator.translate()
        self.assertEqual("ellohay", translator.get_phrase())


